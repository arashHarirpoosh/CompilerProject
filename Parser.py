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
        declist : declist dec
        """
        print("""
        declist :  declist dec 
        """)

    def p_declist_Landa(self, p):
        """
        declist :
        """
        print("""
        declist : 
        """)

    def p_dec(self, p):
        """
        dec : vardec
        """
        print("""
        dec : vardec
        """)

    def p_dec_funcdec(self, p):
        """
        dec : funcdec
        """
        print("""
        dec : funcdec
        """)

    def p_type_INTEGER(self, p):
        """
        type : INTEGER
        """
        print("""
        type : INTEGER
        """)

    def p_type_Float(self, p):
        """
        type : FLOAT
        """
        print("""
        type : FLOAT
        """)

    def p_type_BOOLEAN(self, p):
        """
        type : BOOLEAN
        """
        print("""
        type : BOOLEAN
        """)

    def p_iddec(self, p):
        """
        iddec : ID
        """
        print("""
        iddec : ID
         """)

    def p_iddec_LSB(self, p):
        """
        iddec : ID LSB exp RSB
        """
        print("""
        iddec : ID LSB exp RSB
         """)

    def p_iddec_ASSIGN(self, p):
        """
        iddec : ID ASSIGN exp
        """
        print("""
        iddec : ID ASSIGN exp
         """)

    def p_idlist(self, p):
        """
        idlist : iddec
        """
        print("""
        idlist : iddec
         """)

    def p_idlist_idlist(self, p):
        """
        idlist : idlist COMMA iddec
        """
        print("""
        idlist : idlist COMMA iddec
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
        """
        print("""
        funcdec : type ID LRB paramdecs RRB block 
         """)

    def p_funcdec_VOID(self, p):
        """
        funcdec : VOID ID LRB paramdecs RRB block
        """
        print("""
        funcdec : VOID ID LRB paramdecs RRB block
         """)

    def p_paramdecs(self, p):
        """
        paramdecs : paramdecslist
        """
        print("""
        paramdecs : paramdecslist
         """)

    def p_paramdecs_Landa(self, p):
        """
        paramdecs :
        """
        print("""
        paramdecs : 
         """)

    def p_paramdecslist(self, p):
        """
        paramdecslist : paramdec
        """
        print("""
        paramdecslist : paramdec
         """)

    def p_paramdecslist_COMMA(self, p):
        """
        paramdecslist : paramdecslist COMMA paramdec
        """
        print("""
        paramdecslist : paramdecslist COMMA paramdec
         """)

    def p_paramdec(self, p):
        """
        paramdec : type ID
        """
        print("""
        paramdec : type ID
         """)

    def p_paramdec_type(self, p):
        """
        paramdec : type ID LSB RSB
        """
        print("""
        paramdec : type ID LSB RSB
         """)

    def p_varlist(self, p):
        """
        varlist : vardec varlist
        """
        print("""
        varlist : vardec  varlist 
         """)

    def p_varlist_Landa(self, p):
        """
        varlist :
        """
        print("""
        varlist : 
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
        stmtlist : stmtlist stmt
        """
        print("""
        stmtlist : stmtlist stmt
         """)

    def p_stmtlist_Landa(self, p):
        """
        stmtlist :
        """
        print("""
        stmtlist : 
         """)

    def p_lvalue(self, p):
        """
        lvalue : ID
        """
        print("""
        lvalue : ID 
         """)

    def p_lvalue_ID(self, p):
        """
        lvalue : ID LSB exp RSB
        """
        print("""
        lvalue : ID LSB exp RSB
         """)

    def p_stmt_RETURN(self, p):
        """
        stmt : RETURN exp SEMICOLON
        """
        print("""
        stmt : RETURN exp SEMICOLON
        """)

    def p_stmt_exp(self, p):
        """
        stmt : exp SEMICOLON
        """
        print("""
        stmt : exp SEMICOLON
        """)

    def p_stmt_block(self, p):
        """
        stmt : block
        """
        print("""
        stmt : block
        """)

    def p_stmt_WHILE(self, p):
        """
        stmt : WHILE LRB exp RRB stmt
        """
        print("""
        stmt : WHILE LRB exp RRB stmt
        """)

    def p_stmt_FOR(self, p):
        """
        stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
        """
        print("""
        stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
        """)

    def p_stmt_IF(self, p):
        """
        stmt : IF LRB exp RRB stmt elseiflist other
        """
        print("""
        stmt : IF LRB exp RRB stmt elseiflist other
        """)

    def p_other(self, p):
        """
        other : ELSE stmt
        """
        print("""
        other : ELSE stmt
        """)

    def p_other_Landa(self, p):
        """
        other : %prec IF
        """
        print("""
        other : 
        """)


    def p_stmt_PRINT(self, p):
        """
        stmt : PRINT LRB ID RRB SEMICOLON
        """
        print("""
        stmt : PRINT LRB ID RRB SEMICOLON
        """)

    def p_elseiflist(self, p):
        """
        elseiflist : elseiflist ELIF LRB exp RRB stmt
        """
        print("""
        elseiflist : elseiflist ELIF LRB exp RRB stmt
         """)

    def p_elseiflist_Landa(self, p):
        """
        elseiflist :
        """
        print("""
        elseiflist :
         """)

    def p_exp_lvalue(self, p):
        """
        exp : lvalue ASSIGN exp
        """
        print("""
        exp : lvalue ASSIGN exp
         """)

    def p_exp_operator(self, p):
        """
        exp : exp operator exp %prec MUL
        """
        print("""
        exp : exp operator exp
         """)

    def p_exp_relop(self, p):
        """
        exp : exp relop exp %prec GT
        """
        print("""
        exp : exp relop exp
         """)

    def p_exp_const(self, p):
        """
        exp : const
        """
        print("""
        exp : const
         """)

    def p_exp_lval(self, p):
        """
        exp : lvalue
        """
        print("""
        exp : lvalue
         """)

    def p_exp_ID(self, p):
        """
        exp : ID LRB explist RRB
        """
        print("""
        exp : ID LRB explist RRB
         """)

    def p_exp_LRB(self, p):
        """
        exp : LRB exp RRB
        """
        print("""
        exp : LRB exp RRB
        """)

    def p_exp_ID_LRB(self, p):
        """
        exp : ID LRB RRB
        """
        print("""
        exp : ID LRB RRB
         """)

    def p_exp_SUB(self, p):
        """
        exp : SUB exp
        """
        print("""
        exp : SUB exp
         """)

    def p_exp_NOT(self, p):
        """
        exp : NOT exp
        """
        print("""
        exp : NOT exp
         """)

    def p_operator_OR(self, p):
        """
        operator : OR
        """
        print("""
        operator : OR 
         """)

    def p_operator_AND(self, p):
        """
        operator : AND
        """
        print("""
        operator : AND
         """)

    def p_operator_SUM(self, p):
        """
        operator : SUM
        """
        print("""
        operator : SUM
         """)
    def p_operator_SUB(self, p):
        """
        operator : SUB
        """
        print("""
        operator : SUB
         """)

    def p_operator_MUL(self, p):
        """
        operator : MUL
        """
        print("""
        operator : MUL
         """)

    def p_operator_DIV(self, p):
        """
        operator : DIV
        """
        print("""
        operator : DIV
         """)

    def p_operator_MOD(self, p):
        """
        operator : MOD
        """
        print("""
        operator : MOD
         """)

    def p_const_INT(self, p):
        """
        const : INTEGERNUMBER
        """
        print("""
        const : INTEGERNUMBER 
         """)

    def p_const_FLOAT(self, p):
        """
        const : FLOATNUMBER
        """
        print("""
        const : FLOATNUMBER
         """)

    def p_const_TRUE(self, p):
        """
        const : TRUE
        """
        print("""
        const : TRUE
         """)

    def p_const_FALSE(self, p):
        """
        const : FALSE
        """
        print("""
        const : FALSE
         """)

    def p_relop_GT(self, p):
        """
        relop : GT
        """
        print("""
        relop : GT 
         """)

    def p_relop_LT(self, p):
        """
        relop : LT
        """
        print("""
        relop : LT
         """)

    def p_relop_NE(self, p):
        """
        relop : NE
        """
        print("""
        relop : NE
         """)

    def p_relop_EQ(self, p):
        """
        relop : EQ
        """
        print("""
        relop : EQ
         """)

    def p_relop_GE(self, p):
        """
        relop : GE
        """
        print("""
        relop : GE
         """)

    def p_relop_LE(self, p):
        """
        relop : LE
        """
        print("""
        relop : LE
         """)

    def p_explist(self, p):
        """
        explist : exp
        """
        print("""
        explist : exp 
         """)

    def p_explist_COMMA(self, p):
        """
        explist : explist COMMA exp
        """
        print("""
        explist : explist COMMA exp
         """)

    # Deeper Tokens Higher Priority
    precedence = (
        ('left', 'COMMA'),
        ('right', 'ASSIGN'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'GE', 'LT', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('right', 'NOT'),
        ('left', 'LCB', 'LRB', 'LSB', 'RCB', 'RRB', 'RSB'),
        ('left', 'IF'),
        ('left', 'ELIF', 'ELSE')
    )

    def p_error(self, p):
        print('error', p.value)
        raise Exception('Parsing Error: invalid grammar at', p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser