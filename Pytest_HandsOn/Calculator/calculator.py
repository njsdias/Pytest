import numbers
import sys
class CalculatorError(Exception):
    """ An exception class for Calculator"""

class Calculator:  # class have methods, is a way to group a data and keep a behavior
    """
    A terrible calculator
    """

#    def add_old(self, a, b):  # this function it in fact a method because is in a class and
#        try:
#            return a + b      # for this we need pass the self argument
#        except TypeError:
#            raise CalculatorError("Enter a number not a string")

    def add(self, a, b):
        self._check_operand(a)   # this will be used by test_add_weird and test_add_weirder
        self._check_operand(b)   # this will be used by test_add_weird and test_add_weirder
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
               raise CalculatorError("can't divide by zero!")

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number')

# If you run this python file this all things will be run. It is what means the next line of code.

if __name__ == '__main__':
    print("Let's calculate!")
    calculator = Calculator()
    operations = [ calculator.add,
                   calculator.subtract,
                   calculator.multiply,
                   calculator.divide ]
    while True:
        for i, operation in enumerate(operations, start = 1):
            print(f"{i}: {operation.__name__}")

        print("q: quit")
        operation = input("Pick and operation: ")
        if operation == "q" :
            sys.exit()
        op = int(operation)
        a = float(input("What is a? "))
        b = float(input("What is b? "))
        # for not break the system
        try:
            print(operations[op - 1](a, b))
        except CalculatorError as ex:
            print(ex)

