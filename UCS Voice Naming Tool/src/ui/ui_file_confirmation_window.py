#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 27, 2022
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
    Qt
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QDialog
)
from PySide6.QtWidgets import (
    QListWidgetItem,
    QLabel
)

from src.engine import utilities
from src.engine.audio import wavfile
from src.ui.gui.FileConfirmation import Ui_Dialog

from project_info import Info


def set_wav_info_label(obj: QLabel, info_text: any, ):
    """
    Sets the text of the QLabel to the info_text if they are currently not already the same
    or if multiple info has not already been declared, as shown by '-'
    :param obj: QLabel to set text
    :param info_text: text to set
    """
    info_text = str(info_text)
    if obj.text() != info_text and obj.text() != '-':
        obj.setText(info_text)
    elif obj.text() != info_text:
        obj.setText('-')


class UIFileConfirmation(QDialog, Ui_Dialog):
    """
    .
    """

    def __init__(self, *args: object, parent=None, **kwargs: object) -> None:
        super(UIFileConfirmation, self).__init__(parent, *args, **kwargs)
        self.wav_obj_dict = None
        self.selected_wav_items = []
        self.init_all_ui()

    def init_all_ui(self) -> None:
        """
        Initialize UI window
        :return: None
        """
        self.setupUi(self)

        self.setWindowIcon(QIcon(Info.ICON_PATH))

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.listWidget_WavFileSelect.itemSelectionChanged.connect(self.set_selected_wave_file_info)
        self.show()

    def exists_qt_widgets(self) -> None:
        """
        Not used. Definition is used for testing
        :return:
        """

    def set_wav_list(self, file_list: list) -> None:
        """
        Fill the QListWidget with items from file_list
        :param file_list:
        """
        self.listWidget_WavFileSelect.clear()
        self.set_wav_objects(file_list)

        if utilities.is_list(file_list):
            for file in file_list:
                if wavfile.is_file_valid(file):
                    item = QListWidgetItem(file)
                    item.setCheckState(Qt.Checked)
                    item.setToolTip(file)
                    self.listWidget_WavFileSelect.addItem(item)

    def set_wav_objects(self, file_list: list[str]) -> None:
        """

        :param file_list:
        :return:
        """
        self.wav_obj_dict = {file: wavfile.Wav(file) for file in file_list}

    def accept(self) -> None:
        """
        Add selected files to class variable. Then accept from super
        """
        self.store_list_widget_wav_file_paths()
        super().accept()

    def store_list_widget_wav_file_paths(self) -> None:
        """
        Store all .wav file paths to self.selected_wav_items as a list
        """
        self.selected_wav_items = []
        print(self.listWidget_WavFileSelect.count())

        for index in range(self.listWidget_WavFileSelect.count()):
            item = self.listWidget_WavFileSelect.item(index)

            if item.checkState() == Qt.Checked:
                self.selected_wav_items.append(item.text())

        print(self.selected_wav_items)

    def set_selected_wave_file_info(self):
        """
        .
        """
        if self.wav_obj_dict is not None:
            self.clear_audio_info_labels()
            for item in self.listWidget_WavFileSelect.selectedItems():
                wav_obj = self.wav_obj_dict[item.text()]

                if wav_obj.sample_rate is not None and utilities.is_type(wav_obj, wavfile.Wav):
                    set_wav_info_label(self.label_SampleRate, wav_obj.sample_rate)
                    set_wav_info_label(self.label_Channels, wav_obj.channels)
                    set_wav_info_label(self.label_BitDepth, wav_obj.bit_depth)
                    set_wav_info_label(self.label_Length, wav_obj.length)

    def clear_audio_info_labels(self):
        """
        Clear all audio text in labels
        """
        self.label_SampleRate.clear()
        self.label_Channels.clear()
        self.label_BitDepth.clear()
        self.label_Length.clear()

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
