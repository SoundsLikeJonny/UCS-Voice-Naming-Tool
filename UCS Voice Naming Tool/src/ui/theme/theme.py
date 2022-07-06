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

from __future__ import annotations
from src.engine import utilities

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet, QtStyleTools, get_theme, build_stylesheet


def set_theme(app: QApplication, theme: str, extra=None):
    """
    Apply theme to UI
    :param extra:
    :param app: The main QTApplication object
    :param theme: Theme .xml as string
    """
    if extra is None:
        extra = {}
    if utilities.is_type(app, QApplication) and utilities.is_str(theme):
        apply_stylesheet(app, theme=theme, extra=extra)


def set_default_theme(app: QApplication):
    """
    Apply default theme to UI
    :param app: The QT application
    """
    set_theme(app, Defaults.DEFAULT_THEME, extra=Defaults.DEFAULT_EXTRA)


class Defaults:
    """
    Default theme values
    """
    DEFAULT_THEME = 'dark_teal.xml'
    DEFAULT_EXTRA = {
        'density_scale': '-2',
    }

# Does not work with PyQt5
#
# class RuntimeStylesheets(QMainWindow, QtStyleTools):
#     """
#     Used to create a custom UI style .xml
#     """
#     def __init__(self):
#         super().__init__()
#
#         path = utilities.get_project_ui_file('MainWindow.ui')
#         print(path)
#         self.main = QUiLoader().load(path)
#         self.show_dock_theme(self.main)

