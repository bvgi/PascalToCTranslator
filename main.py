import logging

from ply import yacc

from tokens import *

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

    data = '''program TEST;
    var
    i: integer;
    procedure foo;
    begin
        i := 1;
    end;
    begin
        while i = 1 do
        begin
            writeln(i);
        end;
        repeat writeln(i)
        until i = 0;
        for i := 0 to 2 do
        begin
            if i = 1 then
            begin
                i := 0;
            end
            else
            begin
                i := 1;
            end;
        end;
    end.'''

    ast = parser.parse(input=data, lexer=lexer, debug=True)
    print(ast)