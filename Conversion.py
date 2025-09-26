
import xml.etree.ElementTree as ET
import csv

with open("all_karyotypes.xml", "r", encoding="utf-8") as f:
    contenido = f.read()

contenido = contenido.lstrip()
"""re.sub(patrón, reemplazo, texto)"""
"""Busca todas las coincidencias de patrón dentro 
    de texto y las reemplaza por reemplazo."""
if contenido.count("<?xml") > 1 or not contenido.strip().startswith("<root>"):
    import re

    contenido = re.sub(r"<\?xml.*?\?>", "", contenido)
    contenido = "<root>" + contenido + "</root>"

archivo_tsv = "all_karyotypes.tsv"

arbol = ET.ElementTree(ET.fromstring(contenido))
raiz = arbol.getroot()

with open(archivo_tsv, "w", newline="", encoding="utf-8") as tsvfile:
    csvwrite = csv.writer(tsvfile, delimiter="\t")
    encabezados = ["id", "description", "name", "biomarker_catogory"]
    csvwrite.writerow(encabezados)

    for karyotype in raiz.findall('.//karyotype'):
        id_ = karyotype.find("id").text if karyotype.find("id") is not None else ""
        description = karyotype.find("description").text if karyotype.find("description") is not None else ""

        for condition in karyotype.findall("conditions/condition"):
            name = condition.find("name").text if condition.find("name") is not None else ""
            biomarker_catogory = condition.find("biomarker_catogory").text if condition.find(
                "biomarker_catogory") is not None else ""

            csvwrite.writerow([id_, description, name, biomarker_catogory])

print("archivo guardado de manera correcta", archivo_tsv)