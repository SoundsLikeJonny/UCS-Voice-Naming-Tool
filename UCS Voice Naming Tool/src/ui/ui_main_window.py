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
import PySide6
from PySide6.QtCore import (
    QRunnable
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox
)
from PySide6.QtWidgets import (
    QMainWindow
)

from src.engine import utilities
from src.engine.stt.speechread import SpeechRead
from src.ui.gui.MainWindow import Ui_MainWindow
from src.ui.ui_file_confirmation_window import FileConfirmation


class MainWindow(QMainWindow, Ui_MainWindow):
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

        self.setupUi(self)

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

    def exists_qt_widgets(self) -> bool:
        """
        Not used. Definition is used for testing
        :return:
        """
        self.groupBox_UserCat
        self.groupBox_VendorCat
        self.groupBox_UserData
        return True

    def init_ui_voice_tab(self) -> None:
        """
        Used to only initialize UI elements in the Voice tab
        :return: None
        """
        self.groupBox_UserCat.setChecked(False)
        self.groupBox_VendorCat.setChecked(False)
        self.groupBox_UserData.setChecked(False)
        pass
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

    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        """
        Override QT drop event
        :param event:
        """
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.handle_drop_event_files(files)

    def handle_drop_event_files(self, files: list):
        """
        Passes the files to the appropriate function
        :param files:
        """
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

    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent) -> None:
        """
        Set drag and drop to only handle urls
        :param event:
        """
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def reset_file_confirmation_window(self) -> None:
        """
        Reset window object back to None. Used to ensure that only one FileConfirmation window is made
        """
        self.file_confirmation_window = None

    def file_confirmation_window_analyze_stt(self) -> None:
        """
        If the window exists, get the files to analyse
        """
        if self.file_confirmation_window is not None:
            files = self.file_confirmation_window.selected_wav_items
            self.analyze_stt(files)
            self.reset_window()

    def analyze_stt(self, files=None) -> None:
        """
        Hand off to STT engine to handle processing of speech
        :param files:
        """
        if utilities.is_list(files) and files:
            sr = SpeechRead(files[0])
            sr.get_transcription_from_wav_file_google()
            QMessageBox.about(self, "Speech-To-Text File Results", sr.speech_transcription_from_file)

    def reset_window(self):
        """
        Reset the
        :return: 
        """
        if not utilities.is_type(self.file_confirmation_window, QDialog):
            self.reset_file_confirmation_window()


class Worker(QRunnable):

    def __init__(self):
        super().__init__()

# TODO: continue setting up the worker
# class WorkerSignals(QO)
