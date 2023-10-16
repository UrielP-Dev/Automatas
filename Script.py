class Automata:
    def __init__(self):
        self.estados = {'s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18'}
        self.separadores = {':', ';', '+', '*', '/', '<', '>', '[', ']', '!', '(', ')', ' ', '='}
        self.simbolos = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.letras_minusculas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_'}
        self.letras_mayusculas = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','_'}
        self.variable = {"int", "float", "bool", "void", "string", "char"}
        self.palabras = {"for", "print", "static", "if", "Public", "new", "private", "else", "import", "return", "do", "def", "protec", "switch"}        
        self.lista_de_palabras = list(self.palabras)
        self.comillas = '"'
        self.aroba = '@' 
        self.punto = '.'
        self.negativo = '-'
        
        
        self.transiciones = {
            's1': {**{symbol: 's8' for symbol in self.simbolos}, self.negativo: 's10',self.aroba: 's13',self.comillas: 's15',**{symbol: 's17' for symbol in self.letras_mayusculas} ,**{symbol: 's18' for symbol in self.letras_minusculas}},
            's8': {**{symbol: 's8' for symbol in self.simbolos}, self.punto: 's9'},
            's9': {**{symbol: 's9' for symbol in self.simbolos}},
            's10': {**{symbol: 's11' for symbol in self.simbolos}},
            's11': {**{symbol: 's11' for symbol in self.simbolos}, self.punto: 's12'},
            's12': {**{symbol: 's12' for symbol in self.simbolos}},
            's13': {**{symbol: 's13' for symbol in self.simbolos},**{symbol: 's13' for symbol in self.letras_mayusculas} ,**{symbol: 's13' for symbol in self.letras_minusculas} ,self.aroba: 's14'},
            's14': {},
            's15': {**{symbol: 's15' for symbol in self.simbolos}, **{symbol: 's15' for symbol in self.letras_mayusculas} ,**{symbol: 's15' for symbol in self.letras_minusculas} ,self.comillas: 's16'},
            's16': {},
            's17': {**{symbol: 's17' for symbol in self.simbolos}, **{symbol: 's17' for symbol in self.letras_mayusculas}},
            's18': {**{symbol: 's18' for symbol in self.simbolos}, **{symbol: 's18' for symbol in self.letras_minusculas}},
        }
        
        self.estado_actual = 's1'
    
    def procesar_cadena(self, cadena, renglon):
        
        if cadena in self.palabras:
            asignacion = f"{cadena}, Palabra Reservada, token  {self.lista_de_palabras.index(cadena)}, renglon: {renglon}"
            return asignacion
        elif cadena in self.variable:
            asignacion = f"{cadena}, Tipo de variable, renglon: {renglon}"
            return asignacion
        elif cadena in self.separadores:
            asignacion = f"{cadena}, Separador, renglon: {renglon}"
            return asignacion
            
        else:
            try:
                self.estado_actual = 's1'
                for simbolo in cadena:
                    if simbolo not in self.simbolos and simbolo != self.punto and simbolo != self.negativo and simbolo != self.comillas and simbolo != self.aroba and simbolo not in self.letras_minusculas and simbolo not in self.letras_mayusculas:
                        return "Cadena rechazada"
                    self.estado_actual = self.transiciones[self.estado_actual][simbolo]
                
                if self.estado_actual in {'s8', 's9', 's11', 's12','s14','s16','s17','s18'}:
                    if self.estado_actual == 's8':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Numero entero, Token 8, renglon: {renglon}"
                        return asignacion
                    
                    elif self.estado_actual == 's9':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Numero decimal, Token 10, renglon: {renglon}"
                        return asignacion
                    
                    elif self.estado_actual == 's11':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Negativo entero, Token 12, renglon: {renglon}"
                        return asignacion
                    
                    elif self.estado_actual == 's12':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Negativo decimal, Token 14, renglon: {renglon}"
                        return asignacion
                    
                    elif self.estado_actual == 's14':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Comentario, Token 5, renglon: {renglon}"
                        return asignacion
                        
                    elif self.estado_actual == 's16':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Cadena, Token 3 renglon: {renglon}"
                        return asignacion
                        
                    elif self.estado_actual == 's17':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Clase, Token 6 renglon: {renglon}"
                        return asignacion
                        
                    elif self.estado_actual == 's18':
                        self.estado_actual = 's1'
                        asignacion = f"{cadena}, Variable, Token 7 renglon: {renglon}"
                        return asignacion
                    self.estado_actual = 's1'
                else:
                    self.estado_actual = 's1'
                    return "Cadena rechazada"
            except Exception as e:
                return f"Error al procesar la cadena: {str(e)}, Renglon: {renglon}"    


