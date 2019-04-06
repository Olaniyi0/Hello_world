'''
    Started on 26/03/2019 by me
'''
import math


class Calculator:
    """This is a basic calculator"""
    def __init__(self):
        pass


    def addition(self, *add):
        """This method takes in as many as possible numbers and add it together"""

        add_container = 0
        for num in add:
            add_container += num
        print(add_container)


    def multiplication(self, *multiply):
        """This method takes in as many as possible numbers and multiply it together"""

        multi_container = 1
        for num in multiply:
            multi_container *= num
        print(multi_container)


    def subtraction(self, *subtract):
        """This method takes in as many as possible numbers and subtract it from one another"""

        sub_holder = [num for num in subtract]
        sub_container = sub_holder[0]
        for num in subtract:
            if num == subtract[0]:
                continue
            sub_container -= num
        print(sub_container)


    def division(self, *divide):
        """This method takes in as many as possible numbers and divide it by each other"""

        div_holder = [num for num in divide]
        div_container = div_holder[0]
        for num in divide:
            if num == divide[0]:
                continue
            div_container /= num
        print(div_container)


    def square_root(self, root):
        """This method takes in a number and returns it square root"""
        print(math.sqrt(root))

    def binary(self, a):
        """This function converts decimal number to binary"""
        print("{0:b}".format(a))

    def hexadecimal(self, b):
        print("{0:x}".format(b))

    def octal(self, c):
        print("{0:o}".format(c))

    def raise_to_power(self, a, b):
        print(a**b)

result = Calculator()
result.