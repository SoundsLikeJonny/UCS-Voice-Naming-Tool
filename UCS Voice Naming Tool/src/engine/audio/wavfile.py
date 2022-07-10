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

import wave
import os, pathlib
from src.engine.audio import Audio
from src.engine.utilities import is_str


class Wav(Audio):

    def __init__(self,file_path: str = '', **kwargs):
        super().__init__(self,**kwargs)
        if not self.is_file_valid(file_path):
            self = None
            return self
        self.file_path = file_path


    def is_file_valid(self, file: str) -> bool:
        if not is_str(file) \
            or not os.path.isfile(file) \
            or pathlib.Path(file).suffix != '.wav':
            return False
        return True

    def load_audio_data(self, file_path: str):
        # TODO: load audio data
        pass

    def get_audio_data(self, file_path: str):
        # TODO: return audio data
        pass


    # TODO: write a function to get audio chunks
    