from Script import Automata  

automata = Automata()  

nombre_archivo = "File_out.txt"
try:
    with open(nombre_archivo, "r") as archivo:
        numero_renglon = 1
        for linea in archivo:
            # Elimina espacios en blanco y caracteres de nueva línea
            linea = linea.strip()
            resultado = automata.procesar_cadena(linea, numero_renglon)
            print(linea)
            print(resultado)
            print('-----------------------')
            numero_renglon += 1
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except Exception as e:
    print(f"Error al procesar el archivo: {str(e)}")
