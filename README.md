# Entrega-1
### Transformación de un archivo XML a formato TSV utilizando PyCharm y Visual Studio

Para realizar la conversión de un archivo **XML** a **TSV (Tab Separated Values)**, se siguieron los siguientes pasos empleando las herramientas **PyCharm** y **Visual Studio**:

1. **Preparación del entorno de trabajo**

   * Se instaló y configuró el intérprete de **Python** en PyCharm y Visual Studio.
   * Se creó un proyecto destinado a la manipulación y conversión de archivos en formato XML.

2. **Lectura del archivo XML**

   * Se utilizó la librería estándar `xml.etree.ElementTree` de Python para abrir y recorrer la estructura del archivo XML.
   * El archivo completo se cargó como texto para permitir tanto el procesamiento estructurado como la aplicación de expresiones regulares.

3. **Extracción de información relevante**

   * Se implementaron **expresiones regulares** y funciones de Python para identificar y extraer etiquetas específicas del archivo XML, tales como:

     * `<id>` para los identificadores.
     * `<description>` para las descripciones.
     * `<name>` para los nombres de condiciones.
     * `<biomarker_category>` para las categorías de biomarcadores.

4. **Transformación de los datos**

   * Una vez extraída la información, se organizó en forma de tabla con valores separados por tabulación.
   * Este formato **TSV** facilita la lectura en editores de texto, hojas de cálculo y herramientas de análisis de datos.

5. **Exportación a TSV**

   * Los datos procesados fueron escritos en un nuevo archivo con extensión `.tsv`.
   * Para ello, se utilizó la librería estándar `csv` de Python con el parámetro `delimiter='\t'` para garantizar que los campos quedaran separados por tabulaciones.

6. **Verificación del resultado**

   * Se abrió el archivo `.tsv` en Visual Studio y en PyCharm para comprobar la correcta alineación de las columnas.
   * Finalmente, se validó que la transformación preservara toda la información contenida en el archivo XML original.

<p align="center">
  <img src="https://resources.jetbrains.com/storage/products/pycharm/img/meta/pycharm_logo_300x300.png" alt="Logo PyCharm" width="150px" height="150px" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://visualstudio.microsoft.com/wp-content/uploads/2021/10/Product-Icon.svg" alt="Logo Visual Studio" width="150px" height="150px" />
</p>


