from urllib import request
from bs4 import BeautifulSoup
import sys
import re


def analisis_conahcyt():
    hdr = {
        'User-Agent': 'Wget/1,14 (linux-gnu)',
        'Accept': '*/*'
    }

    link_conahcyt = 'https://centrosconahcyt.net/oferta-academica/'
    req = request.Request(link_conahcyt, headers=hdr)
    html_conahcyt = request.urlopen(req).read().decode('utf8')

    data = BeautifulSoup(html_conahcyt, 'html.parser')
    # print(data.prettify())

    # oferta_academica = data.find_all('div', {'class': 'col-md-3 col-sm-12 blog-masonry-item m-b-lg'})
    oferta_html = data.find_all('div', {'class': 'col-md-3 col-sm-12 blog-masonry-item Licenciatura m-b-lg'})
    oferta_html += data.find_all('div', {'class': 'col-md-3 col-sm-12 blog-masonry-item Especialidad m-b-lg'})
    oferta_html += data.find_all('div', {'class': 'col-md-3 col-sm-12 blog-masonry-item Maestria m-b-lg'})
    oferta_html += data.find_all('div', {'class': 'col-md-3 col-sm-12 blog-masonry-item Doctorado m-b-lg'})

    # Filtrado de datos
    ofertas = []
    for oferta in oferta_html:
        oferta_data = oferta.find_all('span', {'class': 'sub alt-font'})
        oferta_data += oferta.find_all('a')
        # print(oferta_data)

        # Limpiado de datos
        for index in range(0, len(oferta_data)):
            oferta_data[index] = oferta_data[index].text
            oferta_data[index] = re.sub(r'-', ' ', oferta_data[index])
        # print(oferta_data)
        ofertas.append(oferta_data)

    # Oferta academica de CONAHCYT
    with open('oferta_conahcyt.txt', 'w') as archivo:
        sys.stdout = archivo

        print(f'\nOferta conahcyt\n')
        for oferta in ofertas:
            print(f'{oferta[2]}')

    # Oferta por sedes
    with open('oferta_por_sedes.txt', 'w') as archivo:
        sys.stdout = archivo

        print(f'\nOferta por coordinaciones y sedes\n')
        sedes = {}
        for sede in ofertas:
            sedes[sede[0]] = []

        for oferta in ofertas:
            sedes[oferta[0]].append(oferta[2])

        coordinaciones = {}
        for coordinacion in ofertas:
            coordinaciones[coordinacion[1]] = set()

        for oferta in ofertas:
            coordinaciones[oferta[1]].add(oferta[0])

        for coordinacion in coordinaciones:
            print(f'{coordinacion}')
            for sede in coordinaciones[coordinacion]:
                print(f'\t{sede}')
                for oferta in sedes[sede]:
                    print(f'\t\t{oferta}')
                print()

    sys.stdout = sys.__stdout__
    with open('oferta_conahcyt.txt', 'r') as archivo:
        for linea in archivo:
            print(linea, end='')

    with open('oferta_por_sedes.txt', 'r') as archivo:
        for linea in archivo:
            print(linea, end='')
