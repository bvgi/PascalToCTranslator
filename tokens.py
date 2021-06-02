from ply import lex

QUOTE = r'(\'|")'

tokens = (

    # assignment
    'IDENTIFIER',
    'ASSIGNMENT',
    'SEMICOLON',
    'COLON',
    'COMMA',

    # main
    'PROGRAM',
    'DOT',

    # blocks
    'VAR',
    'BEGIN',
    'END',

    # control flow
    'IF',
    'THEN',
    'ELSE',
    'FOR',
    'WHILE',
    'REPEAT',
    'UNTIL',
    'DO',
    'TO',
    'DOWNTO',

    # logic
    'AND',
    'OR',
    'NOT',

    # operations
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'INT_DIV',
    'FLOAT_DIV',
    'MOD',

    # comparations
    'EQ',
    'NEQ',
    'LT',
    'GT',
    'LTE',
    'GTE',

    # functions
    'LPAREN',
    'RPAREN',
    # 'LBRACKET',
    # 'RBRACKET',
    'PROCEDURE',
    'FUNCTION',
    # 'OF',

    # types
    # 'ARRAY',
    'REAL',
    'INTEGER',
    'STRING',
    'CHAR',
    'BOOLEAN',
    # 'BOOLEAN_TRUE',
    # 'BOOLEAN_FALSE',

    # types names
    # 'SARRAY',
    'SREAL',
    'SINTEGER',
    'SSTRING',
    'SCHAR',
    'SBOOLEAN',
)

# Regular statement rules for tokens.
t_DOT = r"\."

t_ASSIGNMENT = r":="
t_SEMICOLON = r";"
t_COLON = r":"
t_COMMA = r","

t_PLUS = r"\+"
t_MINUS = r"\-"
t_MULTIPLY = r"\*"
t_FLOAT_DIV = r"/"

t_EQ = r"\="
t_NEQ = r"\<\>"
t_LT = r"\<"
t_GT = r"\>"
t_LTE = r"\<\="
t_GTE = r"\>\="

t_LPAREN = r"\("
t_RPAREN = r"\)"
# t_LBRACKET = r"\["
# t_RBRACKET = r"\]"

# t_REAL = r"(\-)*[0-9]+\.[0-9]+"
# t_INTEGER = r"(\-)*[0-9]+"

reserved_keywords = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'begin': 'BEGIN',
    'end': 'END',

    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'repeat': 'REPEAT',
    'do': 'DO',
    'to': 'TO',
    'downto': 'DOWNTO',
    'until': 'UNTIL',

    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',

    'div': 'INT_DIV',
    'mod': 'MOD',

    'procedure': 'PROCEDURE',
    'function': 'FUNCTION',
    # 'of': 'OF',

    # 'true': 'BOOLEAN_TRUE', #TODO: dopytać
    # 'false': 'BOOLEAN_FALSE',

    'real': 'SREAL',
    'integer': 'SINTEGER',
    'string': 'SSTRING',
    'char': 'SCHAR',
    'boolean': 'SBOOLEAN',

    # 'array': 'SARRAY',
}

def t_BOOLEAN(t):
    r"true|false"
    t.value = bool(t.value)
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    if t.value.lower() in reserved_keywords:
        t.type = reserved_keywords[t.value.lower()]
    return t

def t_REAL(t):
    r"(\-)*[0-9]+\.[0-9]+"
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r"(\-)*[0-9]+"
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r"(\'([^\\\'])\')"
    return t


def t_STRING(t):
    r"\'([^\\\']|(\\.))*\'"
    # escaped = 0
    # s = t.value[1:-1]
    # new_str = ""
    # for i in range(0, len(s)):
    #     c = s[i]
    #     if escaped:
    #         if c == "n":
    #             c = "\n"
    #         elif c == "t":
    #             c = "\t"
    #         new_str += c
    #         escaped = 0
    #     else:
    #         if c == "\\":
    #             escaped = 1
    #         else:
    #             new_str += c
    return t
#


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs).
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])


if __name__ == '__main__':
    lexer = lex.lex()
    data = '''program TEST;
    var
    i: integer;
    j: boolean;

    procedure foo;
    begin
        i := 1;
    end;
    
    begin
        j := true;
        for i := 0 to 2 do
        begin
            writeLn(i);
            foo;
        end;
    end.'''
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

#     # Build the lexer
#     from ply import lex
#     import sys
#
#     lex.lex()
#
#     if len(sys.argv) > 1:
#         f = open(sys.argv[1], "r")
#         data = f.read()
#         f.close()
#     else:
#         data = ""
#         while 1:
#             try:
#                 data += input() + "\n"
#             except:
#                 break
#
#     lex.input(data)
#
#     # Tokenize
#     while 1:
#         tok = lex.token()
#         if not tok: break  # No more input
#         print(tok)
