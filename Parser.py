from ply import yacc
from Lexer import Lexer

class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        """
        program : declist MAIN LRB RRB block
        """
        print("""
        program : declist MAIN LRB RRB block
        """)

    def p_declist(self, p):
        """
        declist : dec
                | declist dec
                |
        """
        print("""
        declist : dec 
                | declist dec 
                |  
        """)

    def p_dec(self, p):
        """
        dec : vardec
            | funcdec
        """
        print("""
        dec : vardec
            | funcdec
        """)

    def p_type(self, p):
        """
        type : INTEGER
             | FLOAT
             | BOOLEAN
        """
        print("""
        type : INTEGER
             | FLOAT
             | BOOLEAN
        """)

    def p_iddec(self, p):
        """
        iddec : ID
              | ID LSB exp RSB
              | ID ASSIGN exp
        """
        print("""
        iddec : ID
              | ID LSB exp RSB
              | ID ASSIGN exp
         """)

    def p_idlist(self, p):
        """
        idlist : iddec
               | idlist COMMA iddec
        """
        print("""
        idlist : iddec
               | idlist COMMA iddec
         """)

    def p_vardec(self, p):
        """
        vardec : type idlist SEMICOLON
        """
        print("""
        vardec : type idlist SEMICOLON

         """)

    def p_funcdec(self, p):
        """
        funcdec : type ID LRB paramdecs RRB block
                | VOID ID LRB paramdecs RRB block
        """
        print("""
        funcdec : type ID LRB paramdecs RRB block 
                | VOID ID LRB paramdecs RRB block
         """)

    def p_paramdecs(self, p):
        """
        paramdecs : paramdecslist
                  |
        """
        print("""
        paramdecs : paramdecslist
                  |
         """)

    def p_paramdecslist(self, p):
        """
        paramdecslist : paramdec
                      | paramdecslist COMMA paramdec
        """
        print("""
        paramdecslist : paramdec
                      | paramdecslist COMMA paramdec
         """)

    def p_paramdec(self, p):
        """
        paramdec : type ID
                 | type ID LSB RSB
        """
        print("""
        paramdec : type ID
                 | type ID LSB RSB
         """)

    def p_varlist(self, p):
        """
        varlist : vardec
                | varlist vardec
                |
        """
        print("""
        varlist : vardec 
                | varlist vardec 
                | 
         """)

    def p_block(self, p):
        """
        block : LCB varlist stmtlist RCB
        """
        print("""
        block : LCB varlist stmtlist RCB
         """)

    def p_stmtlist(self, p):
        """
        stmtlist : stmt
                 | stmtlist stmt
                 |
        """
        print("""
         """)

    def p_lvalue(self, p):
        """
        lvalue : ID
               | ID LSB exp RSB
        """
        print("""
        lvalue : ID 
               | ID LSB exp RSB
         """)

    def p_stmt(self, p):
        """
        stmt : RETURN exp SEMICOLON
             | exp SEMICOLON
             | block
             | WHILE LRB exp RRB stmt
             | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
             | IF LRB exp RRB stmt elseiflist
             | IF LRB exp RRB stmt elseiflist ELSE stmt
             | PRINT LRB ID RRB SEMICOLON
        """
        print("""
        stmt : RETURN exp SEMICOLON
             | exp SEMICOLON
             | block
             | WHILE LRB exp RRB stmt 
             | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt 
             | IF LRB exp RRB stmt elseiflist 
             | IF LRB exp RRB stmt elseiflist ELSE stmt 
             | PRINT LRB ID RRB SEMICOLON
         """)

    def p_elseiflist(self, p):
        """
        elseiflist : ELIF LRB exp RRB stmt
                   | elseiflist ELIF LRB exp RRB stmt
                   |
        """
        print("""
        elseiflist : ELIF LRB exp RRB stmt 
                   | elseiflist ELIF LRB exp RRB stmt 
                   | 
         """)

    def p_exp(self, p):
        """
        exp : lvalue ASSIGN exp
            | exp operator exp
            | exp relop exp
            | const
            | lvalue
            | ID LRB explist RRB
            | LRB exp RRB
            | ID LRB RRB
            | SUB exp
            | NOT exp
        """
        print("""
        exp : lvalue ASSIGN exp
            | exp operator exp
            | exp relop exp
            | const
            | lvalue
            | ID LRB explist RRB
            | LRB exp RRB
            | ID LRB RRB
            | SUB exp
            | NOT exp
         """)

    def p_operator(self, p):
        """
        operator : OR
                 | AND
                 | SUM
                 | SUB
                 | MUL
                 | DIV
                 | MOD
        """
        print("""
        operator : OR 
                 | AND 
                 | SUM 
                 | SUB 
                 | MUL 
                 | DIV 
                 | MOD
         """)

    def p_const(self, p):
        """
        const : INTEGERNUMBER
              | FLOATNUMBER
              | TRUE
              | FALSE
        """
        print("""
        const : INTEGERNUMBER 
              | FLOATNUMBER 
              | TRUE 
              | FALSE
         """)

    def p_relop(self, p):
        """
        relop : GT
              | LT
              | NE
              | EQ
              | GE
              | LE
        """
        print("""
        relop : GT 
              | LT 
              | NE 
              | EQ 
              | GE 
              | LE
         """)

    def p_explist(self, p):
        """
        explist : exp
                | explist COMMA exp
        """
        print("""
        explist : exp 
                | explist COMMA exp
         """)

    # Deeper Tokens Higher Priority
    precedence = (
        ('nonassoc', 'GT', 'LT', 'NE', 'EQ', 'GE', 'LE'),  # Nonassociative operators
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('Parsing Error: invalid grammar at', p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser