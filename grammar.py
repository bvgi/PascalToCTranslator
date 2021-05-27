import sys

from ply import yacc, lex
from tokens import *
from Node import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'FLOAT_DIV'),
    ('left', 'INT_DIV', 'MOD'),
    ('left', 'EQ', 'NEQ', 'LTE', 'LT', 'GT', 'GTE'),
    ('left', 'OR', 'AND'),
)


def p_empty(p):
    'empty : '
    pass


def p_program(p):
    'program : PROGRAM IDENTIFIER SEMICOLON block DOT'
    p[0] = Node('program', p[2], p[4])


def p_block(p):
    '''
    block : variable_declaration_part
            procedure_or_function
            compound_statement
            | variable_declaration_part
            compound_statement
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
    if len(p) > 1:
        p[0] = p[2]


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
    variable_declaration : IDENTIFIER COMMA variable_declartion
                        | IDENTIFIER COLON type SEMICOLON
    '''
    p[0] = Node('variable_declaration', p[1], p[3])

def p_type(p):
    '''
    type : simple_type
    '''
    p[0] = p[1]


def p_simple_type(p):
    ''' type : SINTEGER
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
        p[0] = Node('function_list', p[1], p[3])


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
        p[0] = Node("function_head", p[2], p[3])
    else:
        p[0] = Node("function_head", p[2], p[4], p[7])


def p_procedure_declaration(p):
    """procedure_declaration : procedure_heading SEMICOLON block"""
    p[0] = Node("procedure", p[1], p[3])


def p_procedure_heading(p):
    """ procedure_heading : PROCEDURE identifier
    | PROCEDURE identifier LPAREN parameter_list RPAREN"""

    if len(p) == 3:
        p[0] = Node("procedure_head", p[2])
    else:
        p[0] = Node("procedure_head", p[2], p[4])





def p_parameter_list(p):
    """ parameter_list : parameter COMMA parameter_list
    | parameter"""
    if len(p) == 4:
        p[0] = Node("parameter_list", p[1], p[3])
    else:
        p[0] = p[1]


def p_parameter(p):
    """ parameter : identifier COLON type"""
    p[0] = Node("parameter", p[1], p[3])


def p_statement_part(p):
    """statement_part : BEGIN statement_sequence END"""
    p[0] = p[2]


def p_statement_sequence(p):
    """statement_sequence : statement SEMICOLON statement_sequence
     | statement"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('statement_list', p[1], p[3])


def p_statement(p):
    """statement : assignment_statement
     | statement_part
     | if_statement
     | while_statement
     | repeat_statement
     | for_statement
     | procedure_or_function_call
     |
    """
    if len(p) > 1:
        p[0] = p[1]


def p_procedure_or_function_call(p):
    """ procedure_or_function_call : identifier LPAREN param_list RPAREN
    | identifier """

    if len(p) == 2:
        p[0] = Node("function_call", p[1])
    else:
        p[0] = Node("function_call", p[1], p[3])


def p_param_list(p):
    """ param_list : param_list COMMA param
     | param """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("parameter_list", p[1], p[3])


def p_param(p):
    """ param : expression """
    p[0] = Node("parameter", p[1])


def p_if_statement(p):
    """if_statement : IF expression THEN statement ELSE statement
    | IF expression THEN statement
    """

    if len(p) == 5:
        p[0] = Node('if', p[2], p[4])
    else:
        p[0] = Node('if', p[2], p[4], p[6])


def p_while_statement(p):
    """while_statement : WHILE expression DO statement"""
    p[0] = Node('while', p[2], p[4])


def p_repeat_statement(p):
    """repeat_statement : REPEAT statement UNTIL expression"""
    p[0] = Node('repeat', p[2], p[4])


def p_for_statement(p):
    """for_statement : FOR assignment_statement TO expression DO statement
    | FOR assignment_statement DOWNTO expression DO statement
    """
    p[0] = Node('for', p[2], p[3], p[4], p[6])


def p_assignment_statement(p):
    """assignment_statement : identifier ASSIGNMENT expression"""
    p[0] = Node('assign', p[1], p[3])


def p_expression(p):
    """expression : expression and_or expression_m
    | expression_m
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('op', p[2], p[1], p[3])


def p_expression_m(p):
    """ expression_m : expression_s
    | expression_m sign expression_s"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('op', p[2], p[1], p[3])


def p_expression_s(p):
    """ expression_s : element
    | expression_s psign element"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node('op', p[2], p[1], p[3])


def p_and_or(p):
    """ and_or : AND
    | OR """
    p[0] = Node('and_or', p[1])


def p_psign(p):
    """psign : TIMES
    | DIVISION"""
    p[0] = Node('sign', p[1])


def p_sign(p):
    """sign : PLUS
    | MINUS
    | DIV
    | MOD
    | EQ
    | NEQ
    | LT
    | LTE
    | GT
    | GTE
    """
    p[0] = Node('sign', p[1])


def p_element(p):
    """element : identifier
    | real
    | integer
    | string
    | char
    | LPAREN expression RPAREN
    | NOT element
    | function_call_inline
    """
    if len(p) == 2:
        p[0] = Node("element", p[1])
    elif len(p) == 3:
        # not e
        p[0] = Node('not', p[2])
    else:
        # ( e )
        p[0] = Node('element', p[2])


def p_function_call_inline(p):
    """ function_call_inline : identifier LPAREN param_list RPAREN"""
    p[0] = Node('function_call_inline', p[1], p[3])


def p_identifier(p):
    """ identifier : IDENTIFIER """
    p[0] = Node('identifier', str(p[1]).lower())


def p_real(p):
    """ real : REAL """
    p[0] = Node('real', p[1])


def p_integer(p):
    """ integer : INTEGER """
    p[0] = Node('integer', p[1])


def p_string(p):
    """ string : STRING """
    p[0] = Node('string', p[1])


def p_char(p):
    """ char : CHAR """
    p[0] = Node('char', p[1])


def p_error(p):
    print
    "Syntax error in input, in line %d!" % p.lineno
    sys.exit()
