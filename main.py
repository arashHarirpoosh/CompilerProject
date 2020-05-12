from Lexer import Lexer
from Parser import Parser
lexer = Lexer().build()
# file = open('TestCases/Lexer_TestCases/test1.txt')
file = open('TestCases/Parser_TestCases/test2.txt')
print(file.name)
# lexer_res = open('Results/Lexer_Results/lexer_result_' + file.name.split('/')[-1].title(), 'w')
# parser_res = open('Results/Parser_Results/parser_result_' + file.name.split('/')[-1].title(), 'w')
text_input = file.read()
file.close()
lexer.input(text_input)

# while True:
#     tok = lexer.token()
#     if not tok: break
#     print(tok)
    # lexer_res.write(str(tok)+'\n')
#
# lexer_res.close()

parser = Parser()
parser.build().parse(text_input, lexer, False)
