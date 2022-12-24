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

from PySide6.QtWidgets import QApplication, QMainWindow

from qt_material import apply_stylesheet, list_themes


def set_theme(app: QApplication, theme: str, extra=None):
    """
    Apply theme to UI
    :param extra:
    :param app: The main QTApplication object
    :param theme: Theme .xml as string
    """
    if extra is None:
        extra = {}
    if isinstance(app, QApplication) and isinstance(theme, str):
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

    DEFAULT_THEME = list_themes()[2]
    DEFAULT_EXTRA = {
        'density_scale': '-2',
    }
