#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 10, 2022
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
import unittest
from src.engine.audio.wavfile import Wav, is_file_valid


class TestWav(unittest.TestCase):

    def setUp(self) -> None:
        self.path = os.getcwd() + Defaults.WAV_FILEPATH_UNIX
        self.filenames = os.listdir(self.path)
        self.audio_files = [self.path + filename for filename in self.filenames]
        self.wav_obj = Wav(file_path='/workspaces/UCS-Voice-Naming-Tool/UCS Voice Naming Tool/src/tests/test_wav_files/Test_05.wav')
        # self.wav_obj = Wav(file_path=self.audio_files[4])

    def tearDown(self) -> None:
        pass

    def test_get_audio_info(self):
        self.assertNotEqual(self.wav_obj.get_audio_info(), {})

    def test_load_audio_data(self):
        pass
        # self.fail()

    def test_is_file_valid(self):
        self.assertTrue(is_file_valid(self.audio_files[0]))
        self.assertFalse('')
        self.assertFalse(None)
        self.assertFalse(0)

class Defaults:
    WAV_FILEPATH_WINDOWS = '\\src\\tests\\test_wav_files\\'
    WAV_FILEPATH_UNIX = '/src/tests/test_wav_files/'

