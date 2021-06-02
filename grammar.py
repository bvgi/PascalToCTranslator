import sys

from ply import yacc, lex
from tokens import *
from Node import *
import logging

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'FLOAT_DIV'),
    ('left', 'INT_DIV', 'MOD'),
    ('left', 'EQ', 'NEQ', 'LTE', 'LT', 'GT', 'GTE'),
    ('left', 'OR', 'AND'),
)


def p_empty(p):
    '''empty : '''
    pass


def p_program(p):
    '''
    program : PROGRAM IDENTIFIER SEMICOLON block DOT
    '''
    p[0] = Node('program', p[2], p[4])


def p_block(p):
    '''
    block : variable_declaration_part procedure_or_function compound_statement
    '''
    if len(p) == 4:
        p[0] = Node('block', p[1], p[2], p[3])
    else:
        p[0] = Node('block', p[1], p[2])


def p_variable_declaration_part(p):
    '''
    variable_declaration_part : empty
                                | VAR variable_declaration_list
    '''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_variable_declaration_list(p):
    '''
    variable_declaration_list : variable_declaration
                            | variable_declaration variable_declaration_list
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('variable_declaration_list', p[1], p[2])


def p_variable_declaration(p):
    '''
    variable_declaration : IDENTIFIER COMMA variable_declaration
                        | IDENTIFIER COLON type SEMICOLON
    '''
    p[0] = Node('variable_declaration', p[1], p[3])


def p_type(p):
    '''
    type : SINTEGER
	         | SCHAR
	         | SREAL
	         | SSTRING
	         | SBOOLEAN
    '''
    p[0] = Node('type', p[1].lower())


def p_procedure_or_function(p):
    '''
    procedure_or_function : proc_or_func_declaration SEMICOLON procedure_or_function
                        | empty
    '''
    if len(p) == 4:
        p[0] = Node('procedure_or_function', p[1], p[3])
    else:
        p[0] = p[1]


def p_proc_or_func_declaration(p):
    '''proc_or_func_declaration : procedure_declaration
   				                | function_declaration
    '''
    p[0] = p[1]


def p_function_declaration(p):
    '''
    function_declaration : function_heading SEMICOLON block
    '''
    p[0] = Node('function', p[1], p[3])


def p_function_heading(p):
    '''
    function_heading : FUNCTION type
                    | FUNCTION IDENTIFIER COLON type
                    | FUNCTION IDENTIFIER LPAREN parameters_list RPAREN COLON type
    '''
    if len(p) == 3:
        p[0] = Node("function_head", p[2])
    elif len(p) == 5:
        p[0] = Node("function_head", p[2], p[4])
    else:
        p[0] = Node("function_head", p[2], p[4], p[7])


def p_parameters_list(p):
    '''parameters_list : parameter COMMA parameters_list
		                | parameter
    '''
    if len(p) == 4:
        p[0] = Node("parameters_list", p[1], p[3])
    else:
        p[0] = p[1]


def p_parameter(p):
    ''' parameter : IDENTIFIER COLON type '''
    p[0] = Node("parameter", p[1], p[3])


def p_procedure_declaration(p):
    ''' procedure_declaration : procedure_heading SEMICOLON block '''
    p[0] = Node("procedure", p[1], p[3])


def p_procedure_heading(p):
    '''
        procedure_heading : PROCEDURE IDENTIFIER
                            | PROCEDURE IDENTIFIER LPAREN parameters_list RPAREN
	'''
    if len(p) == 3:
        p[0] = Node("procedure_head", p[2])
    else:
        p[0] = Node("procedure_head", p[2], p[4])


def p_compound_statement(p):
    '''
        compound_statement : BEGIN statement_sequence END
    '''
    p[0] = p[2]


def p_statement_sequence(p):
    '''
        statement_sequence : statement SEMICOLON statement_sequence
			                | statement SEMICOLON
    '''
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = Node('statement_sequence', p[1], p[3])


def p_statement(p):
    '''
    statement : compound_statement
             | assignment_statement
             | if_statement
             | while_statement
             | repeat_statement
             | for_statement
             | procedure_or_function_call
    '''
    # if len(p) > 1: #EMPTY
    p[0] = p[1]

# def p_statement(p):
#     '''
#         statement : no_if_statement
#                 | if_statement
#     '''
#     p[0] = p[1]


def p_procedure_or_function_call(p):
    '''
        procedure_or_function_call : IDENTIFIER
                                 | IDENTIFIER LPAREN variables_list RPAREN
    '''
    if len(p) == 2:
        p[0] = Node("procedure_or_function_call", p[1])
    else:
        p[0] = Node("procedure_or_function_call", p[1], p[3])


def p_variables_list(p):
    '''
        variables_list : variables_list COMMA variable
	                    | variable
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("variables_list", p[1], p[3])


def p_variable(p):
    '''
        variable : expression
    '''
    p[0] = Node("parameter", p[1])


def p_assignment_statement(p):
    '''
        assignment_statement : IDENTIFIER ASSIGNMENT expression
    '''
    p[0] = Node('assign', p[1], p[3])


# def p_if_statement(p):
#     '''
#         if_statement : open_statement
#                     | closed_statement
#     '''
#     p[0] = p[1]
#
#
# def p_open_statement(p):
#     '''
#         open_statement : IF expression THEN if_statement
#                     | IF expression THEN closed_statement ELSE open_statement
#     '''
#     if len(p) == 5:
#         p[0] = Node('open_if', p[2], p[4])
#     else:
#         p[0] = Node('open_if', p[2], p[4], p[6])
#
#
# def p_closed_statement(p):
#     '''
#         closed_statement : statement
#                         | IF expression THEN closed_statement ELSE closed_statement
#     '''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = Node('closed_if', p[2], p[4], p[6])

# def p_no_if_statement(p):
#     '''
#         no_if_statement : compound_statement
#              | assignment_statement
#              | while_statement
#              | repeat_statement
#              | for_statement
#              | procedure_or_function_call
#     '''
#     p[0] = p[1]


def p_if_statement(p):
    '''
        if_statement : IF expression THEN compound_statement else_statement
    '''
    # if len(p) == 5:
    p[0] = Node('if', p[2], p[4], p[5])
    # else:
    #     p[0] = Node('if', p[2], p[4], p[6])


def p_else_statement(p):
    '''
        else_statement : ELSE compound_statement
                    | empty
    '''
    if len(p) == 3:
        p[0] = Node('if', p[2])
    else:
        p[0] = p[1]


def p_while_statement(p):
    '''
        while_statement : WHILE expression DO statement
    '''
    p[0] = Node('while', p[2], p[4])


def p_repeat_statement(p):
    '''
        repeat_statement : REPEAT statement UNTIL expression
    '''
    p[0] = Node('repeat', p[2], p[4])


def p_for_statement(p):
    '''
    for_statement : FOR assignment_statement TO expression DO statement
		        | FOR assignment_statement DOWNTO expression DO statement
    '''
    p[0] = Node('for', p[2], p[3], p[4], p[6])


def p_expression(p):
    '''
        expression : expression and_or expression_m
	               | expression_m
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('expr', p[2], p[1], p[3])


def p_expression_m(p):
    '''
        expression_m : element
	                | expression_m sign element
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('expr', p[2], p[1], p[3])


def p_and_or(p):
    '''
        and_or : AND
               | OR
    '''
    p[0] = Node('and_or', p[1])


def p_sign(p):
    '''
        sign : PLUS
            | MINUS
            | INT_DIV
            | FLOAT_DIV
            | MULTIPLY
            | MOD
            | EQ
            | NEQ
            | LT
            | GT
            | LTE
            | GTE
    '''
    p[0] = Node('sign', p[1])


def p_element(p):
    '''
        element : BOOLEAN
               | NOT element
               | IDENTIFIER
               | REAL
               | INTEGER
               | CHAR
               | STRING
               | LPAREN expression RPAREN
               | function_call
    '''
    if len(p) == 2:
        p[0] = Node("element", p[1])
    elif len(p) == 3:
        p[0] = Node('not', p[2])
    else:
        p[0] = Node('element', p[2])


def p_function_call(p):
    '''
        function_call : IDENTIFIER LPAREN variables_list RPAREN
    '''
    p[0] = Node('function_call', p[1], p[3])


# def p_identifier(p):
#     """ identifier : IDENTIFIER """
#     p[0] = Node('identifier', str(p[1]).lower())
#
#
# def p_real(p):
#     """ real : REAL """
#     p[0] = Node('real', p[1])
#
#
# def p_integer(p):
#     """ integer : INTEGER """
#     p[0] = Node('integer', p[1])
#
#
# def p_string(p):
#     """ string : STRING """
#     p[0] = Node('string', p[1])
#
#
# def p_char(p):
#     """ char : CHAR """
#     p[0] = Node('char', p[1])


def p_error(p):
    print("Syntax error in input, in line %d!" % p.lineno)
    sys.exit()


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

    # lexer.input(data)
    result = parser.parse(input=data, lexer=lexer, debug=True)
    print(result)
