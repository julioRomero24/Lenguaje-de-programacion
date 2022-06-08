
class main():
    class Ejecucion:
        def __init__(self, arbol, env):
                self.env = env
                resultado = self.r_arbol(arbol)
                if resultado is not None and isinstance(resultado, int):
                    print(resultado)
                if resultado is not None and isinstance(resultado, float):
                    print(resultado)
                if isinstance(resultado, str) and resultado[0] == '"':
                    print(resultado)
        def r_arbol(self, node):
            if isinstance(node, int):
                return node
            if isinstance(node, float):
                return node
            if isinstance(node, str):
                return node
            if node is None:
                return None
            if node[0] == 'numeroEntero':
                return node[1]
            if node[0] == 'numeroFlotante':
                return node[1]
            if node[0] == 'str':
                return node[1]
            if node[0] == 'program':
                if node[1] == None:
                    self.r_arbol(node[2])
                else:
                    self.r_arbol(node[1])
                    self.r_arbol(node[2])
        
            if node[0] == 'suma':
                return self.r_arbol(node[1]) + self.r_arbol(node[2])
            elif node[0] == 'resta':
                return self.r_arbol(node[1]) - self.r_arbol(node[2])
            elif node[0] == 'multiplica':
                return self.r_arbol(node[1]) * self.r_arbol(node[2])
            elif node[0] == 'divide':
                return self.r_arbol(node[1]) / self.r_arbol(node[2])
            
            if node[0] == 'asignacion':
                self.env[node[1]] = self.r_arbol(node[2])
                return node[1]
            
            if node[0] == 'si':
                resultado = self.r_arbol(node[1])
                if resultado:    
                    self.r_arbol(node[2][1])
                return self.r_arbol(node[2][1])
            
            if node[0] == 'sino':
                resultado = self.r_arbol(node[1])
                if resultado:
                    return self.r_arbol(node[2][1])
                return self.r_arbol(node[2][2])
                
            if node[0] == 'condicionIgual':
                return self.r_arbol(node[1]) == self.r_arbol(node[2])

            if node[0] == 'condicionMayor':
                return self.r_arbol(node[1]) > self.r_arbol(node[2])
            
            if node[0] == 'condicionMenor':
                return self.r_arbol(node[1]) < self.r_arbol(node[2])
            
            if node[0] == 'condicionDiferente':
                return self.r_arbol(node[1]) != self.r_arbol(node[2])

            if node[0] == 'variable':
                try:
                    return self.env[node[1]]
                except LookupError:
                    print("Variable indefinida '"+node[1]+"' encontrada")
                    return 0
            if node[0] == 'para':
                if node[1][0] == 'para-s':
                    loop_setup = self.r_arbol(node[1])
                
                    loop_count = self.env[loop_setup[0]]
                    loop_limit = loop_setup[1]
                
                    for i in range(loop_count+1, loop_limit+1):
                        res = self.r_arbol(node[2])
                        if res is not None:
                            return res
                        self.env[loop_setup[0]] = i
                    del self.env[loop_setup[0]]
            if node[0] == 'para-s':
                return (self.r_arbol(node[1]), self.r_arbol(node[2]))

            
            if node[0] == 'mientras':
                resultado = self.r_arbol(node[1])
                aux = resultado
                if resultado:
                    while(aux == resultado):    
                        self.r_arbol(node[2][1])
                        resultado = self.r_arbol(node[1])
                return self.r_arbol(node[2][2])


if __name__ == "__main__":
    lexer = analizadorLexico()
    parser = analizadorParser()
    env = { }
    while True:
        try:
            texto = input('Ingrese expresión > ')
        except EOFError:
            break
        if texto:
            arbol = parser.parse(lexer.tokenize(texto))
            Ejecucion(arbol, env)