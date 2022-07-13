#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 12, 2022
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


from unittest import TestCase
import sys
import os

from PyQt5.QtWidgets import QApplication
from src.ui.ui_file_confirmation_window import FileConfirmation
from src.ui.ui_main_window import MainWindow


class TestFileConfirmation(TestCase):

    def setUp(self) -> None:
        self.app = QApplication(sys.argv)
        self.parent = MainWindow()
        self.obj_good = FileConfirmation(parent=self.parent)
        self.obj_good.set_wav_list(Defaults.test_file_list)
        self.obj_good.show()
        self.obj_bad = FileConfirmation(parent=self.parent)
        self.obj_bad.set_wav_list(Defaults.bad_test_file_list)
        self.obj_bad.show()

    def tearDown(self) -> None:
        self.app.exit()

    def test_exists_qt_widgets(self):
        self.assertIsNotNone(self.obj_good.listWidget_WavFileSelect)

    def test_store_list_widget_wav_file_paths(self):
        self.obj_good.set_wav_list(Defaults.test_file_list)
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, Defaults.test_file_list)
        self.obj_bad.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_bad.selected_wav_items, [])

    def test_set_wav_list(self):
        self.obj_good.set_wav_list(5)
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, [])
        self.obj_good.set_wav_list('')
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, [])
        self.obj_good.set_wav_list(None)
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, [])
        self.obj_good.set_wav_list({})
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, [])
        self.obj_good.set_wav_list([])
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, [])
        self.obj_good.set_wav_list(Defaults.test_file_list)
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, Defaults.test_file_list)
        self.obj_good.set_wav_list(Defaults.bad_test_file_list)
        self.obj_good.store_list_widget_wav_file_paths()
        self.assertEqual(self.obj_good.selected_wav_items, [])

    def test_get_selected_wave_file_info(self):
        self.obj_good.listWidget_WavFileSelect.setCurrentRow(0)
        self.obj_good.get_selected_wave_file_info()

    def test_reject(self):
        self.obj_good.reject()
        self.assertFalse(self.obj_good.isVisible())

    def test_close_event(self):
        self.obj_good.closeEvent(None)
        self.assertFalse(self.obj_good.isVisible())
        # self.assertIsInstance(self.obj, FileConfirmation)

    def test_close(self):
        self.obj_good.close()
        self.assertFalse(self.obj_good.isVisible())
        # self.assertIsInstance(self.obj, FileConfirmation)


class Defaults:
    test_file_list = [
        f"{os.getcwd()}\\src\\tests\\test_wav_files\\TEST_01.wav",
        f"{os.getcwd()}\\src\\tests\\test_wav_files\\TEST_02.wav",
        f"{os.getcwd()}\\src\\tests\\test_wav_files\\TEST_03.wav"
    ]
    bad_test_file_list = [
        f"{os.getcwd()}\\src\\tests\\test_wav_files\\TEST_01.mp3",
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_02",
        f"{os.getcwd()}\\UCS Voice Naming Tool\\src\\tests\\test_wav_files\\TEST_03.av"
    ]
    voice_results = [
        '',
        '',
        ''
    ]
