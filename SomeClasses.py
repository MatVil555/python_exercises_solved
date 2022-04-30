# Task 8--
import numpy as np
from Utils import InvalidOperationException, EvenStream, OddStream

class Rectangle:
    def __init__(self,altezza,base):
        self.altezza=altezza
        self.base=base

    def area(self):
        return self.altezza*self.base


class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2*np.pi


# Task 9--
class Product:
    def __init__(self,name_product,cost_product):
        self.name_product=name_product
        self.cost_product=cost_product

    def __str__(self):
        return f'{self.name_product} costs {self.cost_product} euro(s)'

# Task 10
class PhoneBook:
    empty_book = {}
    def __init__(self):
        self.dict_number = self.empty_book

    def add_number(self, name, number):
        if name in self.dict_number.keys():
            raise InvalidOperationException
        else:
            self.dict_number[str(name)] = number
            return self.dict_number

        """
        try:
            flag=1 if name in self.dict_number.keys() else InvalidOperationException
            raise InvalidOperationException()
        except name in self.dict_number.keys():
            self.dict_number[str(name)] = number
            InvalidOperationException()
        """

        """
       Add a contact or throw InvalidOperationException if it is already present
        :param number: an integer number
        :param name: a string
       """


    def del_number(self, name):
        if name not in self.dict_number.keys():
            raise InvalidOperationException
        else:
            self.dict_number.pop(name)
            return self.dict_number

        """
        Delete a contact or throw InvalidOperationException if it is not present
        :param name: a string
        """
    def size(self):
        return len(self.dict_number.keys())

        """
        :return: current size of PhoneBook
        """


    def get_all(self):
        output=''
        for name in sorted(self.dict_number.keys()):
           output += f'{name}: {self.dict_number[name]}; '
        return output[:-2]
        """
        return: a string representation of all entries in the format 'name: number',
        merged and separated by ';' and a space. The entries should be sorted alphabetically
        """


