from Script import Automata  

automata = Automata()  


cadena = input('Ingresa cadena: ')
resultado = automata.procesar_cadena(cadena)
print('-----------------------')
print(resultado)