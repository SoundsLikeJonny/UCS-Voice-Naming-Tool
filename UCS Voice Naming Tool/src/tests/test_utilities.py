#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 5, 2022
"""

#  UCS Voice Naming Tool. A tool that uses voice to name audio
#  recordings according to the Universal Category System.
#
#  Copyright (C) 2022  Jon Evans
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>

import os
from unittest import TestCase
from src.engine import utilities


class Test(TestCase):
    def test_get_file(self):
        self.assertEqual(utilities.get_file(Defaults.SRC_PATH+Defaults.FILE), Defaults.FULL_PATH)
        self.assertIsNone(utilities.get_file(Defaults.SRC_PATH))
        self.assertIsNone(utilities.get_file(''))
        self.assertIsNone(utilities.get_file(0))
        self.assertIsNone(utilities.get_file(None))
        self.assertIsNone(utilities.get_file(True))

    def test_get_resource(self):
        self.assertEqual(utilities.get_resource(Defaults.RESOURCE), Defaults.RESOURCES_FULL_PATH)
        self.assertIsNone(utilities.get_resource(Defaults.RESOURCES_PATH))
        self.assertIsNone(utilities.get_resource(None))
        self.assertIsNone(utilities.get_resource(False))
        self.assertIsNone(utilities.get_resource(''))
        self.assertIsNone(utilities.get_resource(0))

    def test_get_project_ui_file(self):
        self.assertEqual(utilities.get_project_ui_file(Defaults.GUI_DOC_FILE), Defaults.GUI_DOC_FULL_PATH)
        self.assertIsNone(utilities.get_project_ui_file(Defaults.RESOURCES_PATH))
        self.assertIsNone(utilities.get_project_ui_file(''))
        self.assertIsNone(utilities.get_project_ui_file(0))
        self.assertIsNone(utilities.get_project_ui_file(None))
        self.assertIsNone(utilities.get_project_ui_file(True))

    def test_is_type(self):
        self.assertTrue(utilities.is_type(0, int), True)
        self.assertFalse(utilities.is_type('', int), False)
        self.assertTrue(utilities.is_type(None, type(None)), True)
        self.assertFalse(utilities.is_type(None, None), False)
        self.assertTrue(utilities.is_type('', str), True)
        self.assertFalse(utilities.is_type(0, str), False)
        self.assertTrue(utilities.is_type([], list), True)
        self.assertFalse(utilities.is_type([], str), False)
        self.assertTrue(utilities.is_type({}, dict), True)
        self.assertFalse(utilities.is_type([], dict), False)
        self.assertTrue(utilities.is_type(set(), type(set())), True)
        self.assertFalse(utilities.is_type(set(), set()), False)

    def test_is_str(self):
        self.assertTrue(utilities.is_str(''), True)
        self.assertTrue(utilities.is_str('Hello!'), True)
        self.assertFalse(utilities.is_str([]), False)
        self.assertFalse(utilities.is_str(None), False)
        self.assertFalse(utilities.is_str({}), False)
        self.assertFalse(utilities.is_str(set()), False)
        self.assertFalse(utilities.is_str(0), False)
        self.assertFalse(utilities.is_str(True), False)

    def test_is_int(self):
        self.assertTrue(utilities.is_int(0), True)
        self.assertFalse(utilities.is_int(''), False)
        self.assertFalse(utilities.is_int('Hello!'), False)
        self.assertFalse(utilities.is_int([]), False)
        self.assertFalse(utilities.is_int(None), False)
        self.assertFalse(utilities.is_int({}), False)
        self.assertFalse(utilities.is_int(set()), False)
        self.assertFalse(utilities.is_int(True), False)

    def test_is_list(self):
        self.assertTrue(utilities.is_list([]), True)
        self.assertFalse(utilities.is_list({}), False)
        self.assertFalse(utilities.is_list(0), False)
        self.assertFalse(utilities.is_list(''), False)
        self.assertFalse(utilities.is_list('Hello!'), False)
        self.assertFalse(utilities.is_list(None), False)
        self.assertFalse(utilities.is_list(set()), False)
        self.assertFalse(utilities.is_list(True), False)

    def test_is_dict(self):
        self.assertTrue(utilities.is_dict({}), True)
        self.assertFalse(utilities.is_dict([]), False)
        self.assertFalse(utilities.is_dict(0), False)
        self.assertFalse(utilities.is_dict(''), False)
        self.assertFalse(utilities.is_dict('Hello!'), False)
        self.assertFalse(utilities.is_dict(None), False)
        self.assertFalse(utilities.is_dict(set()), False)
        self.assertFalse(utilities.is_dict(True), False)


class Defaults:
    """
    Default testing values
    """
    FULL_PATH = f'{os.getcwd()}\\src\\engine\\utilities.py'
    SRC_PATH = '\\src\\engine\\'
    FILE = 'utilities.py'
    RESOURCES_FULL_PATH = f'{os.getcwd()}\\resources\\UCS_Logos\\ucs_black_small.ico'
    RESOURCES_PATH = '\\resources'
    RESOURCE = '\\UCS_Logos\\ucs_black_small.ico'
    GUI_DOC_FULL_PATH = f'{os.getcwd()}\\src\\ui\\gui\\MainWindow.ui'
    GUI_DOC_FILE = 'MainWindow.ui'
