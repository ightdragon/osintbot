import requests
import os
import pprint
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("API_KEY")
url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": "Bearer " + api_key ,
    "Content-Type": "application/json"
}

content_user = input()


payload = {
    "model":"sonar-pro",
    "messages":[
        {"role":"system",
         "content":
         "You are Elliot Anderson from Mr. Robot. You will be leading an OSINT investigation."
         "Rules:"
         ". You will not display any catchphrases from the show 'Mr. Robot'."
         ". Display the result in a cherry-tree like structure."
         ". You will provide your insigt on the basic subject info, possible connections to other accounts and employment."
         ". Your answers will be final."
         ". Your answers will be specific to OSINT."
         ". You will provide citations and links to the profiles."
          },
        {"role":"user",
         "content":content_user}
    ],
    "max_tokens":700,
    "top_p":0.1,
    "return_images": True,
    "web_search_options":{
      "search_context_size": "medium"
    },
    "search_domain_filter":[
        "instagram.com",
        "facebook.com",
        "x.com"
    ]
}

print("Loading...")
response = requests.post(url, headers=headers, json=payload).json()





finalResponse = response["choices"][0]["message"]["content"]


pprint.pprint(finalResponse)
print("***************************")
pprint.pprint(response["citations"])
print("***************************")
pprint.pprint(response["images"])