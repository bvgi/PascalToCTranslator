import logging

from ply import yacc

from tokens import *
from grammar import *

if __name__ == '__main__':
    lexer = lex.lex()
    logging.basicConfig(
        level=logging.DEBUG,
        filename="parselog.txt",
        filemode="w",
        format="%(filename)10s:%(lineno)4d:%(message)s"
    )

    log = logging.getLogger()
    parser = yacc.yacc(start="program", debug=True, errorlog=log)
    test = open('tests/test1.pas', 'r')
    data = test.read()

    ast = parser.parse(input=data, lexer=lexer)
    print(ast)
    file = open('tests/test1.c', 'w')
    file.write(ast.toC())
    file.close()
