import re
from urllib import request
from bs4 import BeautifulSoup

urls = [
    ('https://es.anuto.app/', ['h5', 'div'], ['listing-title dont-break-out mb-1 p-2', 'label price ng-star-inserted']),
    ('https://www.ebay.es/?ff3=4&pub=5575132557&toolid=10001&campid=5338326437&customid=&mkevt=1&mkcid=1&mkrid=1185'
     '-53479-19255-0&ufes_redirect=true',
     ['h3', 'div'],
     ['vlp-merch-item-title vlp-merch-item-title-dweb vlp-merch-item-title-margin', 'vlp-merch-price']),
    ('https://www.poneranuncios.com/inmuebles/', ['etiquetas', 'aqui'], ['clases', 'aqui'])
]


def analisis_tiendas():
    for url, etiquetas, clases in urls:
        resultados = obtener_contenido_web(url, etiquetas, clases)
        limpiar_y_mostrar_resultados(resultados)

def obtener_contenido_web(url, etiquetas, clases):
    hdr = {
        'User-Agent': 'Wget/1.14 (linux-gnu)',
        'Accept': '*/*'
    }
    req = request.Request(url, headers=hdr)
    html = request.urlopen(req).read().decode('utf8')
    data = BeautifulSoup(html, 'html.parser')
    resultados = data.find_all(etiquetas, {'class': clases})
    return resultados


def limpiar_y_mostrar_resultados(resultados):
    print("\n")
    for resultado in resultados:
        texto = resultado.text
        texto_limpio = re.sub(r'^[ \t]+', '', texto, flags=re.MULTILINE)
        texto_limpio = re.sub(r'\n\s*\n', '', texto_limpio)
        print(texto_limpio)
