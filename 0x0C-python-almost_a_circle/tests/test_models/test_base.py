#!/usr/bin/python3
"""This is a test file.
"""
import unittest
import json
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import pycodestyle


class TestBase(unittest.TestCase):
    """Unit tests class for Base test.
    """

    def set_method(self):
        Base._Base__nb_object = 0

    def test_id(self):
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mixed(self):
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_private_attrs(self):
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r")
        self.assertEqual(file.read(), "[]")