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

from pydub import AudioSegment
from pydub.silence import detect_nonsilent

from src.engine.audio.wavfile import Wav
from src.engine.audio.audio import is_file_valid

import speech_recognition as stt

class SpeechRead:
    """
    Reading of speech and storing of text from the Google Speech Recognition API

    Requires an internet connection
    """
    def __init__(self, file_path=None) -> None:
        self.file_path = None
        self.wav = None
        self.recognizer = None
        self.speech_transcription_from_file = None
        self.audio_data_from_file_pydub = None
        self.audio_data_from_file_googrec = None

        self.min_silence_len = 50
        self.silence_threshold = -16
        self.seek_step = 1

        if is_file_valid(file_path):
            self.wav = Wav(file_path)

        if self.wav.file_path is not None:
            self.recognizer = stt.Recognizer()
        
        self.init_all_audio_data()

    def init_all_audio_data(self):
        self.init_audio_data_from_file_googrec()
        self.init_audio_data_from_file_pydub()

    def init_audio_data_from_file_pydub(self) -> None:
        """
        
        """
        if self.wav is None:
            return None

        self.audio_data_from_file_pydub = AudioSegment.from_wav(self.wav.file_path)

    def init_audio_data_from_file_googrec(self) -> None:
        """
        Read the audio .wav file and add the data to the object.
        The suffix 'googrec' is used to signify that the data was stored using Google's .record method
        """
        if self.wav is None or self.recognizer is None:
            return None

        with stt.AudioFile(self.wav.file_path) as audio_file:
            self.audio_data_from_file_googrec = self.recognizer.record(audio_file)

    def store_speech_from_file(self) -> None:
        """``
        Attempt to access the Google Speech Recognition API and read the file.
        """
        self.speech_transcription_from_file = self.recognizer.recognize_google(self.audio_data_from_file_googrec)

    def get_non_silent_ranges(self) -> list:
        return detect_nonsilent(
            self.audio_data_from_file_pydub,
            min_silence_len=self.min_silence_len,
            silence_thresh=self.silence_threshold,
            seek_step=self.seek_step
            )
