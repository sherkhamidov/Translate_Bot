import requests
from pprint import pprint as print

API_KEY =  '94888e9f3172cc3cd00a3f10'
currency='USD'
url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
print(response.status_code)
print(response.json())

jsondata = response.json()
kurs = jsondata['conversion_rate']
print(f"Bugungi kurs: 1$ = {kurs} so'm")