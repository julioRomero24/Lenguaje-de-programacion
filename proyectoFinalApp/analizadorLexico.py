from sly import Lexer
from sly import Parser
   

class AnalizadorLexico(Lexer):
    
    # Set of token names.   This is always required
    #colocar los nombre de los tokens
    tokens =    { CARACTER,CADENA, NUMERO_ENTERO, NUMERO_FLOTANTE, 
               CADENA, SI, SINO,PARA,HASTA,AUMENTAEN, LLAVE_IZQ, 
               LLAVE_DER, IGUAL, MIENTRAS, MAYOR, MENOR,
                DIFERENTE}

    
    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_comentario = r'\##.*'
    ignore_nuevalinea = r'\n+'
    #Caracteres únicos que se devuelven tal cual.
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Regular expression rules for tokens
    CARACTER = r'[a-zA-Z_][a-zA-Z0-9_]*'
    CADENA= r'\".*?\"'
    NUMERO_ENTERO = r'\d+'
    NUMERO_FLOTANTE = r'\d+\.\d+'
    CADENA = r'\".*?\"'
    SI = r'si'
    SINO = r'siNO'
    PARA = r'para'
    HASTA= r"hasta"
    AUMENTAEN= r"aumentaEn"
    LLAVE_IZQ=LLAVE_IZQ = r'{'
    LLAVE_DER = r'}'
    IGUAL = r'=='
    MIENTRAS= r"mientras"
    MAYOR= r">"
    MENOR= r"<"
    DIFERENTE= r"!="

    """
        Acciones con un método, y dar la expresión regular asociada con un @_()
    """

    @_(r'\d+.\d+')
    def NUMERO_FLOTANTE(self, token):
        token.value = float(token.value)
        return token

    @_(r'\d+')
    def NUMERO_ENTERO(self, token):
        token.value = int(token.value)
        return token
    
    @_(r'##.*')
    def COMENTARIO(self, token):
        pass
    
    @_(r'\n+')
    def LINEA_NUEVA(self, token):
        self.lineno += len(token.value)

    def error(self, token):
        print('Caracter invalido "%s"' % token.value[0])
        self.index += 1


if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))