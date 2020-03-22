from ply import lex


class Lexer:

    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER',
        'FLOAT', 'BOOLEAN', 'VOID', 'TRUE', 'FALSE', 'PRINT',
        'RETURN', 'MAIN', 'IF', 'ELSE', 'ELIF', 'WHILE', 'FOR',
        'AND', 'OR', 'NOT', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB', 'LRB',
        'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COMMA', 'SYNTAXERROR'
    ]

    reserved = {
        'int': 'INT',
        'float': 'FLOAT',
        'boolean': 'BOOLEAN',
        'void': 'VOID',
        'true': 'TRUE',
        'false': 'FALSE',
        'print': 'PRINT',
        'return': 'RETURN',
        'main': 'MAIN',
        'if': 'IF',
        'else': 'ELSE',
        'elif': 'ELIF',
        'while': 'WHILE',
        'for': 'FOR'
    }

    # COLONS
    t_SEMICOLON = r';'
    t_COMMA = r','

    # BRACKETS
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    # OPERATOR
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_NOT = r'\!'
    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'/'
    t_MOD = r'%'
    t_GT = r'\>'
    t_GE = r'>='
    t_LT = r'\<'
    t_LE = r'<='
    t_EQ = r'='
    t_NE = r'!='
    # KW
    t_INTEGER = r'int'
    t_FLOAT = r'float'
    t_BOOLEAN = r'boolean'
    t_VOID = r'void'
    t_TRUE = r'true'
    t_FALSE = r'false'
    t_PRINT = r'print'
    t_RETURN = r'return'
    t_MAIN = r'main'
    t_IF = r'if'
    t_ELSE = r'else'
    t_ELIF = r'elif'
    t_WHILE = r'while'
    t_FOR = r'for'


    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value in Lexer.reserved:
            t.type = Lexer.reserved[t.value]
        return t

    def t_INTEGERNUMBER(self, t):
        # r'([-|+]?(\d+))'                   # error(3+2)
        # r'(^[-|+]?(\d+)) | (\d+)'          # error(3+(-2))
        r'[+|-]?(?<!\.)\b[0-9]+\b(?!\.[0-9])' # error(3+2)
        # (? < ![-.])  # Assert that the previous character isn't a minus sign or a dot.
        # \b  # Anchor the match to the start of a number.
        # [0 - 9] +  # Match a number.
        # \b  # Anchor the match to the end of the number.
        # (?!\.[0-9])  # Assert that no decimal part follows.
        t.value = int(t.value)
        return t
    def t_FLOATNUMBER(self, t):
        # r'[+|-]?\d*(\.)\d+'
        # r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
        r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
        t.value = float(t.value)
        return t


    # def t_SYNTAXERROR(self, t):
    #     r'19a'
    #     t.type = ''
    #     return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_error(self, t):
        print('ERROR')
        t.lexer.skip(1)
        # raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer