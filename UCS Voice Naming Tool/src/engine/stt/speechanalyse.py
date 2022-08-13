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

import nlu

from src.engine.stt.speechread import SpeechRead


class SpeechAnalyse(SpeechRead):
    """
    Extends SpeechRead, but with functionality for parsing apart the text and extracting info
    """

    def __init__(self, file_path=None) -> None:
        super(SpeechAnalyse, self).__init__(file_path)

    def get_transcription_from_wav_file_google(self):
        """
        Override the get_transcription_from_wav_file_google method from the base class
        Perform nlu analysis on all text
        """
        super(SpeechAnalyse, self).get_transcription_from_wav_file_google()
        self.analyse_all_text()

    def analyse_all_text(self):
        """

        """
        pass
