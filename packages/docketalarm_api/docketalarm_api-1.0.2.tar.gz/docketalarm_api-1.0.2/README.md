# DocketAlarmAPI
API Wrapper for DocketAlarm.
# Table of Contents
1. [Instalation and usage](#usage)
2. [Get Login Token](#get_login_token)
3. [Search](#search)
4. [Get Docket](#get_docket)
5. [Get Document](#get_document_binary)
6. [Ask Docket](#ask_docket)
7. [Case Matcher](#case_matcher)
8. [Smart Search](#smart_search)
9. [Attorney Billing Rates](#attorney_billing_rates)
10. [Get Complaint Summary](#get_complaint_summary)
11. [Get Cause of Action](#get_cause_of_action)

# usage
Use `pip install docketalarm_api` to install this library.  
To use the DocketAlarmClient you'll need your DocketAlarm user and password, and if desired to interact with OpenAI powered endpoints, an OpenAI API Key.  
Import and initialize the client as follows:
```
from docketalarm_api import DocketAlarmClient

da_client = DocketAlarmClient(<your-docketalarm-user>, <your-docketalarm-password>, <your-openai-api-key>)
```

# General Endpoints
These are methods available directly to your DocketAlarm user through a `DocketAlarmClient` instance.

## get_login_token
Get authentication token from docketalarm.  

**Example**:

```
    from docketalarm_api import DocketAlarmClient

    da_client = DocketAlarmClient(<your-docketalarm-user>, <your-docketalarm-password>, <your-openai-api-key>)
    login_token = da_client.get_login_token()
```

## search
Perform a search on DocketAlarm API's search endpoint.  

| Parameter    | Description                                         |
|--------------|-----------------------------------------------------|
| query        | The DocketAlarm query to use.                       |
| order        | The order to get the results by.                    |
| limit        | The search limit, must be 50 or less.               |
| offset       | Offset for the search, useful for pagination.       |
| login_token  | Will be created if not provided.                    |
| return       | Dictionary with JSON response.                      |

**Example**:

```
    response = da_client.search("is:docket AND is:state", "random", limit=10)
    search_results = response["search_results"]
```

## get_docket
Interact with getdocket endpoint, fetching a docket by court and docket number.  

| Parameter               | Description                                                |
|-------------------------|------------------------------------------------------------|
| docket                  | The docket number obtained from search.                    |
| court                   | The court of the docket obtained from search.              |
| timeout                 | Timeout for the GET request.                               |
| client_matter           | The client matter for the API call.                        |
| normalize               | Normalize option for getdocket endpoint.                   |
| cached                  | Defaults to True, gets cached version of the docket.       |
| login_token             | If not provided it's auto-generated.                       |
| check_is_pacer          | Include a boolean stating if the case is from a PACER court|
| add_documents_by_entries| Include a list of all documents per entry on the response  |
| return                  | Dictionary with JSON response.                             |

**Example**:

```
    docket_data = da_client.get_docket(docket="JC205-106", court="Texas State, Grayson County, Justice of the Peace 2")
```

## get_document_binary
Fetches the binary content of a pdf stored in DocketAlarm or directly from the court.  

| Parameter    | Description                                                              |
|--------------|--------------------------------------------------------------------------|
| doc_url      | URL for the document.                                                    |
| login_token  | Token for OpenAI authentication.                                         |
| client_matter| The matter or client for the API call.                                   |
| cached       | Boolean stating if desired to use cached version of the document or not. |
| return       | Document binary (bytes).                                                 |

**Example**:

```
    document_bytes = da_client.get_document_binary(
        'https://www.docketalarm.com/cases/Arkansas_State_Faulkner_County_Circuit_Court/23DR-98-821/OCSE_V_JOHN_TAYLOR/docs/28082014_OTHER_0.pdf'
    )
```

# OpenAI Endpoints

These methods require the use of an OpenAI API key, suplied when initializing the instance.  
You can check if an OpenAI API key is valid using the `DocketAlarmClient.is_openai_valid_api_key` method.

## ask_docket
Interact with DocketAlarm's ask_docket OpenAI endpoint.  

| Parameter       | Description                                                              |
|-----------------|--------------------------------------------------------------------------|
| docket          | The docket number as extracted from search.                              |
| court           | The court of the docket as extracted from search.                        |
| question        | The question to ask to the docket data.                                  |
| output_format   | The output format of the desired response in natural language.           |
| target          | The target for ask_docket, "docket", "documents" or "both".              |
| openai_model    | Model to be used on OpenAI interactions, defaults to gpt-3.5-turbo-1106. |
| cached          | Gets cached version of the docket on the interaction, defaults to False. |
| show_relevant   | Gets relevant data used by ask_docket.                                   |
| login_token     | If not provided, it is autogenerated.                                    |
| return          | Dictionary with JSON response.                                           |

**Example**:

```
    response = da_client.ask_docket(docket='JC205-106', court='Texas State, Grayson County, Justice of the Peace 2',
                                    question='is the case pre or post discovery stages?',
                                    output_format='Enum["pre" or "post" or "unknown"]',
                                    target="docket", cached = True)

    openai_answer = response["from_dockets"]["openai_answer"]
```

## case_matcher
Match a case from any input provided using DocketAlarm's OpenAI powered case_matcher endpoint.  

| Parameter       | Description                                                         |
|-----------------|---------------------------------------------------------------------|
| openai_model    | The OpenAI model to use during case matching.                       |
| kwargs          | Provide any argument and it will be used as inputs in case matcher. |
| return          | Dictionary with result from case matcher and OpenAI costs incurred. |

**Example**:

```
    response = da_client.case_matcher(openai_model="gpt-4-1106-preview",
                                    description="A PACER case involving Cloud Systems HoldCo in California")
    case_link = response["result"]["Link"]
```

## smart_search
Return a query for DocketAlarm search based on instructions in natural language  

| Parameter       | Description                                                     |
|-----------------|-----------------------------------------------------------------|
| instructions    | Instructions to build a query by.                               |
| openai_model    | OpenAI model to be used when generating the query.              |
| login_token     | If not provided, it will be auto-generated.                     |
| return          | Dictionary with query and OpenAI costs incurred.                |

**Example**:

```
    response = da_client.smart_search(
        instructions="Cases involving Ford Motor in New York, that span from December 2014 to june 2019"
    )
    query = response["query"]
```

## attorney_billing_rates
Extract attorney billing rates by name and state.  

| Parameter       | Description                                                           |
|-----------------|-----------------------------------------------------------------------|
| attorney_name   | The name of the attorney for which billing rates are to be extracted. |
| state           | The state of the attorney.                                            |
| openai_model    | OpenAI model to be used on the API call.                              |
| login_token     | Auto-generated by default.                                            |
| client_matter   | Empty by default.                                                     |
| return          | Dictionary with result and OpenAI costs incurred.                     |

**Example**

```
    response = da_client.attorney_billing_rates(attorney_name="ashley marshal",
                                                state="connecticut")
    attorney_data = response["result"]
```

## get_complaint_summary
Get a summary of the legal complaint in the docket.  

| Parameter       | Description                                                     |
|-----------------|-----------------------------------------------------------------|
| docket          | Docket number.                                                  |
| court           | The court of the docket.                                        |
| openai_model    | The OpenAI model to be used on the API call.                    |
| login_token     | Auto-generated by default.                                      |
| cached          | Bool stating if desired to use cached version of the docket.    |
| short           | Extract a short complaint summary.                              |
| return          | Dictionary with complaint summary and OpenAI costs incurred.    |

**Example**:

```
    response = da_client.get_complaint_summary(docket="JC205-106", court="Texas State, Grayson County, Justice of the Peace 2",
                                            short=True, openai_model="gpt-4-1106-preview", cached=True)
    openai_answer = response["openai_answer"]
```

## get_cause_of_action
Get the causes of action from a legal complaint.  

| Parameter       | Description                                                     |
|-----------------|-----------------------------------------------------------------|
| docket          | Docket number.                                                  |
| court           | The court of the docket.                                        |
| openai_model    | The OpenAI model to be used on the API call.                    |
| login_token     | Auto-generated by default.                                      |
| cached          | Bool stating if desired to use cached version of the docket.    |
| return          | Dictionary with cause of action and OpenAI costs incurred.      |

**Example**:

```
    response = da_client.get_cause_of_action(docket="JC205-106", court="Texas State, Grayson County, Justice of the Peace 2",
                                            openai_model="gpt-4-1106-preview", cached=True)
    openai_answer = response["openai_answer"]
```

## entity_normalizer
Get a DocketAlarm query for the entity normalized  

| Parameter           | Description                                                            |
|---------------------|------------------------------------------------------------------------|
| entity              | The entity to normalize.                                               |
| include_corp_group  | Boolean stating if desired to include corporation group matches.       |
| search_limit        | The internal search limit when optimizing. Must be between 10 and 50.  |
| login_token         | If not provided, it is autogenerated.                                  |

**Example**:

```
    response = da_client.entity_normalizer(entity="Apple", search_limit=20,
                                           include_corp_group=True)
    query = response["query"]
```