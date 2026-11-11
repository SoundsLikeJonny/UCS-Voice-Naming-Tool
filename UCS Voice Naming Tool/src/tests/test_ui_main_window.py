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
import os
import sys
from unittest import TestCase

from PySide6.QtWidgets import QApplication

from src.ui.theme import theme
from src.ui.ui_file_confirmation_window import UIFileConfirmation
from src.ui.ui_main_window import MainWindow


class TestMainWindow(TestCase):

    def setUp(self) -> None:
        self.app = QApplication(sys.argv)
        theme.set_default_theme(self.app)
        self.obj = MainWindow()
        self.file_confirm_good = self.obj.open_file_confirmation_window(Defaults.test_file_list)
        self.file_confirm_bad = self.obj.open_file_confirmation_window(Defaults.bad_test_file_list)

    def tearDown(self) -> None:
        self.app.exit()

    def test_exists_qt_widgets(self):
        self.assertTrue(self.obj.exists_qt_widgets())

    def test_init_ui_voice_tab(self) -> None:
        self.assertFalse(self.obj.groupBox_UserCat.isChecked(), False)
        self.assertFalse(self.obj.groupBox_VendorCat.isChecked(), False)
        self.assertFalse(self.obj.groupBox_UserData.isChecked(), False)

    def test_init_ui_conflict_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_conflict_tab(), True)

    def test_init_ui_mic_list_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_mic_list_tab(), True)

    def test_init_ui_wildcard_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_wildcard_tab(), True)

    def test_init_ui_settings_tab(self) -> None:
        self.assertTrue(self.obj.init_ui_settings_tab(), True)

    def test_open_file_confirmation_window(self):
        self.assertIsInstance(self.obj.file_confirmation_window, UIFileConfirmation)

    def test_reset_file_confirmation_window(self):
        self.obj.reset_file_confirmation_window()
        self.assertIsNone(self.obj.file_confirmation_window)

    def test_file_confirmation_window_analyze_stt(self):
        self.obj.file_confirmation_window = self.file_confirm_good
        self.obj.file_confirmation_window_analyze_stt()
        self.assertIsNone(self.obj.file_confirmation_window)

    def test_handle_drop_event_files(self):
        self.obj.handle_drop_event_files(Defaults.test_file_list)
        self.assertIsInstance(self.obj.file_confirmation_window, UIFileConfirmation)

    def test_analyze_stt(self):
        self.assertFalse(self.obj.analyze_stt())
        self.assertTrue(self.obj.analyze_stt(files=[]))
        self.assertTrue(self.obj.analyze_stt(files=Defaults.test_file_list))
        self.assertTrue(self.obj.analyze_stt(files=Defaults.bad_test_file_list))


class Defaults:
    test_file_list = [
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_01.wav",
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_02.wav",
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_03.wav",
    ]
    bad_test_file_list = [
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_01.mp3",
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_02",
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_03.av",
    ]
    voice_results = [
        '',
        '',
        ''
    ]


class TestMainWindow(TestCase):
    def test_init_all_ui(self):
        self.fail()

    def test_exists_qt_widgets(self):
        self.fail()

    def test_init_ui_voice_tab(self):
        self.fail()

    def test_init_ui_conflict_tab(self):
        self.fail()

    def test_init_ui_mic_list_tab(self):
        self.fail()

    def test_init_ui_wildcard_tab(self):
        self.fail()

    def test_init_ui_settings_tab(self):
        self.fail()

    def test_ui_init_all_groupboxes(self):
        self.fail()

    def test_ui_init_groupbox_filename_signals(self):
        self.fail()

    def test_toggle_all_groupboxes_colors(self):
        self.fail()

    def test_set_opacity(self):
        self.fail()

    def test_drop_event(self):
        self.fail()

    def test_handle_drop_event_files(self):
        self.fail()

    def test_open_file_confirmation_window(self):
        self.fail()

    def test_drag_enter_event(self):
        self.fail()

    def test_reset_file_confirmation_window(self):
        self.fail()

    def test_file_confirmation_window_analyze_stt(self):
        self.fail()

    def test_analyze_stt(self):
        self.fail()

    def test_reset_window(self):
        self.fail()

    def test_save_full_cat_feather(self):
        self.fail()

    def test_save_full_trans_feather(self):
        self.fail()

    def test_save_top_level_feather(self):
        self.fail()

    def test_get_csv_file(self):
        self.fail()

    def test_update_settings_csv_labels(self):
        self.fail()
