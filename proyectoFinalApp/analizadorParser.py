from email.parser import Parser
from analizadorLexico import AnalizadorLexico
from sly import Parser

from proyectoFinalApp import analizadorLexico
class AnalizadorParser(Parser):
    #Obtenemos la lista de Tokens del Analizador Léxico.
    analizadorLex=analizadorLexico()
    tokens = analizadorLex.tokens
    #prioridad, para cuando Cuando se encuentran conflictos de desplazamiento/reducción
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )    

    # Grammar rules and actions
    @_('')
    def declaracion(self, parser):
        pass

    @_('expresion')
    def declaracion(self, parser):
        return (parser.expresion)

    @_('expresion "+" expresion')
    def expresion(self, parser):
        return ('suma', parser.expresion0, parser.expresion1)
    
    @_('expresion "-" expresion')
    def expresion(self, parser):
        return ('resta', parser.expresion0, parser.expresion1)
    
    @_('expresion "*" expresion')
    def expresion(self, parser):
        return ('multiplica', parser.expresion0, parser.expresion1)

    @_('expresion "/" expresion')
    def expresion(self, parser):
        return ('divide', parser.expresion0, parser.expresion1)

    @_('"-" expresion %prec UMINUS')
    def expresion(self, parser):
        return parser.expresion
    
    @_('asignacion')
    def declaracion(self, parser):
        return parser.asignacion
    
    @_('CARACTER "=" expresion')
    def asignacion(self, parser):
        return ('asignacion', parser.CARACTER, parser.expresion)
    
    @_('CARACTER "=" CADENA')
    def asignacion(self, parser):
        return ('asignacion', parser.CARACTER, parser.CADENA)
    
    @_('CARACTER')
    def expresion(self, parser):
        return ('variable', parser.CARACTER)

    @_('NUMERO_ENTERO')
    def expresion(self, parser):
        return ('numeroEntero', parser.NUMERO_ENTERO)
    
    @_('NUMERO_FLOTANTE')
    def expresion(self, parser):
        return ('numeroFlotante', parser.NUMERO_FLOTANTE)

    @_('expresion IGUAL expresion')
    def condicion(self, parser):
        return ('condicionIgual', parser.expresion0, parser.expresion1)
    
    @_('expresion MAYOR expresion')
    def condicion(self, parser):
        return ('condicionMayor', parser.expresion0, parser.expresion1)
    
    @_('expresion MENOR expresion')
    def condicion(self, parser):
        return ('condicionMenor', parser.expresion0, parser.expresion1)
    
    @_('expresion DIFERENTE expresion')
    def condicion(self, parser):
        return ('condicionDiferente', parser.expresion0, parser.expresion1)

    @_('SI condicion LLAVE_IZQ declaracion LLAVE_DER')
    def declaracion(self, parser):
        return ('si', parser.condicion, ('branch', parser.declaracion, parser.declaracion))
    
    @_('SI condicion LLAVE_IZQ declaracion LLAVE_DER SINO LLAVE_IZQ declaracion LLAVE_DER')
    def declaracion(self, parser):
        return ('sino', parser.condicion, ('branch', parser.declaracion0, parser.declaracion1))

    @_('PARA asignacion EN expresion LLAVE_IZQ declaracion LLAVE_DER')
    def declaracion(self, parser):
        return ('para', ('para-s', parser.asignacion, parser.expresion), parser.declaracion)

    @_('MIENTRAS condicion LLAVE_IZQ declaracion LLAVE_DER ')
    def declaracion(self, parser):
        return ('mientras', parser.condicion, ('branch', parser.declaracion, parser.declaracion))   
        
