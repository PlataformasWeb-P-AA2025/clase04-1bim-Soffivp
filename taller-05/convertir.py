import csv
import json

# Abre el archivo CSV con codificación 'latin1'
with open('atp_tennis.csv', newline='', encoding='latin1') as csvF:
    reader = csv.DictReader(csvF)  # Lee el CSV como diccionario (cada fila será un dict)
    data = list(reader)  # Convierte todas las filas en una lista

# Envuelve los datos en un diccionario con clave 'docs'
bulk_data = {"docs": data}

# Guarda los datos en formato JSON, con codificación UTF-8 y formato legible (indentado)
with open('atp_tennis.json', 'w', encoding='utf-8') as jF:
    json.dump(bulk_data, jF, indent=4, ensure_ascii=False)
