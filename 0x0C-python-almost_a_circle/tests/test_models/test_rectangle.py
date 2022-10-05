#!/usr/bin/python3
"""This is a test file.
"""
import unittest
import os
import pycodestyle
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """Tests for class Rectangle.
    """
    def set_method(self):
        Base._Base__nb_objects = 0

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id_default(self):
        self.set_method()
        r1 = Rectangle(10, 2)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        r2.id = 2
        self.assertEqual(r2.id, 2)

    def test_rectangle_instance(self):
        r = Rectangle(5, 4, 2, 6, 27)
        self.assertEqual(type(r), Rectangle)
        self.assertTrue(type(r) == Rectangle)
        self.assertFalse(type(r) == Base)

    def test_given_id(self):
        r3 = Rectangle(10, 4, 5, 3, 30)
        self.assertEqual(r3.id, 30)

    def test_wrong_arguments(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(5)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 3, 5, 6, 8, 33)

    def test_correct_set_attr(self):
        r = Rectangle(10, 5, 1, 2, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 12)

    def test_width_height(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(10, 2)
            r3.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(10, 4)
            r4.height = -10

    def test_x_and_y(self):
        self.set_method()
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5 = Rectangle(10, 2, 4, -5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5 = Rectangle(10, 2, -4, -5)

    def test_private(self):
        self.set_method()
        r6 = Rectangle(10, 2, 3, 1)
        self.assertEqual(r6.x, 3)
        with self.assertRaises(AttributeError):
            r6.__x

    def test_area(self):
        self.set_method()
        r1 = Rectangl(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 5
        self.assertEqual(r1.area(), 10)

    def display_rectangle(self):
        r1 = Rectangle(3, 3)
        with patch('sys.stdout', new=StringIO()) as draw12:
            self.assertEqual(draw12.getvalue(), "###\n###\n###\n")

    def display_line(self):
        r2 = Rectangle(3, 1)
        with patch('sys.stdout', new=StringIO()) as draw12:
            self.assertEqual(draw12.getvalue(), "###\n")

    def check_correct_print(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_result = "[Rectangle] (12) 2/1 - 4/6"
        with patch('sys.stdout', new=StringIO()) as string12:
            self.assertEqual(string12.getvalue(), r1_result)
        r2 = Rectangle(5, 5, 1)
        r2_result = "[Rectangle] (1) 1/0 - 5/5"
        with patch('sys.stdout', new=StringIO()) as string 12:
            self.assertEqual(string12.getvalue(), r2_result)

    def test_invalid_attrs(self):
        self.set_nb_to_zero()
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 1, -2)
            r1.display()

    def test_with_args(self):
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        with self.assertRaises(TypeError):
            r1.display(1)
