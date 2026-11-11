#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: November 13, 2022
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

class Info:
    """
    Provide basic information on the project.
    Gets used everywhere in the project
    """
    PROJECT_TITLE = 'UCS Voice Naming Tool'
    COMPANY = ' '
    ICON_PATH = './resources/UCS_Logos/ucs_black_small.ico'
    NOTIFICATION_TIME = 3000


class FileTypes:
    """
    File extensions for files related to the application
    """
    PROJECT: str = '.ucsvnt'
    AUTO_SAVE: str = '.ucsvnt.save'
    PREFS: str = '.prefs'

    ALL_TYPES: list = [
        PROJECT,
        AUTO_SAVE,
        PREFS,

    ]

    @staticmethod
    def is_file_of_filetype(file: str) -> bool:
        """
        Check against
        :param file:
        :return:
        """
        for extension in FileTypes.ALL_TYPES:
            if file.endswith(extension):
                return True
        return False
