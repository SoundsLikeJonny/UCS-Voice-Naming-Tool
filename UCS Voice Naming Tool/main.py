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

from PyQt5.QtWidgets import QApplication

from src.ui.theme import theme
from src.ui.ui_main_window import MainWindow

app = QApplication(sys.argv)
theme.set_default_theme(app)

obj = MainWindow()
obj.show()

sys.exit(app.exec_())
