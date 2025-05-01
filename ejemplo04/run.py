import requests
import json
import csv

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

base_datos = "personas004"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc
    )
    print(f"Insertando {doc['nombre']} | {response.status_code}")






with open('atp_tennis.csv', 'r', encoding='latin1') as fila:

    iteradorDiccionarios = csv.DictReader(fila)
    # Crea un iterador de diccionarios, esta clase convierte cada linea
    # en un diccionario, además usa la primear linea del csv, como las claves de los diccionarios.

    listaColecciones = list(iteradorDiccionarios)
    # Transforma el iterador de diccionarios en una lista de diccionarios

# Nombre de la base de datos
base_datos = "personas005"

# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
datos_finales = {'docs': listaColecciones}
response = requests.post(url, headers=headers, json=datos_finales)

# Mostrar respuesta
print(response.json())
print(response.status_code)