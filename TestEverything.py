import math

import numpy as np
import pytest
import unittest
from BasicFunctions import *
from MoreFunctions import *
from SomeClasses import *
from Utils import InvalidOperationException, EvenStream, OddStream


class BaseTests(unittest.TestCase):

    # Task 1
    def test_average(self):
        self.assertAlmostEqual(1.5, average(1, 2))
        self.assertAlmostEqual(0, average(1, -1))

    # Task 2
    def test_reverse_list(self):
        self.assertEqual([5, 4, 3, 2, 1], reverse_list([1, 2, 3, 4, 5]))
        self.assertEqual(['b', 'a'], reverse_list(['a', 'b']))
        self.assertEqual([1], reverse_list([1]))
        self.assertEqual([[1], [2, 3], [4]], reverse_list([[4], [2, 3], [1]]))

    # Task 3
    def test_sort_numbers(self):
        self.assertEqual([5, 4, 3, 2, 1], sort_numbers_descending([5, 3, 2, 1, 4]))
        self.assertEqual([3.14, 2.71, -1], sort_numbers_descending([2.71, 3.14, -1]))

    # Task 4
    def test_add_indices(self):
        self.assertEquals(["1. A", "2. B", "3. C", "4. D"], add_indices(["A", "B", "C", "D"]))
        self.assertEquals(["1. one", "2. two", "3. three"], add_indices(["one", "two", "three"]))
        self.assertEquals(["1. IT"], add_indices(["IT"]))

    # Task 5
    def test_capitalize_last_letters(self):
        self.assertEquals("johN lemoN", capitalize_last_letter_in_each_word("john lemon"))
        self.assertEquals("VincenT vaN CoC", capitalize_last_letter_in_each_word("Vincent van Coc"))
        self.assertEquals("ABC deF ghI KLM", capitalize_last_letter_in_each_word("ABC def ghI KLm"))
        self.assertEquals("thE quicK browN foX jumpS oveR thE lazY doG",
                          capitalize_last_letter_in_each_word("the quick brown fox jumps over the lazy dog"))

    # Task 6
    def test_element_wise_merge(self):
        self.assertEquals(
            ["Leonardo da Vinci", "Michelangelo Buonarroti", "Raffaello Sanzio"],
            element_wise_merge(["Leonardo", "Michelangelo", "Raffaello"], ["da Vinci", "Buonarroti", "Sanzio"]))
        self.assertEquals(
            ["am ba", "ra ba", "ci ci", "co co"],
            element_wise_merge(["am", "ra", "ci", "co"], ["ba", "ba", "ci", "co"]))

    # Task 7
    def test_execute_safely(self):
        self.assertAlmostEqual(5, execute_safely(lambda x, y: x + y, 2, 3))
        self.assertAlmostEqual(6, execute_safely(lambda x, y: x * y, 2, 3))
        self.assertAlmostEqual(5, execute_safely(lambda x, y: x / y, 10, 2))
        self.assertAlmostEqual(-1, execute_safely(lambda x, y: x / y, 1, 0))
        self.assertAlmostEqual(-1, execute_safely(lambda x, y: math.pow(x, y), -1, 0.5))

    # Task 8
    def test_area(self):
        rectangle = Rectangle(3, 4)  # 3 x 4 rectangle
        self.assertAlmostEqual(12, rectangle.area())
        circle = Circle(2)  # circle with radius r=2
        self.assertAlmostEqual(12.566370614359172953850573533118, circle.area())

    # Task 9
    def test_items(self):
        product_1 = Product("coffee", 1)
        product_2 = Product('car', 20000)
        product_3 = Product('book', 15)
        self.assertEqual("coffee costs 1 euro(s)", str(product_1))
        self.assertEqual("car costs 20000 euro(s)", str(product_2))
        self.assertEqual("book costs 15 euro(s)", str(product_3))

    # Task 10
    def test_phone_book(self):
        phone_book = PhoneBook()
        self.assertEqual(0, phone_book.size())
        phone_book.add_number("Emergenza", 112)
        phone_book.add_number("Polizia", 113)
        phone_book.add_number("Vigili del fuoco", 115)
        phone_book.add_number("Pronto soccorso", 118)
        self.assertEqual(4, phone_book.size())
        phone_book.del_number("Polizia")
        self.assertEqual(3, phone_book.size())

        with pytest.raises(InvalidOperationException):
            phone_book.del_number("Guardia finanza")

        with pytest.raises(InvalidOperationException):
            phone_book.add_number("Emergenza", 999)

        self.assertEqual("Emergenza: 112; Pronto soccorso: 118; Vigili del fuoco: 115", phone_book.get_all())


class FurtherTests(unittest.TestCase):

    # Task 11
    def test_calculate_cost(self):
        self.assertAlmostEqual(1.45, round(calculate_cost(60), 2))
        self.assertAlmostEqual(2.90, round(calculate_cost(120), 2))
        self.assertAlmostEqual(5.37, round(calculate_cost(222), 2))

    # Task 12
    def test_streams(self):
        self.assertEquals([1, 3, 5], print_from_stream(3, stream=OddStream()))
        self.assertEquals([0, 2, 4], print_from_stream(3, stream=EvenStream()))
        self.assertEquals([0, 2, 4], print_from_stream(3))

        self.assertEquals([1, 3, 5, 7], print_from_stream(4, stream=OddStream()))
        self.assertEquals([0, 2, 4, 6], print_from_stream(4, stream=EvenStream()))
        self.assertEquals([0, 2, 4, 6], print_from_stream(4))


if __name__ == '__main__':
    unittest.main()
