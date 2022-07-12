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


class TestWav(unittest.TestCase):

    def setUp(self) -> None:
        self.path = os.getcwd() + '\\src\\tests\\test_wav_files\\'
        self.filenames = os.listdir(self.path)
        self.audio_files = [self.path + filename for filename in self.filenames]

    def tearDown(self) -> None:
        pass

    # def test_get_audio_data(self):
    #     print(self.audio_files)

    # def test_load_audio_data(self):
    #     self.fail()
    #
    # def test_is_file_valid(self):
    #     self.fail()
