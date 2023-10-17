class ReadFile:
    def open_file(self):
        with open('File.txt', 'r') as archivo:
            self.text = archivo.read()
        
    def check_text(self):
        with open('File_out.txt', 'w') as Text_out:
            previous_character = ''  # Almacena el caracter anterior para verificar líneas en blanco
            special_chars = {'@', '"'}
            within_special = False  # Indica si estamos dentro de un carácter especial
            current_special_char = None  # Almacena el carácter especial actual
            for caracter in self.text:
                if caracter in special_chars:
                    if within_special:
                        within_special = False
                        if caracter == current_special_char:
                            current_special_char = None
                    else:
                        within_special = True
                        current_special_char = caracter

                if caracter in {':', ';', '+', '*', '/', '<', '>', '[', ']', '!', '(', ')', ' '}:
                    if previous_character != '\n' and not within_special:  # Evitar escribir líneas en blanco consecutivas
                        Text_out.write('\n')
                    Text_out.write(caracter)
                    if caracter == '(':
                        Text_out.write('\n')  # Add a space after an opening parenthesis
                else:
                    Text_out.write(caracter)
                previous_character = caracter




    
    def remove_blank_lines_from_output(self):
        # Leer el archivo File_out.txt y eliminar líneas en blanco
        with open('File_out.txt', 'r') as file:
            lines = file.readlines()
        
        lines = [line for line in lines if line.strip()]  # Filtrar líneas en blanco

        # Sobrescribir File_out.txt con las líneas restantes
        with open('File_out.txt', 'w') as file:
            file.writelines(lines)       