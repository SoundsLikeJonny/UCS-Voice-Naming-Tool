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
import pathlib
import tempfile
from pathlib import (
    PurePath
)

import speech_recognition as stt
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

from src.engine import utilities
from src.engine.audio.audio import is_file_valid
from src.engine.audio.wavfile import Wav


class SpeechRead:
    """
    Reading of speech and storing of text from the Google Speech Recognition API

    Requires an internet connection
    """

    # audio_data_from_file_googrec: AudioData

    def __init__(self, file_path=None) -> None:
        self.file_path = None
        self.wav = None
        self.recognizer = None
        self.speech_transcription_from_file = None
        self.audio_data_from_file_pydub = None
        self.audio_data_from_file_googrec = None
        self.temp_wav_list_to_process = None

        self.min_silence_len = 1000
        self.silence_threshold = -30
        self.seek_step = 1
        self.pad_length = 1000

        if is_file_valid(file_path):
            self.wav = Wav(file_path)

        if self.wav.file_path is not None:
            self.recognizer = stt.Recognizer()

        self.temp_dir = PurePath(tempfile.gettempdir())

        self.init_all_audio_data()

    def init_all_audio_data(self):
        """
        Call all audio data init functions
        :return:
        """
        self.init_audio_data_from_file_googrec()
        self.init_audio_data_from_file_pydub()

    def init_audio_data_from_file_pydub(self) -> None:
        """
        Read the audio .wav file and add the data to the object.
        """
        if self.wav is None:
            return None

        self.audio_data_from_file_pydub = AudioSegment.from_wav(self.wav.file_path)
        segments = self.get_audio_segments_non_silent_from_ranges()
        self.save_segment_list_to_temp_wav(segments)

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

    def get_non_silent_ranges(self) -> list[list[int, int]]:
        """
        Get a list of ranges where the audio is not silent
        :return:
        """
        return detect_nonsilent(
            self.audio_data_from_file_pydub,
            min_silence_len=self.min_silence_len,
            silence_thresh=self.silence_threshold,
            seek_step=self.seek_step
        )

    def get_audio_segments_non_silent_from_ranges(self) -> list[AudioSegment]:
        """
        Get a list of audio segments where there is no silence
        :return:
        """
        non_silent_ranges = self.get_non_silent_ranges()
        audio_datas = []

        if non_silent_ranges and self.audio_data_from_file_pydub:
            for start_range, end_range in non_silent_ranges:
                start_range, end_range = self.get_padded_ranges((start_range, end_range))
                audio_datas.append(self.audio_data_from_file_pydub[start_range:end_range:])

        return audio_datas

    def get_stt_from_segment_list(self, audio_segment_list: list[AudioSegment]):
        """

        :param audio_segment_list:
        :return:
        """
        text = []
        # for segment in audio_segment_list:

    def save_segment_list_to_temp_wav(self, seg_list: list[AudioSegment]) -> list[str]:
        """

        :param seg_list:
        :return: list of temp filepaths
        """
        self.temp_wav_list_to_process = [self.save_segment_to_temp_wav(segment, segment_file_name=f'chunk{index}')
                                         for index, segment in
                                         enumerate(seg_list) if segment is not None]
        return self.temp_wav_list_to_process

    def get_transcription_from_wav_file_google(self) -> None:
        """

        :return:
        """

        if self.temp_wav_list_to_process:
            transcription_list = [self.get_stt_from_file(file) for file in self.temp_wav_list_to_process
                                  if file is not None]
            self.speech_transcription_from_file = ' '.join(transcription_list)

            try:
                for file in self.temp_wav_list_to_process:
                    if file:
                        file.close()
                        path = pathlib.Path(str(file.name))
                        path.unlink()
            except Exception as e:
                print(e)

    def save_segment_to_temp_wav(self, segment: AudioSegment, segment_file_name: str = 'chunk') -> str | None:
        """
        Save a temporary .wav file and return its path
        :param segment_file_name:
        :param segment: The audio segment to save
        :return: filepath
        """
        if utilities.is_type(segment, AudioSegment) and utilities.is_str(segment_file_name):
            full_filepath = PurePath(self.temp_dir, f'{segment_file_name}.wav')
            print(full_filepath)
            return segment.export(full_filepath, format='wav')
        return None

    def get_stt_from_file(self, wav_filepath: str) -> str | None:
        """
        To be used with a function like "get_audio_segments_non_silent_from_ranges"
        :param wav_filepath:
        :return:
        """
        with stt.AudioFile(wav_filepath) as source:
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except stt.UnknownValueError:
            print("Could not understand audio")
        except stt.RequestError as e:
            print("Could not request results. check your internet connection")
        return None

    def get_stt_from_raw_data(self, raw_audio: bytes):
        """

        :param raw_audio:
        :return:
        """
        pass

    def get_padded_ranges(self, ranges: tuple[int, int]) -> tuple[int, int]:
        """
        Apply padding to start and ends of audio segments ranges
        :param ranges: Start and end values to be used to slice the audio segments
        :return: tuple with padded ranges
        """
        start, end = ranges
        start -= self.pad_length
        end += self.pad_length

        if start < 0:
            start = 0

        if end > len(self.audio_data_from_file_pydub):
            end = len(self.audio_data_from_file_pydub)

        return start, end
