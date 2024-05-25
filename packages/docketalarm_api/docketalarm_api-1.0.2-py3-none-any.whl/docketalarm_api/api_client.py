import requests
import logging
import json
import re

from urllib.parse import urlencode


GPT_3_5_TURBO = "gpt-3.5-turbo-1106"
GPT_4_TURBO = "gpt-4-1106-preview"


class BadRequest(Exception): pass


class DocketAlarmClient():
    """
    Main client to interact with DocketAlarm API endpooints
    :param user: DocketAlarm user
    :param password: DocketAlarm password
    :param openai_api_key: OpenAI API key to use on OpenAIEndpoints
    """
    URL = "https://www.docketalarm.com/api/v1/"

    def __init__(self, user:str, password:str, openai_api_key:str="") -> None:
        self._user = user
        self._password = password
        self._openai_api_key = openai_api_key

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)


    def openaimethod(func):
        def wrapper(self, *args, **kwargs):
            assert self.is_openai_valid_api_key(self._openai_api_key), "Valid OpenAI key not set"
            return func(self, *args, **kwargs)
        return wrapper
    

    def get_login_token(self) -> str:
        """
        Get login token
        :return: token (str)
        """
        response = self._make_post_request("login/", {"username": self._user,
                                                      "password": self._password})
        
        if not response.get("success"):
            error = response.get('error')
            self.logger.warning("Bad request: %s" % error)
            raise BadRequest(f"error: {error}")
        
        return response.get("login_token")
    

    def __make_request(self, endpoint:str, method:str,
                      data:dict=None, timeout:int=None):
        data = data or {}
        method = method.upper()
        params = {
            "method": method,
            "url": self.URL+endpoint,
            "timeout": timeout
        }

        if method=="POST":
            params["data"] = data

        response = requests.request(**params)
        if response.status_code != 200:
            error = f"status: {response.status_code}, text: {response.text}"
            self.logger.warning("Bad request: %s" % error)
            raise BadRequest(error)
        
        json_response = response.json()
        if not json_response.get("success", False):
            error = json.dumps(json_response)
            self.logger.warning("Bad request: %s" % error)
            raise BadRequest(error)
        
        return json_response
    

    def _make_post_request(self, endpoint:str, data:dict):
        return self.__make_request(endpoint, "POST", data)
    

    def _make_get_request(self, endpoint:str, params:dict=None, timeout:int=None):
        params = params or {}
        endpoint=f"{endpoint}?{urlencode(params)}"
        return self.__make_request(endpoint, "GET", timeout=timeout)

    
    def search(self, query:str, order:str, limit:int=50,
               offset:int=0, login_token:str="") -> dict:
        """
        Perform a search on DocketAlarm API's search endpoint
        :param query: The DocketAlarm query to use.
        :param order: The order to get the results by.
        :param limit: the search limit, must be 50 or less.
        :param offset: Offset for the search, usefull for pagination.
        :param login_token: Will be created if not provided
        :return: dictionary with json response
        """
        
        login_token = login_token or self.get_login_token()
        
        # Force limit to be at most 50
        limit = limit if isinstance(limit, int) and limit <= 50 else 50

        params = {"login_token": login_token, "q": query, "o": order, "limit": limit, "offset": offset}
        response = self._make_get_request("search/", params)
        
        return response
    
    
    def get_docket(self, docket:str, court:str, **kwargs) -> dict:
        """
        Interact with the getdocket endpoint.
        :param docket: The docket number obtained from search.
        :param court: The court of the docket obtained from search
        :kwarg timeout: Timout for the GET request.
        :kwarg client_matter: The client matter for the API call.
        :kwarg normalize: normalize option for getdocket endpoint.
        :kwarg cached: Defaults to True, gets cached version of the docket
        :kwarg login_token: If not provided it's auto generated
        :kwarg check_is_pacer: Includes a boolean showing whether the
                               case is from a PACER court or not.
        :kwarg add_documents_by_entries: Includes a list of all documents for
                                     each entry in the main response body 
        :return: dictionary with json response
        """
        timeout = kwargs.get("timeout")
        client_matter = kwargs.get("client_matter", "")
        extra_keys = ["normalize", "cached", "login_token", "check_is_pacer", "add_documents_by_entries"]
        basic_params = [("docket", docket), ("client_matter", client_matter), ("court", court)]
        params = dict(basic_params+[(key, kwargs.get(key)) for key in extra_keys if key in kwargs])

        if not "cached" in params:
            params["cached"] = True
        
        self.logger.info("Fetching docket using cached=%s" % params["cached"])
            
        if not params.get("login_token"):
            params["login_token"] = self.get_login_token()

        return self._make_get_request("getdocket/", params=params, timeout=timeout)
    

    def get_document_binary(self, doc_url:str, login_token:str="", client_matter:str="", cached:bool=True) -> bytes:
        """
        Fetches the binary content of a pdf stored in DocketAlarm or directly from the court.
        :param doc_url: Url for the document.
        :param login_token: Token for DocketAlarm authentication.
        :param client_matter: The matter or client for the API call.
        :param cached: Boolean stating if desired to use cached version of the document or not.
        :return: document binarty (bytes)
        """
        if not doc_url.endswith(".pdf") or not doc_url.startswith("https://www.docketalarm.com"):
            raise BadRequest("A DocketAlarm document URL must be provided")
        
        login_token = login_token or self.get_login_token()
        
        doc_url += f"?login_token={login_token}"
        if client_matter:
            doc_url += f"&client_matter={client_matter}"
        if cached:
            doc_url += "&cached"

        response = requests.get(doc_url)
        if response.status_code != 200:
            raise BadRequest(f"status: {response.status_code}, text: {response.text}")
        
        return response.content
    

    @openaimethod
    def ask_docket(self, docket:str, court:str, question:str, output_format:dict,
                   target:str, client_matter:str="", **kwargs) -> dict:
        """
        Interact with ask_docket endpoint.
        :param docket: The docket number as extracted from search.
        :param court: The court of the docket as extracted from search
        :param question: The question to ask to the docket data.
        :param output_format: The output format of the desired response in natural language.
        :param target: The target for ask_docket, "dockets", "documents" or "both"
        :kwarg openai_model: Model to be use on openai interactions, by default uses gpt-3.5-turbo-1106
        :kwarg cached: Gets cached version of the docket on the interaction, defaults to False.
        :kwarg show_relevant: Gets relevant data used by ask_docket.
        :kwarg login_token: If not provided is autogenerated
        :return: dictionary with json response
        """
        
        extra_keys = ["openai_model", "cached", "show_relevant", "login_token"]
        basic_params = [("docket", docket), ("client_matter", client_matter),
                        ("court", court), ("question", question), ("output_format", output_format),
                        ("openai_key", self._openai_api_key), ("target", target)]
        params = dict(basic_params+[(key, kwargs.get(key)) for key in extra_keys if key in kwargs])

        if not "cached" in params:
            params["cached"] = False
        
        self.logger.info("Executing ask_docket using cached=%s" % params["cached"])

        if not params.get("login_token"):
            params["login_token"] = self.get_login_token()

        timeout = kwargs.get("timeout")

        return self._make_get_request("ask_docket/", params, timeout)


    @openaimethod
    def case_matcher(self, **kwargs) -> dict:
        """
        Match a case from any arguments provided.
        :kwarg openai_model: The OpenAI model to use during case matching
        :kwargs: Provide any argument and will be used as inputs in case matcher
        :return: dict with result from case matcher and OpenAI costs incurred
        """
        login_token = kwargs.get("login_token", self.get_login_token())
        client_matter = kwargs.get("client_matter", "")
        params = dict(login_token=login_token, openai_key=self._openai_api_key,
                      client_matter=client_matter, **kwargs)
        return self._make_get_request("case_matcher/", params)
    

    @openaimethod
    def smart_search(self, instructions:str,
                     openai_model:str=GPT_4_TURBO,
                     login_token:str="") -> dict:
        """
        Return a query for DocketAlarm search based on instructions in natural language.
        :param instructions: Instructions to build a query by.
        :param openai_model: OpenAI model to be used when generating the query
        :param login_token: If not provided will be auto-generated.
        :return: dictionary with query and OpenAI costs incurred.
        """
        login_token = login_token or self.get_login_token()
        params = {"login_token": login_token, "openai_key": self._openai_api_key,
                  "openai_model": openai_model, "instructions": instructions}
        return self._make_get_request(endpoint="smart_search/", params=params)
    

    @openaimethod
    def attorney_billing_rates(self, attorney_name:str, state:str=None, **kwargs) -> dict:
        """
        Extract attorney billing rates by name and state.
        :param attorney_name: The name of the attorney for which billing rates are to be extracted.
        :param state: The state of the attorney.
        :kwarg openai_model: OpenAI model to be used on the API call.
        :kwarg login_token: Auto generated by default.
        :kwarg client_matter: Empty by default.
        :return: dictionary with result and OpenAI costs incurred
        """
        extra_keys = ["openai_model", "login_token", "client_matter"]
        basic_params = [("attorney_name", attorney_name), ("state", state), ("openai_key", self._openai_api_key)]
        params = dict(basic_params+[(key, kwargs.get(key)) for key in extra_keys if key in kwargs])

        if not params.get("login_token"):
            params["login_token"] = self.get_login_token()
    
        if not params.get("client_matter"):
            params["client_matter"] = ""

        return self._make_get_request("attorney_billing_rates/", params)
    

    @openaimethod
    def get_complaint_summary(self, docket:str, court:str, **kwargs) -> dict:
        """
        Get a summary of the legal complaint in the docket.
        :param docket: Docket number.
        :param court: The court of the docket.
        :kwarg openai_model: The OpenAI model to be used on the API call.
        :kwarg login_token: Auto generated by default.
        :kwarg cached: Bool stating if desired to use cached version of the docket.
        :kwarg short: Extract a short complaint summary
        :return: dictionary with complaint summary and OpenAI costs incurred
        """
        extra_keys = ["openai_model", "login_token", "cached", "short"]
        basic_params = [("docket", docket), ("court", court), ("openai_key", self._openai_api_key)]
        params = dict(basic_params+[(key, kwargs.get(key)) for key in extra_keys if key in kwargs])

        if not params.get("login_token"):
            params["login_token"] = self.get_login_token()
        
        return self._make_get_request("get_complaint_summary/", params)


    @openaimethod
    def get_cause_of_action(self, docket:str, court:str, **kwargs) -> dict:
        """
        Get the causes of action from a legal complaint.
        :param docket: Docket number.
        :param court: The court of the docket.
        :kwarg openai_model: The OpenAI model to be used on the API call.
        :kwarg login_token: Auto generated by default.
        :kwarg cached: Bool stating if desired to use cached version of the docket.
        :return: Dictionary with cause of action and OpenAI costs incurred
        """
        extra_keys = ["openai_model", "login_token", "cached"]
        basic_params = [("docket", docket), ("court", court), ("openai_key", self._openai_api_key)]
        params = dict(basic_params+[(key, kwargs.get(key)) for key in extra_keys if key in kwargs])

        if not params.get("login_token"):
            params["login_token"] = self.get_login_token()
        
        return self._make_get_request("get_cause_of_action/", params)


    @openaimethod
    def entity_normalizer(self, entity, include_corp_group:bool=False,
                          search_limit:int=10, login_token:str="") -> dict:
        """
        Get a DocketAlarm query for the entity normalized
        :param entity: The entity to normalize.
        :param include_corp_group: Boolean stating if desired to include corporation group matches.
        :param search_limit: The internal search limit when optimizing. Must be between 10 and 50.
        :param login_token: If not provided is autogenerated.
        """
        params = {
            "entity": entity,
            "login_token": login_token or self.get_login_token(),
            "search_limit": search_limit,
            "openai_key": self._openai_api_key
        }
        if include_corp_group:
            params["include_corporate_group"] = True
        
        return self._make_get_request("entity_normalizer/", params)


    @staticmethod
    def is_openai_valid_api_key(openai_api_key:str) -> bool:
        """
        Check if an OpenAI API key is valid or not.
        :param openai_api_key: The key to check.
        :return: bool
        """
        if not openai_api_key:
            return False
        pattern = re.compile(r'^(sk-|Bearer )?[a-zA-Z0-9]+$')
        return bool(re.match(pattern, openai_api_key))