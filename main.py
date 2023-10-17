from Script import Automata
from Read import ReadFile

automata = Automata()

lector = ReadFile()
lector.open_file()
lector.check_text()
lector.remove_blank_lines_from_output()

nombre_archivo_entrada = "File_out.txt"
nombre_archivo_salida = "Analizador_Léxico.txt"

try:
    with open(nombre_archivo_entrada, "r") as archivo_entrada, open(nombre_archivo_salida, "w") as archivo_salida:
        numero_renglon = 1
        for linea in archivo_entrada:
            # Elimina espacios en blanco y caracteres de nueva línea
            linea = linea.strip()
            resultado = automata.procesar_cadena(linea.replace(" ", ""), numero_renglon)
            archivo_salida.write(f"Linea {numero_renglon}: {linea}\n")
            archivo_salida.write(f"Resultado: {resultado}\n")
            archivo_salida.write('-----------------------\n')
            if linea == ";": numero_renglon += 1
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo_entrada}' no se encontró.")
except Exception as e:
    print(f"Error al procesar el archivo: {str(e)}")

print("Procesamiento completado. Resultados guardados en 'Analizador_Léxico.txt'.")
