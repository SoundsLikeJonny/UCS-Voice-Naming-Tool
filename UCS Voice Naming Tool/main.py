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


import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication

from src.ui import generate_ui_files
from src.ui.theme import theme
from src.ui.ui_main_window import MainWindow
from src.ui.splash import show_splash
from project_info import Info


def main():
    generate_ui_files.main()

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    theme.set_default_theme(app)

    show_splash()

    app_window = MainWindow()
    app_window.show()

    quit_app = QAction("Quit")
    quit_app.triggered.connect(app.quit)
    app_window.tray.menu.addAction(quit_app)

    app_window.tray.menu_item_info.triggered.connect(show_splash)
    app_window.tray.activated.connect(app_window.show)

    app_window.tray.showMessage(Info.PROJECT_TITLE, f'Starting the application...', QIcon(Info.ICON_PATH),
                                Info.NOTIFICATION_TIME)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
