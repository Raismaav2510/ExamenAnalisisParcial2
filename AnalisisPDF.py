import PyPDF2
import re
import os
import glob
import sys


expresiones = [
    (r'^[ \t]+', ''),
    (r'\n\n+', '\n\n'),
]


def analisis_pdf():
    archivos_pdf = obtener_archivos_en_carpeta('PDF')
    print("\n")
    palabra_a_buscar = input("Ingrese la palabra que desea buscar en los archivos PDF: ")

    with open('busqueda_PDF.txt', 'w') as archivo:
        sys.stdout = archivo

        for archivo_pdf in archivos_pdf:
            print("\nBuscando en el archivo:", archivo_pdf)
            buscar_y_mostrar_paginas_con_palabra_en_pdf(archivo_pdf, palabra_a_buscar)

        print("Búsqueda completada")

    sys.stdout = sys.__stdout__
    with open('busqueda_PDF.txt', 'r') as archivo:
        for linea in archivo:
            print(linea, end='')


# Función para buscar una palabra en el texto de una página
def buscar_palabra_en_pagina(pagina, palabra):
    texto = pagina.extractText()
    return re.search(palabra, texto, re.IGNORECASE) is not None


# Función para buscar y mostrar páginas con una palabra en un PDF
def buscar_y_mostrar_paginas_con_palabra_en_pdf(pdf_path, palabra):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            for expresion, sustitucion in expresiones:
                page_text = re.sub(expresion, sustitucion, page_text, flags=re.MULTILINE)

            if buscar_palabra_en_pagina(page, palabra):
                print(f"La palabra '{palabra}' se encuentra en la página {page_num + 1} del archivo {pdf_path}")


def obtener_archivos_en_carpeta(carpeta, extension='.pdf'):
    archivos = glob.glob(os.path.join(carpeta, f"*{extension}"))
    return archivos
