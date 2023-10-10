import requests
import json
from pprint import pprint as print
app_id = "a4e3f2b5"
app_key = "2b4eb0559ebe0eb69096a42d551f793c"
language = "en-gb"
def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res =r.json()
    if "error" in res.keys():
        return False

    output ={}
    senses = res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]
    definitions =[]
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0].get("audioFile"):
        output["audio"] = res["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"]

    return output

if __name__  == "__main__":
    print(getDefinition("Great Britain"))
    print(getDefinition("asdgdg"))




# print(res)
# print(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"])
# print(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][1]["definitions"])
# print(res["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"])