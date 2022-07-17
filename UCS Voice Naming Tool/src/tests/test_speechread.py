#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 16, 2022
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

import unittest

from src.engine.stt.speechread import SpeechRead
from src.tests.test_testdata import Defaults


class TestSpeechRead(unittest.TestCase):

    def setUp(self) -> None:
        self.obj_good = SpeechRead(file_path=Defaults.VALID_WAV_SPEECH_UNIX)
        self.obj_good.store_speech_from_file()

    def tearDown(self) -> None:
        pass

    def test_store_speech_from_file(self) -> None:
        print(self.obj_good.speech_transcription_from_file)
        pass

    def test_get_non_silent_ranges(self) -> None:
        print(self.obj_good.get_non_silent_ranges())