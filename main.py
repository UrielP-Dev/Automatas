from Script import Automata  

automata = Automata()  

while (True):
    cadena = input('Ingresa cadena: ')
    resultado = automata.procesar_cadena(cadena,1)
    print('-----------------------')
    print(resultado)
