import requests

API_KEY ="21b4143922fb0e871261a066"
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS'


response = requests.get(url)
kurs =response.json()["conversion_rate"]
print(f"Bugungi kurs: 1 AQSH dollari ={kurs} so'm")
