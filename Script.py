class Automata:
    def __init__(self):
        
        self.estados = {'s0', 's1', 's2'}
        
        
        self.simbolos = {'a', 'b', 'c'}
        
        
        self.transiciones = {
            's0': {'a': 's1', 'b': 's0','c':''},
            's1': {'a': 's1', 'b': 's2','c':'s1'},
            's2': {'a': 's1', 'b': 's0','c':'s1'},
        }
        
        
        self.estado_actual = 's0'
    
    def procesar_cadena(self, cadena):
        for simbolo in cadena:
            if simbolo not in self.simbolos:
                return "Cadena rechazada"
            self.estado_actual = self.transiciones[self.estado_actual][simbolo]
        
        if self.estado_actual == 's1':
            return "Cadena aceptada"
        else:
            return "Cadena rechazada"


