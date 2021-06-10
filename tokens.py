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
    'PROCEDURE',
    'FUNCTION',

    # types
    'REAL',
    'INTEGER',
    'STRING',
    'CHAR',
    'BOOLEAN',

    # types names
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

    'real': 'SREAL',
    'integer': 'SINTEGER',
    'string': 'SSTRING',
    'char': 'SCHAR',
    'boolean': 'SBOOLEAN',
}


def t_BOOLEAN(t):
    r"true|false"
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
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs).
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])

