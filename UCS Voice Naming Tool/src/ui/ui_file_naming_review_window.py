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
from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtCore import (
    Qt
)

from PySide6.QtWidgets import (
    QDialog,
    QTableWidgetItem, QVBoxLayout, QWidget
)

from project_info import Info
from src.engine.stt.speechanalyse import SpeechAnalyse
from src.ui.gui.FileNamingReview import Ui_Dialog
from src.ui.gui import ReviewFileInfo


class UIFileNamingReview(QDialog, Ui_Dialog):
    """
    Window for confirming the naming of files
    """

    def __init__(self, *args: object, parent=None, **kwargs: object) -> None:
        super(UIFileNamingReview, self).__init__(*args, parent=parent, **kwargs)
        self.frame4 = None
        self.frame3 = None
        self.frame2 = None
        self.frame1 = None
        self.frame = None
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
        self.stackedWidget.setCurrentIndex(1)

        """
        Checkboxes
        """
        self.checkBox_switch_views.toggled.connect(self.update_views)

        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        # self.listWidget_WavFileSelect.itemSelectionChanged.connect(self.set_selected_wave_file_info)

        self.show()

    def update_table(self, speech_data: list[SpeechAnalyse]) -> None:
        """

        :param speech_data:
        """
        self.tableWidget.clear()
        self.tableWidget.verticalHeader().setVisible(False)
        layout = QVBoxLayout()

        for index, speech_item in enumerate(speech_data):
            self.tableWidget.insertRow(index)
            self.tableWidget.setItem(index, 0, QTableWidgetItem(speech_item.wav.file_path))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(speech_item.speech_transcription_from_file))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(speech_item.silence_threshold))
            # self.tableWidget.setItem(index, 2, QTableWidgetItem("text3"))

            frame = UIReviewFileInfo()
            frame.label_description.setText(speech_item.speech_transcription_from_file)
            frame.label_file.setText(speech_item.wav.file_path)
            template = frame.frame_main

            layout.insertWidget(layout.count(), template)

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        self.scrollArea1.setWidget(scroll_widget)
        self.tableWidget.resizeColumnsToContents()

    def update_views(self) -> None:
        """
        Change the view to box or table
        """
        if self.checkBox_switch_views.isChecked():
            return self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)

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


class UIReviewFileInfo(QWidget, ReviewFileInfo.Ui_Frame_window):
    """
    Single widget for displaying STT and UCS information to the user.
    """

    def __init__(self):
        super(UIReviewFileInfo, self).__init__()
        self.setupUi(self)
