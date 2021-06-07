class Program:
    def __init__(self, identifier, block):
        self.identifier = identifier
        self.block = block

    def __str__(self):
        return "program " + self.identifier

    def toC(self):
        converted_statement = "#include <stdio.h> \n \n int main(void){"


class Block:
    def __init__(self, variable_declaration_part, procedure_or_function, compound_statement):
        self.variable_declaration_part = variable_declaration_part
        self.procedure_or_function = procedure_or_function
        self.compound_statement = compound_statement

    def __str__(self):
        return "block: " + self.variable_declaration_part + ", " + self.procedure_or_function + ", " + self.compound_statement

    def toC(self):
        return


class FunctionCall:
    def __init__(self, identifier, variables_list):
        self.variables_list = variables_list
        self.identifier = identifier

    def __str__(self):
        return f"function_call: {self.identifier}({self.variables_list});"

    def toC(self):
        return f"{self.identifier}({self.variables_list.toC});"


class Element:
    def __init__(self, element):
        self.element = element

    def __str__(self):
        return f"element: {self.element}"

    def toC(self):
        return f""


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
        return f"{self.expr1} {self.sign} {self.expr2}"


class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return f"assignment: {self.identifier} := {self.expression}"

    def toC(self):
        return f"{self.identifier} = {self.expression};"


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
            return f"for({self.assignment.toC()} ; {self.assignment.identifier} <= {self.assignment.expression} ; {self.assignment.identifier}++)" + "{ \n" + self.statement + "\n}"


class Repeat:
    def __init__(self, statement, expression):
        self.statement = statement
        self.expression = expression

    def __str__(self):
        return f"repeat: repeat {self.statement} until {self.expression}"

    def toC(self):
        return "do { \n" + self.statement + "\n } while(" + self.expression + ")"




