from Lexer import Lexer
lexer = Lexer().build()
file = open('TestCases/test1.txt')
print(file.name)
res = open('Results/result'+file.name.split('/')[-1].title(), 'w')
text_input = file.read()
file.close()
lexer.input(text_input)
while True:
    tok = lexer.token()
    if not tok: break
    print(tok)
    res.write(str(tok)+'\n')

res.close()

