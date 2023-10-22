import AnalisisConahcyt
import AnalisisPDF
import AnalisisTiendas

while True:
    print("Menú de Opciones:")
    print("1. Analisis CONACYTH")
    print("2. Opción 2")
    print("3. Analisis PDF")
    print("4. Salir")
    print("5. Salir")
    seleccion = input("Elige una opción: ")

    if seleccion == '1':
        AnalisisConahcyt.analisis_conahcyt()

    elif seleccion == '2':
        print("Has seleccionado la Opción 2")

    elif seleccion == '3':
        AnalisisPDF.analisis_pdf()

    elif seleccion == '4':
        AnalisisTiendas.analisis_tiendas()

    elif seleccion == '5':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elige una opción válida.")
