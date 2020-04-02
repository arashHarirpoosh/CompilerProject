from Lexer import Lexer
lexer = Lexer().build()
file = open('TestCases/test1.txt')
text_input = file.read()
file.close()
lexer.input(text_input)
while True:
    tok = lexer.token()
    if not tok: break
    print(tok)
