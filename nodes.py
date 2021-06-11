class Empty:
    def __str__(self):
        return "empty"

    def toC(self):
        return ""


class Program:
    def __init__(self, identifier, variables, proc_or_func, statement):
        self.identifier = identifier
        self.variables = variables
        self.proc_or_func = proc_or_func
        self.statement = statement

    def __str__(self):
        return f"program " + str(self.identifier) + str(self.variables) + str(self.proc_or_func) + str(
            self.statement) + "\n"

    def toC(self):
        converted_statement = "#include <stdio.h> \n \n"
        if not isinstance(self.proc_or_func, Empty):
            converted_statement += self.proc_or_func.toC()
        converted_statement += "\nint main(void){\n"
        if not isinstance(self.variables, Empty):
            converted_statement += self.variables.toC() + "\n"
        if not isinstance(self.statement, Empty):
            converted_statement += self.statement.toC()
        converted_statement += "return 0; \n}"
        return converted_statement


class Block:
    def __init__(self, variable_declaration_part, procedure_or_function, compound_statement):
        self.variable_declaration_part = variable_declaration_part
        self.procedure_or_function = procedure_or_function
        self.compound_statement = compound_statement

    def __str__(self):
        return "block: " + str(self.variable_declaration_part) + ", " + str(self.procedure_or_function) + ", " + str(
            self.compound_statement) + "\n"

    def toC(self):
        output = ""
        if not isinstance(self.variable_declaration_part, Empty):
            output += f"{self.variable_declaration_part.toC()}\n"
        if not isinstance(self.procedure_or_function, Empty):
            output += f"{self.procedure_or_function.toC()}\n"
        if not isinstance(self.compound_statement, Empty):
            output += f"{self.compound_statement.toC()}"
        return output


class FunctionCall:
    def __init__(self, identifier, variables_list):
        self.identifier = identifier
        self.variables_list = variables_list

    def __str__(self):
        return f"function_call: {self.identifier}({self.variables_list}) \n"

    def toC(self):
        return f"{self.identifier.toC()}({self.variables_list.toC()})"


class Real:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"real: {self.value} \n"

    def toC(self):
        return f"{self.value}f"


class Integer:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"integer: {self.value} \n"

    def toC(self):
        return f"{self.value}"


class String:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"string: {self.value} \n"

    def toC(self):
        return f"\"{self.value[1:-1]}\""


class Char:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"char: {self.value}\n"

    def toC(self):
        return f"\'{self.value[1:-1]}\'"


class Identifier:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}\n"

    def toC(self):
        return str(self.name)


class Element:
    def __init__(self, element, no=False):
        self.element = element
        self.no = no

    def __str__(self):
        return f"element: {self.element}\n"

    def toC(self):
        if f"{self.element}"[0:-1] == "element: true":
            return "1"
        elif f"{self.element}"[0:-1] == "element: false":
            return "0"
        elif isinstance(self.element, Expression):
            return f"({self.element.toC()})"
        elif self.no:
            return f"!{self.element.toC()}"
        else:
            return f"{self.element.toC()}"


class Sign:
    def __init__(self, sign):
        self.sign = sign

    def __str__(self):
        return f"sign: {self.sign}"

    def toC(self):
        if self.sign == "div":
            return "/"
        elif self.sign == "mod":
            return "%"
        elif self.sign == "=":
            return "=="
        elif self.sign == "<>":
            return "!="
        else:
            return f"{self.sign}"


class AndOr:
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        return f"and_or: {self.operator} \n"

    def toC(self):
        if self.operator == "and":
            return "&&"
        else:
            return "||"


class Expression:
    def __init__(self, expr1, sign, expr2):
        self.expr1 = expr1
        self.sign = sign
        self.expr2 = expr2

    def __str__(self):
        return f"expression: {self.expr1} {self.sign} {self.expr2}\n"

    def toC(self):
        return f"{self.expr1.toC()} {self.sign.toC()} {self.expr2.toC()}"


class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return f"assignment: {self.identifier} := {self.expression}"

    def toC(self):
        return self.identifier.toC() + " = " + str(self.expression.toC()) + ";\n"


class For:
    def __init__(self, assignment, operator, expression, statement):
        self.assignment = assignment
        self.operator = operator
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"for_statement: for {self.assignment} {self.operator} {self.expression} do {self.statement}\n"

    def toC(self):
        if self.operator == "to":
            return f"for({self.assignment.toC()[:-1]} {self.assignment.identifier.toC()} <= {self.expression.toC()}; {self.assignment.identifier.toC()}++)" + "{ \n" + self.statement.toC() + "}\n"
        else:
            return f"for({self.assignment.toC()[:-1]} {self.assignment.identifier.toC()} >= {self.expression.toC()}; {self.assignment.identifier.toC()}--)" + "{ \n" + self.statement.toC() + "\n}\n"


class Repeat:
    def __init__(self, statement, expression):
        self.statement = statement
        self.expression = expression

    def __str__(self):
        return f"repeat: repeat {self.statement} until {self.expression}\n"

    def toC(self):
        return "do { \n" + self.statement.toC() + "} while(!(" + self.expression.toC() + "));\n"


class While:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"while: while {self.expression} do {self.statement}\n"

    def toC(self):
        return "while(" + self.expression.toC() + ") {\n" + self.statement.toC() + "}\n"


class If:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"If: if {self.expression} then {self.statement}\n"

    def toC(self):
        return "if(" + self.expression.toC() + "){\n" + self.statement.toC() + "}\n"


class IfElse:
    def __init__(self, expression, statement1, statement2):
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

    def __str__(self):
        return f"If: if {self.expression} then {self.statement1} else {self.statement2}\n"

    def toC(self):
        return "if(" + self.expression.toC() + "){\n" + self.statement1.toC() + "} else {\n" + self.statement2.toC() + "}\n"


class VariablesList:
    def __init__(self, variables, expression):
        self.variables = variables
        self.expression = expression

    def __str__(self):
        return f"variables list: {self.variables}, {self.expression}\n"

    def toC(self):
        output = f"{self.variables.toC()}, {self.expression.toC()}"
        return output


class ProcOrFunCall:
    def __init__(self, identifier, variables=None):
        self.identifier = identifier
        self.variables = variables

    def __str__(self):
        return f"procedure or function call: {self.identifier}{self.variables}\n"

    def toC(self):
        if f"{self.identifier}"[0:-1] == "write":
            self.identifier = Identifier("printf")
        elif f"{self.identifier}"[0:-1] == "readln":
            self.identifier = Identifier("scanf")
        if self.variables is None:
            return f"{self.identifier.toC()}();\n"
        else:
            return f"{self.identifier.toC()}({self.variables.toC()});\n"


class StatementSequence:
    def __init__(self, statement, sequence):
        self.statement = statement
        self.sequence = sequence

    def __str__(self):
        return f"statement sequence: {self.statement}; {self.sequence}\n"

    def toC(self):
        output = f"{self.statement.toC()}"
        output += self.sequence.toC()
        return output


class Type:
    def __init__(self, typename):
        self.typename = typename

    def __str__(self):
        return f"type: {self.typename}"

    def toC(self):
        if self.typename == "integer":
            return "int"
        elif self.typename == "real":
            return "float"
        elif self.typename == "boolean":
            return "int"
        elif self.typename == "string":
            return "char"
        else:
            return f"{self.typename}"


class Parameter:
    def __init__(self, identifier, typename):
        self.identifier = identifier
        self.typename = typename

    def __str__(self):
        return f"parameter: {self.identifier}: {self.typename}\n"

    def toC(self):
        if f"{self.typename}" == "type: string":
            return f"{self.typename.toC()} *{self.identifier.toC()}"
        else:
            return f"{self.typename.toC()} {self.identifier.toC()}"


class ParametersList:
    def __init__(self, parameter, p_list):
        self.parameter = parameter
        self.p_list = p_list

    def __str__(self):
        return f"parameters list: {self.parameter}: {self.p_list}\n"

    def toC(self):
        output = self.parameter.toC() + ", " + self.p_list.toC()
        return output


class ProcedureHeading:
    def __init__(self, identifier, parameters=None):
        self.identifier = identifier
        self.parameters = parameters

    def __str__(self):
        return f"procedure heading: {self.identifier}, {self.parameters}\n"

    def toC(self):
        if self.parameters is None:
            return f"void {self.identifier.toC()}()"
        else:
            return f"void {self.identifier.toC()}({self.parameters.toC()})"


class Procedure:
    def __init__(self, heading, block):
        self.heading = heading
        self.block = block

    def __str__(self):
        return f"procedure: {self.heading}; {self.block}\n"

    def toC(self):
        return self.heading.toC() + "{\n" + self.block.toC() + "}\n"


class FunctionHeading:
    def __init__(self, identifier, typename, params=None):
        self.identifier = identifier
        self.typename = typename
        self.params = params

    def __str__(self):
        return f"function heading: {self.identifier} ({self.params}) : {self.typename}\n"

    def toC(self):
        new_type = self.typename.toC()

        if f"{self.typename}" == "type: string":
            new_type += "*"
            declaration_part = f"{self.typename.toC()} *{self.identifier.toC()};\n"
        else:
            declaration_part = f"{self.typename.toC()} {self.identifier.toC()};\n"
        if self.params is None:
            return f"{new_type} {self.identifier.toC()}()" + "{\n" + declaration_part
        else:
            return f"{new_type} {self.identifier.toC()}({self.params.toC()})" + "{\n" + declaration_part


class Function:
    def __init__(self, heading, block):
        self.heading = heading
        self.block = block

    def __str__(self):
        return f"function: {self.heading}; {self.block}\n"

    def toC(self):
        return self.heading.toC() + self.block.toC() + "return " + self.heading.identifier.toC() + ";\n}\n"


class ProcedureOrFunction:
    def __init__(self, declaration, proc_or_func):
        self.declaration = declaration
        self.proc_or_func = proc_or_func

    def __str__(self):
        return f"procedure or function: {self.declaration}; {self.proc_or_func}\n"

    def toC(self):
        return f"{self.declaration.toC()}\n{self.proc_or_func.toC()}"


class Variable:
    def __init__(self, identifier, typename):
        self.identifier = identifier
        self.typename = typename

    def __str__(self):
        return "variable: " + str(self.identifier) + "," + str(self.typename) + "\n"

    def toC(self):
        if f"{self.typename}" == "type: string":
            return f"{self.typename.toC()} *{self.identifier.toC()};"
        else:
            return f"{self.typename.toC()} {self.identifier.toC()};"


class VariableDeclarationList:
    def __init__(self, variable, varlist):
        self.variable = variable
        self.varlist = varlist

    def __str__(self):
        return f"variable list: {self.variable} {self.varlist}\n"

    def toC(self):
        return f"{self.variable.toC()}\n{self.varlist.toC()}"
