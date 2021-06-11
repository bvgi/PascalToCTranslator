import sys
from nodes import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'FLOAT_DIV'),
    ('left', 'INT_DIV', 'MOD'),
    ('left', 'EQ', 'NEQ', 'LTE', 'LT', 'GT', 'GTE'),
    ('left', 'OR', 'AND'),
)


def p_empty(p):
    '''empty : '''
    p[0] = Empty()


def p_program(p):
    '''
    program : PROGRAM identifier SEMICOLON variable_declaration_part procedure_or_function compound_statement DOT
    '''
    p[0] = Program(p[2], p[4], p[5], p[6])


def p_block(p):
    '''
    block : variable_declaration_part procedure_or_function compound_statement
    '''
    p[0] = Block(p[1], p[2], p[3])


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
        p[0] = VariableDeclarationList(p[1], p[2])


def p_variable_declaration(p):
    '''
    variable_declaration : identifier COLON type SEMICOLON
    '''
    p[0] = Variable(p[1], p[3])


def p_type(p):
    '''
    type : SINTEGER
	         | SCHAR
	         | SREAL
	         | SSTRING
	         | SBOOLEAN
    '''
    p[0] = Type(p[1].lower())


def p_procedure_or_function(p):
    '''
    procedure_or_function : proc_or_func_declaration SEMICOLON procedure_or_function
                        | empty
    '''
    if len(p) == 4:
        p[0] = ProcedureOrFunction(p[1], p[3])
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
    p[0] = Function(p[1], p[3])


def p_function_heading(p):
    '''
    function_heading : FUNCTION identifier COLON type
                    | FUNCTION identifier LPAREN parameters_list RPAREN COLON type
    '''
    if len(p) == 5:
        p[0] = FunctionHeading(p[2], p[4])
    else:
        p[0] = FunctionHeading(p[2], p[7], p[4])


def p_parameters_list(p):
    '''parameters_list : parameter SEMICOLON parameters_list
		                | parameter
    '''
    if len(p) == 4:
        p[0] = ParametersList(p[1], p[3])
    else:
        p[0] = p[1]


def p_parameter(p):
    ''' parameter : identifier COLON type '''
    p[0] = Parameter(p[1], p[3])


def p_procedure_declaration(p):
    ''' procedure_declaration : procedure_heading SEMICOLON block '''
    p[0] = Procedure(p[1], p[3])


def p_procedure_heading(p):
    '''
        procedure_heading : PROCEDURE identifier
                            | PROCEDURE identifier LPAREN parameters_list RPAREN
	'''
    if len(p) == 3:
        p[0] = ProcedureHeading(p[2])
    else:
        p[0] = ProcedureHeading(p[2], p[4])


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
        p[0] = StatementSequence(p[1], p[3])


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
    p[0] = p[1]


def p_procedure_or_function_call(p):
    '''
        procedure_or_function_call : identifier
                                 | identifier LPAREN variables_list RPAREN
    '''
    if len(p) == 2:
        p[0] = ProcOrFunCall(p[1])
    else:
        p[0] = ProcOrFunCall(p[1], p[3])


def p_variables_list(p):
    '''
        variables_list : variables_list COMMA expression
	                    | expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = VariablesList(p[1], p[3])


def p_assignment_statement(p):
    '''
        assignment_statement : identifier ASSIGNMENT expression
    '''
    p[0] = Assignment(p[1], p[3])


def p_if_statement(p):
    '''
        if_statement : IF expression THEN compound_statement
                    | IF expression THEN compound_statement ELSE compound_statement
    '''
    if len(p) == 5:
        p[0] = If(p[2], p[4])
    else:
        p[0] = IfElse(p[2], p[4], p[6])


def p_while_statement(p):
    '''
        while_statement : WHILE expression DO statement
    '''
    p[0] = While(p[2], p[4])


def p_repeat_statement(p):
    '''
        repeat_statement : REPEAT statement_sequence UNTIL expression
    '''
    p[0] = Repeat(p[2], p[4])


def p_for_statement(p):
    '''
    for_statement : FOR assignment_statement TO expression DO statement
		        | FOR assignment_statement DOWNTO expression DO statement
    '''
    p[0] = For(p[2], p[3], p[4], p[6])


def p_expression(p):
    '''
        expression : expression and_or expression_m
	               | expression_m
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Expression(p[1], p[2], p[3])


def p_expression_m(p):
    '''
        expression_m : element
	                | expression_m sign element
    '''
    if len(p) == 2:
        p[0] = Element(p[1])
    else:
        p[0] = Expression(p[1], p[2], p[3])


def p_and_or(p):
    '''
        and_or : AND
               | OR
    '''
    p[0] = AndOr(p[1])


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
    p[0] = Sign(p[1])


def p_element(p):
    '''
        element : BOOLEAN
                | NOT element
                | identifier
                | real
                | integer
                | char
                | string
                | LPAREN expression RPAREN
                | function_call
                | empty
    '''
    if len(p) == 2:
        p[0] = Element(p[1])
    elif len(p) == 3:
        p[0] = Element(p[2], no=True)
    else:
        p[0] = Element(p[2])


def p_function_call(p):
    '''
        function_call : identifier LPAREN variables_list RPAREN
    '''
    p[0] = FunctionCall(p[1], p[3])


def p_identifier(p):
    ''' identifier : IDENTIFIER '''
    p[0] = Identifier(str(p[1]).lower())


def p_real(p):
    ''' real : REAL '''
    p[0] = Real(p[1])


def p_integer(p):
    ''' integer : INTEGER '''
    p[0] = Integer(p[1])


def p_string(p):
    ''' string : STRING '''
    p[0] = String(p[1])


def p_char(p):
    ''' char : CHAR '''
    p[0] = Char(p[1])


def p_error(p):
    print("Syntax error in input, in line %d!" % p.lineno)
    sys.exit()

