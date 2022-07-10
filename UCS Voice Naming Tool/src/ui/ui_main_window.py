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

from PyQt5 import uic
from PyQt5.Qt import (
    QMainWindow
)
from PyQt5.QtGui import (
    QIcon,
    QDragEnterEvent,
    QDrag,
    QMouseEvent,
    QDropEvent,

)
from PyQt5.QtCore import (
    Qt,
    QMimeData
)

from src.engine import utilities


class MainWindow(QMainWindow):
    """
    Core functionality of the software. Most used by end user.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.init_all_ui()

    def init_all_ui(self) -> None:
        """
        Initialize all UI elements, calling individual ui init functions
        :return: None
        """
        ui_path = utilities.get_project_ui_file('MainWindow.ui')

        if ui_path is not None:
            uic.loadUi(ui_path, self)

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
        # self.label_DragDrop.set

    def init_ui_conflict_tab(self) -> None:
        """
        Used to only initialize UI elements in the Conflict Resolution tab
        :return: None
        """
        # Remove this when more in function. Then resolve in tests
        # noinspection PyTypeChecker
        return True

    def init_ui_mic_list_tab(self) -> None:
        """
        Used to only initialize UI elements in the Mic List tab
        :return: None
        """
        # Remove this when more in function. Then resolve in tests
        # noinspection PyTypeChecker
        return True

    def init_ui_wildcard_tab(self) -> None:
        """
        Used to only initialize UI elements in the Wild Cards tab
        :return: None
        """
        # Remove this when more in function. Then resolve in tests
        # noinspection PyTypeChecker
        return True

    def init_ui_settings_tab(self) -> None:
        """
        Used to only initialize UI elements in the Settings tab
        :return: None
        """
        # Remove this when more in function. Then resolve in tests
        # noinspection PyTypeChecker
        return True

    # def dragEnterEvent(self, data: QDragEnterEvent) -> None:
    #     """
    #     Accept incoming audio files
    #     :param data:
    #     """
    #     print(data.type())
    #     data.accept()

    # def mouseMoveEvent(self, data: QMouseEvent) -> None:
    #     """
    #
    #     :param data:
    #     """
    #     data.accept()
    #     print(data.type())

    def mousePressEvent(self, event):
        print(str(type(event)))
        if event.button() == Qt.LeftButton and self.label_DragDrop.geometry().contains(event.pos()):
            print(event.type())
            drag = QDrag(self)
            # mimeData = QMimeData()
            # mimeData.setText(self.label_DragDrop.toPlainText())
            # drag.setMimeData(mimeData)

            # Qt.DropAction.dropAction = drag.exec()

    # def dropEvent(self, data: QDropEvent) -> None:
    #     print(data.type())
    #     data.accept()
