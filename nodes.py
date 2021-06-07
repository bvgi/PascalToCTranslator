class Program:
    def __init__(self, identifier, variables, proc_or_func, statement):
        self.identifier = identifier
        self.variables = variables
        self.proc_or_func = proc_or_func
        self.statement = statement

    def __str__(self):
        return "program " + self.identifier + self.variables + self.proc_or_func + self.statement

    def toC(self):
        converted_statement = "#include <stdio.h> \n \n"
        converted_statement += self.proc_or_func.toC()
        converted_statement += "int main(void){\n"
        converted_statement += self.variables.toC() + "\n"
        converted_statement += self.statement.toC() + "\n"
        converted_statement += "return 0; \n}"


class Block:
    def __init__(self, variable_declaration_part, procedure_or_function, compound_statement):
        self.variable_declaration_part = variable_declaration_part
        self.procedure_or_function = procedure_or_function
        self.compound_statement = compound_statement

    def __str__(self):
        return "block: " + self.variable_declaration_part + ", " + self.procedure_or_function + ", " + self.compound_statement

    def toC(self):
        return f"{self.variable_declaration_part.toC()}\n{self.procedure_or_function.toC()}\n{self.compound_statement.toC()}\n"


class FunctionCall:
    def __init__(self, identifier, variables_list):
        self.variables_list = variables_list
        self.identifier = identifier

    def __str__(self):
        return f"function_call: {self.identifier}({self.variables_list});"

    def toC(self):
        return f"{self.identifier}({self.variables_list.toC});"


class Element:
    def __init__(self, element, no=False):
        self.element = element
        self.no = no

    def __str__(self):
        return f"element: {self.element}"

    def toC(self):
        if isinstance(self.element, FunctionCall):
            return self.element.toC()
        elif isinstance(self.element, Expression):
            return f"({self.element.toC()})"
        elif self.no:
            return f"!{self.element.toC()}"
        else:
            if self.element == "true":
                return "1"
            elif self.element == "false":
                return "0"




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
        return f"and_or: {self.operator}"

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
        return f"expression: {self.expr1} {self.sign} {self.expr2}"

    def toC(self):
        return f"{self.expr1.toC()} {self.sign.toC()} {self.expr2.toC()}"


class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return f"assignment: {self.identifier} := {self.expression}"

    def toC(self):
        return f"{self.identifier} = {self.expression.toC()};"


class For:
    def __init__(self, assignment, operator, expression, statement):
        self.assignment = assignment
        self.operator = operator
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"for_statement: for {self.assignment, self.operator, self.expression} do {self.statement}"

    def toC(self):
        if self.operator == "to":
            return f"for({self.assignment.toC()} ; {self.assignment.identifier}<={self.assignment.expression.toC()} ; {self.assignment.identifier}++)" + "{ \n" + self.statement.toC() + "\n}"
        else:
            return f"for({self.assignment.toC()} ; {self.assignment.identifier} <= {self.assignment.expression.toC()} ; {self.assignment.identifier}--)" + "{ \n" + self.statement.toC() + "\n}"


class Repeat:
    def __init__(self, statement, expression):
        self.statement = statement
        self.expression = expression

    def __str__(self):
        return f"repeat: repeat {self.statement} until {self.expression}"

    def toC(self):
        return "do { \n" + self.statement.toC() + "\n } while(" + self.expression.toC() + ");"


class While:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"while: while {self.expression} do {self.statement}"

    def toC(self):
        return "while(" + self.expression.toC() + "){\n" + self.statement.toC() + "\n}"


class If:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"If: if {self.expression} then {self.statement}"

    def toC(self):
        return "if(" + self.expression.toC() + "){\n" + self.statement.toC() + "\n}"


class IfElse:
    def __init__(self, expression, statement1, statement2):
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

    def __str__(self):
        return f"If: if {self.expression} then {self.statement1} else {self.statement2}"

    def toC(self):
        return "if(" + self.expression.toC() + "){\n" + self.statement1.toC() + "\n} else { \n" + self.statement2.toC() + "\n}"


class VariablesList:
    def __init__(self, variables, expression):
        self.variables = variables
        self.expression = expression

    def __str__(self):
        return f"variables list: {self.variables}, {self.expression}"

    def toC(self):
        output = ""
        for i, var in enumerate(self.variables):
            if i != 0:
                output += ", "
            output += var.toC()
        output += ", "
        output += self.expression.toC()
        return output


class ProcOrFunCall:
    def __init__(self, identifier, variables = None):
        self.identifier = identifier
        self.variables = variables

    def __str__(self):
        return f"procedure or function call: {self.identifier, self.variables}"

    def toC(self):
        if self.variables is None:
            return f"{self.identifier}();"
        else:
            return f"{self.identifier}({self.variables.toC()});"


class StatementSequence:
    def __init__(self, statement, sequence):
        self.statement = statement
        self.sequence = sequence

    def __str__(self):
        return f"statement sequence: {self.statement}; {self.sequence}"

    def toC(self):
        output = f"{self.statement.toC()}"
        for i, statement in enumerate(self.sequence):
            output += statement.toC()
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
        return f"parameter: {self.identifier}: {self.typename}"

    def toC(self):
        if self.typename == "string":
            return f"{self.typename.toC()} *{self.identifier}"
        else:
            return f"{self.typename.toC()} {self.identifier}"

class ParametersList:
    def __init__(self, parameter, p_list):
        self.parameter = parameter
        self.p_list = p_list

    def __str__(self):
        return f"parameters list: {self.parameter}: {self.p_list}"

    def toC(self):
        output = self.parameter.toC() + ", "
        for i, param in enumerate(self.p_list):
            if i != 0:
                output += ", "
            output += param.toC()
        return output


class ProcedureHeading:
    def __init__(self, identifier, parameters = None):
        self.identifier = identifier
        self.parameters = parameters

    def __str__(self):
        return f"procedure heading: {self.identifier}, {self.parameters}"

    def toC(self):
        if self.parameters is None:
            return f"void {self.identifier}()\n"
        else:
            return f"void {self.identifier}({self.parameters.toC()})\n"


class Procedure:
    def __init__(self, heading, block):
        self.heading = heading
        self.block = block

    def __str__(self):
        return f"procedure: {self.heading}; {self.block}"

    def toC(self):
        return self.heading.toC() + "{\n" + self.block.toC() + "\n}"


class FunctionHeading:
    def __init__(self, identifier, typename, params=None):
        self.identifier = identifier
        self.typename = typename
        self.params = params

    def __str__(self):
        return f"function heading: {self.identifier} ({self.params}) : {self.typename}"

    def toC(self):
        new_type = self.typename.toC()
        if self.typename == "string":
            new_type += "*"
        if self.params is None:
            return f"{new_type} {self.identifier}()\n"
        else:
            return f"{new_type} {self.identifier}({self.params.toC()})\n"


class Function:
    def __init__(self, heading, block):
        self.heading = heading
        self.block = block

    def __str__(self):
        return f"function: {self.heading}; {self.block}"

    def toC(self):
        return self.heading.toC() + "{\n" + self.block.toC() + "\n}"


class ProcedureOrFunction:
    def __init__(self, declaration, proc_or_func):
        self.declaration = declaration
        self.proc_or_func = proc_or_func

    def __str__(self):
        return f"procedure or function: {self.declaration}; {self.proc_or_func}"

    def toC(self):
        return f"{self.declaration.toC()}\n{self.proc_or_func.toC()}"

class Variable:
    def __init__(self, identifier, typename):
        self.identifier = identifier
        self.typename = typename

    def __str__(self):
        return f"variable: {self.identifier}, {self.typename}"

    def toC(self):
        if self.typename == "string":
            return f"{self.typename.toC()} *{self.identifier};"
        else:
            return f"{self.typename.toC()} {self.identifier};"


class VariableDeclarationList:
    def __init__(self, variable, varlist):
        self.variable = variable
        self.varlist = varlist

    def __str__(self):
        return f"variable list: {self.variable} {self.varlist}"

    def toC(self):
        return f"{self.variable.toC()}\n{self.varlist}"