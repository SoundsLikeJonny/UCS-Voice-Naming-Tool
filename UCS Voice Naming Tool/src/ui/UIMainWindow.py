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
Last Modified: July 3, 2022
"""

# Errors shown are resolved when running
from PyQt5.uic import loadUi
from src import utilities
from PyQt5.QtWidgets import *


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
