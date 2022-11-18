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

from PySide6.QtGui import (
    QIcon,
    QAction
)
from PySide6.QtWidgets import (
    QSystemTrayIcon,
    QMenu
)

from project_info import Info


class SysTray(QSystemTrayIcon):
    """
    Sets up basic system tray commands
    """

    def __init__(self, *args):
        super(SysTray, self).__init__(*args)

        self.setIcon(QIcon(Info.ICON_PATH))
        self.setVisible(True)
        self.setToolTip(Info.PROJECT_TITLE)

        self.menu = QMenu()
        self.menu_item_info = QAction("Info")
        self.menu.addAction(self.menu_item_info)

        self.setContextMenu(self.menu)
