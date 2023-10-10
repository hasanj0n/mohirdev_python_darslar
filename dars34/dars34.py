from urllib import response
# import requests
import json


# wikiurl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Alisher%20Navoiy"

# response = requests.get(wikiurl)

# print(json.dump(response.json(), indent=))

# x= 10
# x_json = json.dumps(x)
# print(type(x_json))


# y= 1.5
# y_json = json.dumps(y)
# print(type(y_json))
# print(y_json)

m= True
m_json = json.dumps(m)
print(type(m_json))
print(m_json)

sonlar = (5,12,54,57,3)
sonlar_json = json.dumps(sonlar)

print(sonlar)
print(sonlar_json)