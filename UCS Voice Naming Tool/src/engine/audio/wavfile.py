#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 27, 2022
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


import datetime
import wave
from typing import BinaryIO

import soundfile

from src.engine.audio.audio import Audio, is_file_valid


def get_length_formatted(wave_file) -> str:
    """
    Returns a formatted string of the length of the audio file
    :param wave_file:
    :return:
    """
    len_sec: float = wave_file.getnframes() / float(wave_file.getframerate())
    len_sec: int = round(len_sec)
    return str(datetime.timedelta(seconds=len_sec))


def get_samplerate(wave_file) -> int:
    """
    Return the framerate multiplied bu the samplewidth
    :param wave_file:
    :return:
    """
    return wave_file.getframerate() * wave_file.getnchannels()


class Wav(Audio):
    """
    .
    """

    def __init__(self, file_path: str = None, **kwargs):
        super().__init__(file_path=file_path, **kwargs)
        # if not is_file_valid(file_path):
        # self = None
        self.file_path = None
        self.sample_width = None
        self.channels = None
        self.sample_rate = None
        self.comp_name = None
        self.comp_type = None
        self.fp = None
        self.bit_depth = None
        self.n_frames = None
        self.length = None

        if is_file_valid(file_path):
            self.file_path: str = file_path

        self.set_audio_info()

    def __str__(self):
        f"""

        """

    def set_audio_info(self) -> None:
        """
        Set all audio info to the object
        """
        # TODO: find a way to load without errors. FFmpeg needs installation, can't read RIF

        if self.file_path is not None:
            wave_file: any = wave.open(self.file_path, 'rb')
            wave_file_sf: soundfile.SoundFile = soundfile.SoundFile(self.file_path)

            self.sample_width: int = wave_file.getsampwidth()
            self.channels: int = wave_file.getnchannels() or None
            self.sample_rate: int = get_samplerate(wave_file) or None
            self.comp_name: str = wave_file.getcompname() or None
            self.comp_type: str = wave_file.getcomptype() or None
            self.fp: BinaryIO = wave_file.getfp() or None
            self.bit_depth: str = wave_file_sf.subtype or None
            self.n_frames: int = wave_file.getnframes() or None
            self.length: str = get_length_formatted(wave_file) or None
