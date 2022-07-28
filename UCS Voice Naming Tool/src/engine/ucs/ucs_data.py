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

import os

from pyarrow import (
    csv,
    feather,
    Table
)


def create_feather_from_csv(filepath: str, save_name: str) -> None:
    """
    Read the .csv file as a pyarrow Table object and write that to a feather file
    :param save_name: The feather file name
    :param filepath: The .csv file
    """
    if isinstance(filepath, str) and os.path.isfile(filepath):
        table: Table = csv.read_csv(filepath)
        feather.write_feather(table, save_name)
    return None


def exists_full_cat_feather() -> bool:
    """
    Does the feather exists in the current directory?
    :return:
    """
    return _exists_feather_path(Defaults.UCS_FULL_CAT_FILE)


def exists_top_level_feather() -> bool:
    """
    Does the feather exists in the current directory?
    :return:
    """
    return _exists_feather_path(Defaults.UCS_TOP_LEVEL_FILE)


def exists_full_trans_feather() -> bool:
    """
    Does the feather exists in the current directory?
    :return:
    """
    return _exists_feather_path(Defaults.UCS_FULL_TRANS_FILE)


def _exists_feather_path(path: str) -> bool:
    """
    Does the feather exists in the current directory?
    :return:
    """
    if isinstance(path, str):
        if os.path.exists(path):
            return True
    return False


class UCS:
    """
    Class for reading, writing and loading of feather files containing UCS data
    Also converts .csv to .feather files.

    This data can then be elegantly used with Pandas
    """

    def __init__(self) -> None:
        pass


class Defaults:
    """
    Default values
    """
    UCS_FULL_CAT_FILE: str = 'ucs_full_category_list.feather'
    UCS_FULL_TRANS_FILE: str = 'ucs_full_translations_list.feather'
    UCS_TOP_LEVEL_FILE: str = 'ucs_full_top_level_categories.feather'
