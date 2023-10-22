import AnalisisConahcyt
import AnalisisPDF
import AnalisisTiendas
import AnalisisUniversidades

while True:
    print("Menú de Opciones:")
    print("1. Analisis CONACYTH")
    print("2. Analisis de Universidades")
    print("3. Analisis de archivos PDF")
    print("4. Analisis de tiendas")
    print("5. Salir")
    seleccion = input("Elige una opción: ")

    if seleccion == '1':
        AnalisisConahcyt.analisis_conahcyt()

    elif seleccion == '2':
        AnalisisUniversidades.analisis_universidades()

    elif seleccion == '3':
        AnalisisPDF.analisis_pdf()

    elif seleccion == '4':
        AnalisisTiendas.analisis_tiendas()

    elif seleccion == '5':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elige una opción válida.")
