import json

import gandai as ts
from gandai import secrets
from openai import OpenAI

client = OpenAI(
    api_key=secrets.access_secret_version("OPENAI_KEY"),
)

## gpt4


def ask_gpt4(messages: list) -> json:
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
        # model="gpt-4",
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    #
    print(chat_completion.usage)
    return json.loads(chat_completion.choices[0].message.content)


HOW_TO_ENRICH = """
To update an attribute for a company you will create an event with the company's domain
of type "update". This will update that company's meta field 

here is an example update event

{
    "domain": "lol.com",
    "actor_key": "chatgpt",
    "type": "update",
    "data": {
        "contact_name": "Bob"
    }
}

Here are all the fields you can use for event['data']

c.data->>'gpt_description' as gpt_description, -- a description of the company for use by private equity research analyst to understand the company.

You will fill out the description field with a description of the company. 
The description will be a comprehensive description of the company for use 
by private equity research analyst to understand the company.

c.data->>'employees' as employees, -- the INTEGER number of employees at the company. prefer the grata estimate. this is an integer.
c.data->>'ownership' as ownership, -- one of ["bootstrapped","investor_backed","public","public_subsidiary","private_subsidiary","private_equity","private_equity_add_on"] 
c.data->>'headquarters' as headquarters,
c.data->>'city' as city,
c.data->>'state' as state,
c.data->>'designation' as designation,
c.data->>'products' as products, -- products are physical goods sold by the company. do not list services here. A brand is not a product, do not list brands here.
c.data->>'services' as services, -- services are intangible goods offered by the company. do not list products here.
c.data->>'end_customer' as end_customer, -- what types of customers does the company serve. If commercial, what industry(s). do not list specific customers here.
c.data->>'geographies' as geographies, -- geographies are the areas where the company does business. 
c.data->>'year_founded' as year_founded,
c.data->>'linkedin' as linkedin, -- linkedinUrl 
c.data->>'linkedin_range' as linkedin_range,
c.data->>'industry' as industry,
c.data->>'revenue_estimates' as revenue_estimates,
c.data->>'location_count' as location_count,
c.data->>'business_models' as business_models,
c.data->>'facility_size' as facility_size,
c.data->>'contact_name' as contact_name,
c.data->>'contact_title' as contact_title,
c.data->>'contact_email' as contact_email,
c.data->>'contact_phone' as contact_phone,
c.data->>'contact_address' as contact_address,

For fields that are lists, you will use a csv string 
For these lists, such as products or services, try to stick to top 5 or less areas of focus.


If you are unsure, just leave that key out of the response data

"""


HOW_TO_RESPOND = """
You will respond with an JSON object that looks like this:
{
    "events": List[Event],
}
"""

HOW_TO_GOOGLE_MAPS = """
To search the Google Maps Places API
You will respond with this
{"events": List[asdict(Event)]}

Unless otherwise directed you will return 10 centroids

There are 20 results per centroid
So if the user asks for 100 results you will return the count divided by 20

Give me the query strings you would use to search for 
Each query string should be small enough for a Google Maps search

For example to search throughout Dallas you might use:
dentists in Dallas, TX
dentists in Highland Park, TX
dentists in Grapevine, TX
dentists in Plano, TX

Now give me the queries that you would use

Here's some Event examples:
[{
    "type": "maps",
    "search_uid": 1700,
    "actor_key": "7138248581",
    "data": {
        "query": "dentists in Dallas, TX"
    }
}]

"""

HOW_TO_IMPORT = """
// example Import(Event)
{
    "search_uid": 19696114,
    "domain": null,
    "actor_key": "4805705555",
    "type": "import",
    "data": {
        "stage": "advance",
        "domains": [
            "buybits.com",
            "lidoradio.com",
            "rocklandcustomproducts.com",
            "sigmasafety.ca",
        ],
    },
}

Here are the stages along with their labels:
The only valid stages are labelMap.keys()
const labelMap = {
    "land": "Landing",
    "create": "Inbox",
    "advance": "Review",
    "validate": "Validated",
    "send": "Client Inbox",
    "client_approve": "Client Approved",
    "sync": "Synced",
    "reject": "Reject",
    "conflict": "Conflict",
    "client_conflict": "Client Conflict",
    "client_reject": "Client Reject"
}
"""

HOW_TO_TRANSITION = """
To move a target to a different stage you will create an event with the targets domain 
and the stage you want to move it to.

domain should include domain only, no subdomain or protocol

// example Event
{
    "search_uid": 19696114,
    "domain": "acme.com",
    "actor_key": "5558248581",
    "type": "send",
    "data": {"key": "value"},
}


Here are the stages along with their labels:
The only valid event types are the labelMap.keys()
const labelMap = {
    "land": "Landing",
    "create": "Inbox",
    "advance": "Review",
    "validate": "Validated",
    "send": "Client Inbox",
    "client_approve": "Client Approved",
    "sync": "Synced",
    "reject": "Reject",
    "conflict": "Conflict",
    "client_conflict": "Client Conflict",
    "client_reject": "Client Reject"
}
"""

HOW_TO_GOOGLE = """

To search Google, you will create an Event object.

@dataclass
class Google(Event):
    search_uid: int  # fk # add index
    actor_key: str  # fk
    type: str  
    data: dict = field(default_factory=dict)
    id: int = field(default=None)  # pk
    # created: int = field(init=False)

List[Event] examples asdict:

[{
  'search_uid': 200,
  'domain': null,
  'actor_key': '3125740050',
  'type': 'google',
  'data': {'q': '"golf cart" AND audio'},
  'created': 1697813193},
{
  'search_uid': 5255570,
  'domain': null,
  'actor_key': '3102835279',
  'type': 'google',
  'data': {'q': '"commercial" AND "door" AND ("repair" OR "maintenance" OR "replacement") AND "new York City"'},
  'created': 1697814555}]

The type is 'google'
You will not set the id or created fields.
The default count is 10

"""
