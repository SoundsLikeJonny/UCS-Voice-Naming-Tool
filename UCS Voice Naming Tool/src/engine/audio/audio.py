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
import pathlib

from pyaudio import PyAudio

from src.engine.utilities import is_str


def is_file_valid(file: str) -> bool:
    """
    Validate the .wav file
    :param file:
    :return:
    """
    if not is_str(file) \
            or not os.path.isfile(file) \
            or pathlib.Path(file).suffix != '.wav':
        return False
    return True


class Audio:
    """
    Extends pyaudio and pydub for audio manipulation
    """

    def __init__(self, file_path=None, **kwargs):
        if file_path and is_file_valid(file_path):
            # self.py_audio = PyAudio()
            # self.data, self.samplerate = soundfile.read(file_path)
            # self.audio_segment = AudioSegment().from_wav(file_path)
            self.file_path = file_path
