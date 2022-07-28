#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 6, 2022
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
from pathlib import (
    Path
)

"""
#######################################
############# File Path ###############
#######################################
"""


def get_file(file_name: str) -> str | None:
    """
    Get the full path of the file
    :param file_name: The path of the file relative to the src directory
    :return: Full path
    """
    if type(file_name) == str:
        current_dir = Path.cwd()
        file = str(current_dir) + file_name
        if os.path.isfile(file) and isinstance(file, str):
            return file
    return None


def get_resource(resource_path: str) -> str | None:
    """
    Gets the resource file from the resources' folder
    :param resource_path:
    :return:
    """
    if type(resource_path) == str:
        return get_file(Defaults.RESOURCES_PATH + resource_path)


"""
#######################################
################# UI ##################
#######################################
"""


def get_project_ui_file(ui_file_name: str) -> str | None:
    """
    Get the full path of the relative ui file
    :param ui_file_name: The path of the ui file relative to the src directory
    :return: Full path
    """
    if type(ui_file_name) == str:
        file = os.path.join(os.getcwd(), Defaults.GUI_DOC_PATH, ui_file_name)
        if os.path.isfile(file):
            return file
    return None


"""
#######################################
############ VALIDATION ###############
#######################################
"""


def is_type(value: any, _type: any) -> bool:
    """
    Return True if the value is a string
    :param _type: Builtin type to check
    :param value: Value to check
    :rtype: bool
    """
    return type(value) == _type


def is_str(value: str) -> bool:
    """
    Return True if the value is a string
    :param value: String to check
    :rtype: bool
    """
    return is_type(value, str)


def is_int(value: int) -> bool:
    """
    Return True if the value is an integer
    :param value: Int to check
    :rtype: bool
    """
    return is_type(value, int)


def is_list(value: list) -> bool:
    """
    Return True if the value is a list
    :param value: list to check
    :rtype: bool
    """
    return is_type(value, list)


def is_dict(value: dict) -> bool:
    """
    Return True if the value is a dict
    :param value: dict to check
    :rtype: bool
    """
    return is_type(value, dict)


"""
#######################################
############# DIRECTORY ###############
#######################################
"""


def get_home_path() -> str:
    """
    Return the user's main directory
    :return:
    """
    return str(Path().home())


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
    RESOURCES_PATH = '\\resources'
