#!/env/Scripts/python.exe
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
#

"""
Author: Jon Evans
Last Modified: July 4, 2022
"""

# Errors shown are resolved when running from main.py
from PyQt5.uic import loadUi
from src.engine import utilities
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    """
    Core functionality of the software. Most used by end user.
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.init_all_ui()

    def init_all_ui(self) -> None:
        """
        Initialize all UI elements, calling individual ui init functions
        :return: None
        """
        ui_path = utilities.get_project_ui_file('MainWindow.ui')

        if ui_path is not None:
            loadUi(ui_path, self)

        icon_path = utilities.get_resource('\\UCS_Logos\\ucs_black_small.ico')
        self.setWindowIcon(QIcon(icon_path))

        self.init_ui_voice_tab()
        self.init_ui_conflict_tab()
        self.init_ui_mic_list_tab()
        self.init_ui_wildcard_tab()
        self.init_ui_settings_tab()

    def init_ui_voice_tab(self) -> None:
        """
        Used to only initialize UI elements in the Voice tab
        :return: None
        """
        self.groupBox_UserCat.setChecked(False)
        self.groupBox_VendorCat.setChecked(False)
        self.groupBox_UserData.setChecked(False)

    def init_ui_conflict_tab(self) -> None:
        """
        Used to only initialize UI elements in the Conflict Resolution tab
        :return: None
        """
        pass

    def init_ui_mic_list_tab(self) -> None:
        """
        Used to only initialize UI elements in the Mic List tab
        :return: None
        """
        pass

    def init_ui_wildcard_tab(self) -> None:
        """
        Used to only initialize UI elements in the Wild Cards tab
        :return: None
        """
        pass

    def init_ui_settings_tab(self) -> None:
        """
        Used to only initialize UI elements in the Settings tab
        :return: None
        """
        pass
