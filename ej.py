import re

# Abrir el archivo XML
with open("all_karyotypes.xml", "r", encoding="utf-8") as f:
    contenido = f.read()

# --- Ejemplo A: Buscar IDs numéricos y su Cariotipo ---
pattern_id = r"<id>(\d+)</id>"                        #Busca los numero ID denntro de las etiquetas
pattern_desc = r"t\(\d+;\d+\)\([pq]\d+;[pq]\d+\)"     #Busca las translocaciones cromosómicas en formato t(...).

ids = re.findall(pattern_id, contenido)
desc = re.findall(pattern_desc, contenido)

print("\n--- IDs con sus descripciones ---")
for i in range(min(10, len(ids), len(desc))):
    print(f"ID: {ids[i]} | Descripción: {desc[i].strip()}")


# --- Ejemplo B: Buscar descripciones que contengan "leukemia" (ignore case) ---
patternB = r"(?i)<description>(.*?)</description>"          #Busca todo el contenido entre etiquetas <description> ... </description>
desc_leukemia = re.findall(patternB, contenido, re.DOTALL)
print("\n--- Descripciones con 'leukemia' (máx 3) ---")
count = 0
for d in desc_leukemia:
    if "leukemia" in d.lower():  # filtra solo si contiene la palabra
        print(d.strip())
        count += 1
        if count == 3:
            break


# --- Ejemplo C: Buscar nombres de condiciones disitintas ---
patternC = r"<name>(.*?)</name>"                  # Busca los nombres de las condiciones dentro de las etiquteas de name
nombres = re.findall(patternC, contenido)         #busca todas las coincidencias de ese patrón(definido en patternC) dentro del archivo.
#----Elimina los dulpicados
nombres_unicos = set([n.strip() for n in nombres])

#Imprime las cantidad de condicones distintas que hay
print(f"Cantidad de condiciones distintas: {len(nombres_unicos)}")

print("\n--- Nombres de condiciones (máx 10, sin repetir) ---")
for n in list(nombres_unicos)[:10]:
    print(n)
