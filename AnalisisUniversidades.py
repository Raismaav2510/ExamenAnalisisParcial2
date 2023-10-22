import re
from urllib import request
from bs4 import BeautifulSoup

hdr = {
    'User-Agent': 'Wget/1.14 (linux-gnu)',
    'Accept': '*/*'
}

# URLs de las universidades
universidades = [
    "https://mextudia.com/universidades/universidad-de-guanajuato/#%3cstrong%3ecarreras+de+la+universidad+de+guanajuato%3c%2fstrong%3e",
    "https://mextudia.com/universidades/buap/#carreras+de+la+buap",
    "https://mextudia.com/universidades/unam/#carreras+de+la+unam",
    "https://mextudia.com/universidades/vasco-de-quiroga/#carreras+de-la-universidad-vasco-de-quiroga",
    "https://mextudia.com/universidades/unid/#carreras+de-la-universidad-interamericana-para-el-desarrollo",
    "https://mextudia.com/universidades/tec-de-monterrey/#itesm+-+tec+de-monterrey+carreras"
]


def analisis_universidades():
    for url in universidades:
        req = request.Request(url, headers=hdr)
        html = request.urlopen(req).read().decode('utf8')
        data = BeautifulSoup(html, 'html.parser')
        print(data.prettify())
        etiquetas_validadas = obtener_etiquetas_validas(data)
        for etiqueta in etiquetas_validadas:
            texto_sin_etiquetas = etiqueta.text
            print(texto_sin_etiquetas)

def obtener_etiquetas_validas(data):
    etiquetas_validas = []
    for h4_tag in data.find_all('h4'):
        strong_tags = h4_tag.find_all('strong')
        if strong_tags:
            etiquetas_validas.extend(strong_tags)
    return etiquetas_validas
