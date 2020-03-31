import csv
from pathlib import Path
import requests
from slugify import slugify


URL = "https://preciosmaximos.argentina.gob.ar/api/products"
params = {"pag": 1, "regs": 3000}

provs = [
    "CABA",
    "Santiago del Estero",
    "Buenos Aires",
    "Jujuy",
    "Salta",
    "Tucumán",
    "Catamarca",
    "La Rioja",
    "San Juan",
    "La Pampa",
    "Formosa",
    "Chaco",
    "Misiones",
    "Corrientes",
    "Entre Ríos",
    "Santa Fe",
    "Córdoba",
    "San Luis",
    "Mendoza",
    "Neuquén",
    "Río Negro",
    "Chubut",
    "Santa Cruz",
    "Tierra del Fuego",
]

for prov in provs:
    print(f"Bajando {prov}")
    params["Provincia"] = prov
    response = requests.get(URL, params=params)
    slug = slugify(prov)

    Path(f"{slug}.json").write_text(response.text)

    rows = response.json()["result"]

    fields = rows[0].keys()

    writer = csv.DictWriter(Path(f"{slug}.csv").open("w"), fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
