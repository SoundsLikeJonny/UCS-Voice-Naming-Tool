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

from unittest import TestCase
# From venv
import sys
from PyQt5.QtWidgets import QApplication

# From project
from src.ui.UIMainWindow import MainWindow
from src.ui.theme import theme


class TestMainWindow(TestCase):

    def test_init_ui_voice_tab(self) -> None:
        app = QApplication(sys.argv)
        theme.set_default_theme(app)
        obj = MainWindow()
        obj.show()
        self.assertFalse(obj.groupBox_UserCat.isChecked(), False)
        self.assertFalse(obj.groupBox_VendorCat.isChecked(), False)
        self.assertFalse(obj.groupBox_UserData.isChecked(), False)
        app.exit()

    def test_init_ui_conflict_tab(self) -> None:
        app = QApplication(sys.argv)
        theme.set_default_theme(app)
        obj = MainWindow()
        obj.show()
        self.assertTrue(obj.init_ui_conflict_tab(), True)
        app.exit()

    def test_init_ui_mic_list_tab(self) -> None:
        app = QApplication(sys.argv)
        theme.set_default_theme(app)
        obj = MainWindow()
        obj.show()
        self.assertTrue(obj.init_ui_mic_list_tab(), True)
        app.exit()

    def test_init_ui_wildcard_tab(self) -> None:
        app = QApplication(sys.argv)
        theme.set_default_theme(app)
        obj = MainWindow()
        obj.show()
        self.assertTrue(obj.init_ui_wildcard_tab(), True)
        app.exit()

    def test_init_ui_settings_tab(self) -> None:
        app = QApplication(sys.argv)
        theme.set_default_theme(app)
        obj = MainWindow()
        obj.show()
        self.assertTrue(obj.init_ui_settings_tab(), True)
        app.exit()
