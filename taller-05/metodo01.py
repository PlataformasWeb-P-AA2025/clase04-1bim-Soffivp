import requests
import json

# Cargar datos desde archivo
with open('atp_tennis.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)


lista = []

for d in data['docs']:
    lista.append(d)

base_datos = "personas005"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
data = {'docs': lista}
response = requests.post(url, headers=headers, json=data)

# Mostrar respuesta
print(response.status_code)
print(response.json())


