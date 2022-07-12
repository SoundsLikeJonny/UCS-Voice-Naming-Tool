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

from PyQt5 import uic
from PyQt5.Qt import (
    QDialog
)
from PyQt5.QtCore import (
    Qt
)
from PyQt5.QtGui import (
    QIcon,
)
from PyQt5.QtWidgets import QListWidgetItem

from src.engine import utilities
from src.engine.audio import wavfile


class FileConfirmation(QDialog):
    """
    Core functionality of the software. Most used by end user.
    """

    def __init__(self, *args: object, parent=None, **kwargs: object) -> None:
        super(FileConfirmation, self).__init__(parent, *args, **kwargs)
        self.selected_wav_items = []
        self.init_all_ui()

    def init_all_ui(self) -> None:
        """
        Initialize UI window
        :return: None
        """
        ui_path = utilities.get_project_ui_file('FileConfirmation.ui')
        if ui_path is not None:
            uic.loadUi(ui_path, self)

        icon_path = utilities.get_resource('\\UCS_Logos\\ucs_black_small.ico')
        self.setWindowIcon(QIcon(icon_path))

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

    def set_wav_list(self, file_list: list) -> None:
        """
        Fill the QListWidget with items from file_list
        :param file_list:
        """
        self.listWidget_WavFileSelect.clear()

        if utilities.is_list(file_list):
            for file in file_list:
                if wavfile.is_file_valid(file):
                    item = QListWidgetItem(file)
                    item.setCheckState(Qt.Checked)
                    item.setToolTip(file)
                    self.listWidget_WavFileSelect.addItem(item)

    def accept(self) -> None:
        """
        Add selected files to class variable. Then accept from super
        """
        self.selected_wav_items = []
        for index in range(self.listWidget_WavFileSelect.count()):
            item = self.listWidget_WavFileSelect.item(index)
            if item.checkState() == Qt.Checked:
                self.selected_wav_items.append(item.text())
        super().accept()

    def get_wave_file_info(self):
        """
        .
        """
        pass

    def reject(self) -> None:
        """
        Override to ensure proper closure of window
        """
        super().reject()

    def closeEvent(self, event):
        """
        Override to ensure proper closure of window
        :param event:
        """
        self.reject()

    def close(self) -> None:
        """
        Override to ensure proper closure of window
        """
        self.reject()
