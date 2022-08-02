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
from unittest import TestCase

from src.engine.stt.speechread import SpeechRead
from src.tests.test_testdata import Defaults


class TestSpeechRead(unittest.TestCase):

    def setUp(self) -> None:
        self.obj_good = SpeechRead(file_path=Defaults.VALID_WAV_SPEECH_WINDOWS)
        self.obj_good.store_speech_from_file()

    def tearDown(self) -> None:
        pass

    def test_store_speech_from_file(self) -> None:
        print(self.obj_good.speech_transcription_from_file)
        pass

    def test_get_non_silent_ranges(self) -> None:
        print(self.obj_good.get_non_silent_ranges())

    def test_get_audio_segments_non_silent_from_ranges(self) -> None:
        print(self.obj_good.get_audio_segments_non_silent_from_ranges())

    def test_get_padded_ranges(self):
        # self.fail()
        pass

    def test_get_stt_from_raw_data(self):
        # self.fail()
        pass

    def test_get_stt_from_segment_list(self):
        # self.fail()
        pass

    def test_get_stt_from_segment(self):
        segments = self.obj_good.get_audio_segments_non_silent_from_ranges()
        print(segments)
        result = self.obj_good.get_stt_from_segment(self.obj_good.audio_data_from_file_pydub)
        print(result)

    def test_save_segment_to_temp_wav(self):
        self.fail()

    def test_get_transcription_from_wav_file_google(self):
        self.obj_good.get_transcription_from_wav_file_google()
        print(self.obj_good.speech_transcription_from_file)


class TestSpeechRead(TestCase):
    def test_init_all_audio_data(self):
        self.fail()

    def test_init_audio_data_from_file_pydub(self):
        self.fail()

    def test_init_audio_data_from_file_googrec(self):
        self.fail()

    def test_store_speech_from_file(self):
        self.fail()

    def test_get_non_silent_ranges(self):
        self.fail()

    def test_get_audio_segments_non_silent_from_ranges(self):
        self.fail()

    def test_get_stt_from_segment_list(self):
        self.fail()

    def test_save_segment_list_to_temp_wav(self):
        self.fail()

    def test_get_transcription_from_wav_file_google(self):
        self.fail()

    def test_save_segment_to_temp_wav(self):
        self.fail()

    def test_get_stt_from_file(self):
        self.fail()

    def test_get_stt_from_raw_data(self):
        self.fail()

    def test_get_padded_ranges(self):
        self.fail()
