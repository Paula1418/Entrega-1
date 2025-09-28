
import xml.etree.ElementTree as ET  # Permite leer, manipular y recorrer XML en Python.
import csv                          # Facilita escribir y leer archivos en formato CSV/TSV
import re                           # Importa todas las expresiones regulares (regex)


# Abre el archivo en modo lectura
with open("all_karyotypes.xml", "r", encoding="utf-8") as f:
    contenido = f.read() #Leetodo el contenido del archivo xml en una sola cadena de texto


#.lstrip() Elimina espacios en blanco al inicio del archivo (LIMPIEZA)
contenido = contenido.lstrip()

#Verifica si hay más de una declaración <?xml ... ?> o si el contenido no está envuelto en una etiqueta raíz <root>.
if contenido.count("<?xml") > 1 or not contenido.strip().startswith("<root>"):

    contenido = re.sub(r"<\?xml.*?\?>", "", contenido)  #Elimina todas las declaraciones <?xml ... ?> extras del archivo.
    contenido = "<root>" + contenido + "</root>"                    #Envuelve el contenido dentro de un nodo <root> para que se pueda procesar

#Convierte el contenido en un árbol XML que Python puede recorrer
arbol = ET.ElementTree(ET.fromstring(contenido))
raiz = arbol.getroot()

#Defino el arcivo TSV como variables
archivo_tsv = "all_karyotypes.tsv"

with open(archivo_tsv, "w", newline="", encoding="utf-8") as tsvfile: #Abre el archivo TSV en modo escritura. Se usa newline="" para evitar filas en blanco extra
    csvwrite = csv.writer(tsvfile, delimiter="\t")                    #Crea un escritor CSV pero con delimitador de tabulación (\t), convirtiéndolo en TSV
    encabezados = ["id", "description", "name", "biomarker_catogory"] #Seleccion  de los encabezados
    csvwrite.writerow(encabezados)                                    #Escribe los encabezados en la primera fila del archivo TSV.

# Primera iteración la cual busca los caracteres (id, description) de interes dentro de karyotype si no esta deja vacío
    for karyotype in raiz.findall('.//karyotype'):
        id_ = karyotype.find("id").text if karyotype.find("id") is not None else ""
        description = karyotype.find("description").text if karyotype.find("description") is not None else ""

#Segunda Iteración el cual busca los caracteres (name, biomarker_catogory) de interes dentro de condition si no esta se deja vacío
        for condition in karyotype.findall("conditions/condition"):
            name = condition.find("name").text if condition.find("name") is not None else ""
            biomarker_catogory = condition.find("biomarker_catogory").text if condition.find(
                "biomarker_catogory") is not None else ""

#Escribe una fila en el TSV con los datos extraídos de cada karyotype y su condition
            csvwrite.writerow([id_, description, name, biomarker_catogory])

#Indica que el archivo se guardo de manera correcta
print("archivo guardado de manera correcta", archivo_tsv)
