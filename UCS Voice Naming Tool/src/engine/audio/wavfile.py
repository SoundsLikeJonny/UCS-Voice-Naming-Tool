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

from src.engine.audio.audio import Audio, is_file_valid

import soundfile


class Wav(Audio):
    """
    .
    """

    def __init__(self, file_path: str = None, **kwargs):
        super().__init__(file_path=file_path, **kwargs)
        # if not is_file_valid(file_path):
        # self = None
        self.file_path = None
        
        if is_file_valid(file_path):
            self.file_path = file_path

        self.data = self.get_audio_info()

    def get_audio_info(self) -> dict:
        """
        Return wave info on file
        """
        # TODO: find a way to load without errors. FFmpeg needs installation, can't read RIF

        if self.file_path is not None:
            wave_file = wave.open(self.file_path, 'rb')
            wave_file_sf = soundfile.SoundFile(self.file_path)
            data = {
                'sample_width': wave_file.getsampwidth(),
                'channels': wave_file.getnchannels(),
                'sample_rate': wave_file.getframerate(),
                'comp_name': wave_file.getcompname(),
                'comp_type': wave_file.getcomptype(),
                'fp': wave_file.getfp(),
                'bit_depth' : wave_file_sf.subtype,
                # 'markers': wave_file.getmarkers(),
                'n_frames': wave_file.getnframes(),
                # 'bit_depth' : wave_file.
            }
            return data
        return {}

    def get_audio_data(self):
        """

        """
        # TODO: return audio data
        pass

    # TODO: write a function to get audio chunks
