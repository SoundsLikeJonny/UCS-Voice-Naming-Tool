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
from unittest import TestCase

from PyQt5.QtWidgets import QApplication

from src.ui.theme import theme
from src.ui.ui_main_window import MainWindow


class TestMainWindow(TestCase):

    def setUp(self) -> None:
        self.app = QApplication(sys.argv)
        theme.set_default_theme(self.app)
        self.obj = MainWindow()

    def tearDown(self) -> None:
        self.app.exit()

    def test_init_ui_voice_tab(self) -> None:
        self.assertFalse(self.obj.groupBox_UserCat.isChecked(), False)
        self.assertFalse(self.obj.groupBox_VendorCat.isChecked(), False)
        self.assertFalse(self.obj.groupBox_UserData.isChecked(), False)

    def test_init_ui_conflict_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_conflict_tab(), True)

    def test_init_ui_mic_list_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_mic_list_tab(), True)

    def test_init_ui_wildcard_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_wildcard_tab(), True)

    def test_init_ui_settings_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_settings_tab(), True)
