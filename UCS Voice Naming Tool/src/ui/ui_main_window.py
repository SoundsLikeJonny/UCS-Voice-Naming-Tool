#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 11, 2022
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
import PyQt5
from PyQt5 import uic
from PyQt5.Qt import (
    QMainWindow
)
from PyQt5.QtGui import (
    QIcon,
)
from PyQt5.QtWidgets import QDialog

from src.engine import utilities
from src.ui.ui_file_confirmation_window import FileConfirmation


class MainWindow(QMainWindow):
    """
    Core functionality of the software. Most used by end user.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.file_confirmation_window = None
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

        self.setMouseTracking(True)
        self.setAcceptDrops(True)

        self.file_confirmation_window = None

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

    def dropEvent(self, event: PyQt5.QtGui.QDropEvent) -> None:
        """
        Override QT drop event
        :param event:
        """
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if not self.checkBox_SkipFileSelection.checkState():
            self.open_file_confirmation_window(files)
        else:
            self.analyze_stt(files)

    def open_file_confirmation_window(self, file_list: list):
        """
        Create FileConfirmation window with items from file_list
        :param file_list:
        """
        if self.file_confirmation_window is None:
            self.file_confirmation_window = FileConfirmation(parent=self)
            self.file_confirmation_window.show()
            self.file_confirmation_window.set_wav_list(file_list)
            self.file_confirmation_window.buttonBox.rejected.connect(self.reset_file_confirmation_window)
            self.file_confirmation_window.destroyed.connect(self.reset_file_confirmation_window)
            self.file_confirmation_window.buttonBox.accepted.connect(self.file_confirmation_window_analyze_stt)

    def dragEnterEvent(self, event: PyQt5.QtGui.QDragEnterEvent) -> None:
        """
        Set drag and drop to only handle urls
        :param event:
        """
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def reset_file_confirmation_window(self):
        """
        Reset window object back to None. Used to ensure that only one FileConfirmation window is made
        """
        self.file_confirmation_window = None

    def file_confirmation_window_analyze_stt(self):
        """
        If the window exists, get the files to analyse
        """
        if self.file_confirmation_window is not None:
            files = self.file_confirmation_window.selected_wav_items
            self.analyze_stt(files)

    def analyze_stt(self, files=None):
        """
        Hand off to STT engine to handle processing of speech
        :param files:
        """
        if not utilities.is_type(self.file_confirmation_window, QDialog):
            self.reset_file_confirmation_window()

        if files:
            print("printing files")

        #
        # def eventFilter(self, source, event):
        #
        #     if self.frame_DragDrop.underMouse():
        #         self.frame_DragDrop.setStyleSheet("color: rgb(255, 255, 0);")
        #         print("Mouse")
        #
        #     else:
        #         self.frame_DragDrop.setStyleSheet("")
        #         print("setStyleSheet("")")

        # def mousePressEvent(self, event):
        #     if event.button() == Qt.LeftButton and self.label_DragDrop.geometry().contains(event.pos()):
        #         print(event.type())
        #         drag = QDrag(self)
        #         # mimeData = QMimeData()
        #         # mimeData.setText(self.label_DragDrop.toPlainText())
        #         # drag.setMimeData(mimeData)

        # pixmap = QPixmap(self.size())
        # self.render(pixmap)
        # drag.setPixmap(pixmap)
        #
        # drag.exec_(Qt.MoveAction)
