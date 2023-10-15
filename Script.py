class Automata:
    def __init__(self):
        self.estados = {'s1', 's8', 's9', 's10', 's11', 's12'}
        self.simbolos = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.punto = '.'
        self.negativo = '-'
        
        self.transiciones = {
            's1': {**{symbol: 's8' for symbol in self.simbolos}, self.negativo: 's10'},
            's8': {**{symbol: 's8' for symbol in self.simbolos}, self.punto: 's9'},
            's9': {**{symbol: 's9' for symbol in self.simbolos}},
            's10': {**{symbol: 's11' for symbol in self.simbolos}},
            's11': {**{symbol: 's11' for symbol in self.simbolos}, self.punto: 's12'},
            's12': {**{symbol: 's12' for symbol in self.simbolos}},
        }
        
        self.estado_actual = 's1'
    
    def procesar_cadena(self, cadena):
        for simbolo in cadena:
            if simbolo not in self.simbolos and simbolo != self.punto and simbolo != self.negativo:
                return "Cadena rechazada"
            self.estado_actual = self.transiciones[self.estado_actual][simbolo]
        
        if self.estado_actual in {'s8', 's9', 's11', 's12'}:
            if self.estado_actual == 's8':
                self.estado_actual = 's1'
                return 'Numero entero'
            elif self.estado_actual == 's9':
                self.estado_actual = 's1'
                return 'Decimal'
            elif self.estado_actual == 's11':
                self.estado_actual = 's1'
                return 'Negativo Entero'
            elif self.estado_actual == 's12':
                self.estado_actual = 's1'
                return 'Negativo Decimal'
            self.estado_actual = 's1'
        else:
            return "Cadena rechazada"


