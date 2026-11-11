#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: November 13, 2022
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

from PySide6.QtCore import (
    Qt,
    QTimer
)
from PySide6.QtGui import (
    QFont,
    QGuiApplication
)

from PySide6.QtWidgets import QLabel


def show_splash():
    """
    Display general info about the project
    :return:
    """

    data = None
    try:

        with open('info.txt') as file:
            data = file.read()
    except EOFError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

    if data:
        splash = QLabel(f'{data}')
        splash.setFont(QFont('Arial', 12))
        splash.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        splash.setTextInteractionFlags(Qt.TextSelectableByMouse)
        rectangle = splash.frameGeometry()
        center_point = QGuiApplication.primaryScreen().availableGeometry().center()
        rectangle.moveCenter(center_point)
        splash.move(rectangle.topLeft())
        splash.show()
        QTimer.singleShot(4000, splash.destroy)
