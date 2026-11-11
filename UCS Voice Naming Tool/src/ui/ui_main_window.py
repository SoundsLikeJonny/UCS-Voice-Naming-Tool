#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: Nov 24, 2022
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
    QRunnable, Qt
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
    QFileDialog,
    QMainWindow,
    QGraphicsOpacityEffect,
    QWidget, QGroupBox
)

from src.engine import utilities
from src.engine.stt.speechanalyse import SpeechAnalyse
from src.engine.ucs import ucs_data
from src.ui.gui.MainWindow import Ui_MainWindow
from src.ui.ui_file_confirmation_window import UIFileConfirmation
from src.ui.ui_file_naming_review_window import UIFileNamingReview
from src.ui.ui_progress_window import ProgressWindow
from src.ui.systray import SysTray

from project_info import Info


def set_groupbox_title_white(widget: QGroupBox):
    """
    Set the groupbox color to white
    :param widget:
    """
    widget.setStyleSheet("QGroupBox::title {color: white} QGroupBox {border:0}")

    # widget.setStyleSheet('')


def set_groupbox_title_grey(widget: QGroupBox):
    """
    Set the groupbox color to grey
    :param widget:
    """
    widget.setStyleSheet("QGroupBox::title {color: grey} QGroupBox {border:0}")


def set_groupbox_no_border(widget: QGroupBox):
    """
    Set the groupbox color to grey
    :param widget:
    """
    widget.setStyleSheet('QGroupBox {border:0}')


def toggle_groupbox_colors(widget: QGroupBox):
    """
    Switch title between white and grey if the checkboxes are selected
    :param widget:
    :return:
    """
    if widget.isCheckable():
        if widget.isChecked():
            set_groupbox_title_white(widget)
        else:
            set_groupbox_title_grey(widget)


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Core functionality of the software. Most used by end user.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        # progress_window = ProgressWindow(parent=self)
        self.setupUi(self)
        self.tray = SysTray()

        # list of parent widgets that contain QGroupBox widgets as children
        # These will be looped over to apply signals
        self.groupbox_parent_widgets = [
            self.widget_Naming,
            self.widget_AnalysisPrefs
        ]

        self.opacity = None
        self.file_confirmation_window = None
        self.file_naming_review_window = None

        self.ucs = ucs_data.UCS()
        self.init_all_ui()

    def init_all_ui(self) -> None:
        """
        Initialize all UI elements, calling individual ui init functions
        :return: None
        """

        self.setWindowIcon(QIcon(Info.ICON_PATH))

        self.setMouseTracking(True)
        self.setAcceptDrops(True)

        self.tabWidget_Main.setCurrentIndex(0)
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
        # self.groupBox_UserCat
        # self.groupBox_VendorCat
        # self.groupBox_UserData
        return True

    def init_ui_voice_tab(self) -> None:
        """
        Used to only initialize UI elements in the Voice tab
        :return: None
        """
        self.ui_init_groupbox_filename_signals()
        self.ui_init_all_groupboxes()
        self.toggle_all_groupboxes_colors()
        self.comboBox_CatID.addItems(self.ucs.catids)
        self.set_opacity(self.frame_DragDrop, 0.3)

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
        self.toolButton_LoadFullCatCSV.pressed.connect(self.save_full_cat_feather)
        self.toolButton_LoadTopLevelCSV.pressed.connect(self.save_top_level_feather)
        self.toolButton_LoadTransCSV.pressed.connect(self.save_full_trans_feather)
        self.update_settings_csv_labels()
        # noinspection PyTypeChecker
        return True

    #####################################
    # Funcs #############################
    #####################################

    def ui_init_all_groupboxes(self):
        """
        Initializes the signals for all groupboxes
        """
        for parent in self.groupbox_parent_widgets:
            for self.widget in parent.children():
                if isinstance(self.widget, QGroupBox):
                    self.widget.setFlat(True)
                    self.widget.toggled.connect(self.toggle_all_groupboxes_colors)

    def ui_init_groupbox_filename_signals(self):
        """
        Initializes the groupbox signals for the filename section
        """
        self.groupBox_UserCat.setChecked(False)
        self.groupBox_VendorCat.setChecked(False)
        self.groupBox_UserData.setChecked(False)
        set_groupbox_title_white(self.groupBox_CreatorID)
        set_groupbox_title_white(self.groupBox_SourceID)

    def toggle_all_groupboxes_colors(self):
        """
        Switch title between white and grey if the checkboxes are selected
        Checks all children of certain layouts that contain groupboxes
        """
        for layout in self.groupbox_parent_widgets:
            for widget in layout.children():
                if isinstance(widget, QGroupBox):
                    toggle_groupbox_colors(widget)

    def set_opacity(self, widget: QWidget, opacity_f: float) -> None:
        """
        Set the widget opacity
        :param opacity_f: value to change the opacity
        :param widget: Qt widget to apply the opacity change
        :return:
        """
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(opacity_f)
        widget.setGraphicsEffect(self.opacity)

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
        Create UIFileConfirmation window with items from file_list
        :param file_list:
        """
        if self.file_confirmation_window is None:
            self.file_confirmation_window = UIFileConfirmation(parent=self)
            self.file_confirmation_window.set_wav_list(file_list)
            self.file_confirmation_window.buttonBox.rejected.connect(self.reset_file_confirmation_window)
            self.file_confirmation_window.destroyed.connect(self.reset_file_confirmation_window)
            self.file_confirmation_window.buttonBox.accepted.connect(self.file_confirmation_window_analyze_stt)

    def open_file_naming_review_window(self, speech_data: list[SpeechAnalyse]) -> None:
        """
        Create UIFileNamingReview window with items from file_list
        :param speech_data:
        """
        if self.file_naming_review_window is None:
            self.file_naming_review_window = UIFileNamingReview(parent=self)
            self.file_naming_review_window.update_table(speech_data)
            self.file_naming_review_window.buttonBox.rejected.connect(self.reset_file_naming_review_window)
            self.file_naming_review_window.destroyed.connect(self.reset_file_naming_review_window)
            # self.file_naming_review_window.buttonBox.accepted.connect(self.)

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
        Reset window object back to None. Used to ensure that only one UIFileConfirmation window is made
        """
        self.file_confirmation_window = None

    def reset_file_naming_review_window(self) -> None:
        """
        Reset window object back to None. Used to ensure that only one UIFileConfirmation window is made
        """
        self.file_naming_review_window = None

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
        if isinstance(files, list) and files:
            speech_list = []
            progress_window = ProgressWindow(parent=self)
            # self.progress_window.buttonBox.rejected.connect()
            for file in files:
                sa = SpeechAnalyse(file)
                sa.get_transcription_from_wav_file_google()
                speech_list.append(sa)
            progress_window.reject()

            self.open_file_naming_review_window(speech_list)
            # QMessageBox.about(self, "Speech-To-Text File Results", sa.speech_transcription_from_file)

    def reset_window(self) -> None:
        """
        Reset the
        :return: 
        """
        if not isinstance(self.file_confirmation_window, QDialog):
            self.reset_file_confirmation_window()

    def save_full_cat_feather(self):
        """
        Save a feather file of the UCS Full Category List .csv file
        """
        file = self.get_csv_file(Defaults.DIALOG_UCS_FULL_CAT_WINDOW)
        ucs_data.create_feather_from_csv(file, ucs_data.Defaults.UCS_FULL_CAT_FILE)
        self.update_settings_csv_labels()

    def save_full_trans_feather(self):
        """
        Save a feather file of the UCS Full Translations List .csv file
        """
        file = self.get_csv_file(Defaults.DIALOG_UCS_FULL_TRANS_WINDOW)
        ucs_data.create_feather_from_csv(file, ucs_data.Defaults.UCS_FULL_TRANS_FILE)
        self.update_settings_csv_labels()

    def save_top_level_feather(self):
        """
        Save a feather file of the UCS Full Category List .csv file
        """
        file = self.get_csv_file(Defaults.DIALOG_UCS_TOP_LEVEL_WINDOW)
        ucs_data.create_feather_from_csv(file, ucs_data.Defaults.UCS_TOP_LEVEL_FILE)
        self.update_settings_csv_labels()

    def get_csv_file(self, window_prompt: str) -> str:
        """

        :param window_prompt:
        """
        file: tuple = QFileDialog.getOpenFileName(
            self,
            window_prompt,
            utilities.get_home_path(),
            Defaults.CSV_WINDOW_TITLE
        )
        return file[0]

    def update_settings_csv_labels(self):
        """
        Update the label values if they exist
        :return:
        """
        if ucs_data.exists_full_cat_feather():
            self.label_LoadFullCatCSV.setText(Defaults.TOOL_BUTTON_CSV_LOADED)
        else:
            self.label_LoadFullCatCSV.setText(Defaults.TOOL_BUTTON_CSV_NOT_LOADED)

        if ucs_data.exists_top_level_feather():
            self.label_LoadTopLevelCSV.setText(Defaults.TOOL_BUTTON_CSV_LOADED)
        else:
            self.label_LoadTopLevelCSV.setText(Defaults.TOOL_BUTTON_CSV_NOT_LOADED)

        if ucs_data.exists_full_trans_feather():
            self.label_LoadTransCSV.setText(Defaults.TOOL_BUTTON_CSV_LOADED)
        else:
            self.label_LoadTransCSV.setText(Defaults.TOOL_BUTTON_CSV_NOT_LOADED)


class Defaults:
    """
    Default values
    """
    DIALOG_UCS_FULL_CAT_WINDOW: str = "Select the UCS Full Category List .csv file"
    DIALOG_UCS_TOP_LEVEL_WINDOW: str = "Select the UCS Top Level Categories .csv file"
    DIALOG_UCS_FULL_TRANS_WINDOW: str = "Select the UCS Full Translations List .csv file"

    TOOL_BUTTON_CSV_LOADED: str = '.csv is loaded'
    TOOL_BUTTON_CSV_NOT_LOADED: str = '[NO .CSV LOADED]'
    CSV_WINDOW_TITLE: str = "Comma Seperated Value File (*.csv)"


class Worker(QRunnable):
    """
.
    """

    def __init__(self):
        super().__init__()

# TODO: continue setting up the worker
# class WorkerSignals(QO)
