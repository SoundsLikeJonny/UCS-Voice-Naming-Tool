#!/env/Scripts/python.exe

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

"""
#######################################
################# UI ##################
#######################################
"""


def get_project_ui_file(ui_file_name: str) -> any:
    """
    Get the full path of the relative ui file
    :param ui_file_name: The path of the ui file relative to the src directory
    :return: Full path
    """
    if type(ui_file_name) == str:
        file = os.path.join(os.getcwd(), Defaults.GUI_DOC_PATH, ui_file_name)
        if os.path.exists(file):
            return file
    return None


"""
#######################################
########## DEFAULT VALUES #############
#######################################
"""


class Defaults:
    """
    Default values
    """
    GUI_DOC_PATH = 'src\\ui\\gui\\'
