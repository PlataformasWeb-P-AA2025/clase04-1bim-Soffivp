import requests
import json

with open('atp_tennis.json', 'r') as f:
    data = json.load(f)

lista = []

for d in data['docs']:
    lista.append(d)

base_datos = "personas006"

url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

for doc in lista:
    response = requests.post(
        url,
        json=doc
    )