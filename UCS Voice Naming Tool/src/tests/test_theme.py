#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 6, 2022
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
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import unittest

from PySide6.QtWidgets import QApplication
from qt_material import build_stylesheet

from src.ui.theme import theme


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.app = QApplication(sys.argv)

    def tearDown(self) -> None:
        self.app.exit()

    def test_set_theme(self) -> None:
        # Test same
        theme.set_theme(self.app, 'dark_teal.xml')
        stylesheet = build_stylesheet('dark_teal.xml')
        self.assertEqual(self.app.styleSheet(), stylesheet)
        # Test different
        theme.set_theme(self.app, 'dark_teal.xml')
        stylesheet = build_stylesheet('dark_blue.xml')
        self.assertNotEqual(self.app.styleSheet(), stylesheet)

    def test_set_default_theme(self) -> None:
        theme.set_theme(self.app, theme.Defaults.DEFAULT_THEME)
        stylesheet = build_stylesheet(theme.Defaults.DEFAULT_THEME)
        self.assertEqual(self.app.styleSheet(), stylesheet)
        theme.set_theme(self.app, 'dark_teal.xml')
        stylesheet = build_stylesheet('dark_blue.xml')
        self.assertNotEqual(self.app.styleSheet(), stylesheet)
