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
import pandas as pd
from pandas import (
    DataFrame
)
from pyarrow import (
    feather
)


def create_feather_from_csv(filepath: str, save_name: str) -> None:
    """
    Read the .csv file as a pyarrow Table object and write that to a feather file
    :param save_name: The feather file name
    :param filepath: The .csv file
    """
    if isinstance(filepath, str) and os.path.isfile(filepath):
        df: DataFrame = pd.read_csv(filepath, skipinitialspace=True)
        for column in df.columns:
            df[column] = df[column].str.strip()
            df.rename({column: column.strip()}, axis='columns', inplace=True)
        feather.write_feather(df, save_name)
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


def get_sorted_unique_list(data_list: list) -> list:
    """

    :param data_list:
    :return:
    """
    if isinstance(data_list, list):
        column = set(data_list)
        column = list(column)
        column = sorted(column)
        return column


class UCS:
    """
    Class for reading, writing and loading of feather files containing UCS data
    Also converts .csv to .feather files.

    This data can then be elegantly used with Pandas
    """

    def __init__(self) -> None:
        self.catids = []
        self.categories = []
        self.ucs_full_cat = None
        self.ucs_full_trans = None
        self.ucs_top_level = None
        self.load_feathers()

    def load_feathers(self):
        """
        Attempt to load the feathers if they exist
        """
        if exists_full_cat_feather():
            self.ucs_full_cat = pd.read_feather(Defaults.UCS_FULL_CAT_FILE)
            self.categories = get_sorted_unique_list(self.ucs_full_cat["Category"].tolist())
            self.catids = self.ucs_full_cat["CatID"].tolist()

        if exists_full_trans_feather():
            self.ucs_full_trans = pd.read_feather(Defaults.UCS_FULL_TRANS_FILE)
        if exists_top_level_feather():
            self.ucs_top_level = pd.read_feather(Defaults.UCS_TOP_LEVEL_FILE)

    def get_row_from_catid(self, catid: str) -> DataFrame:
        """
        Use the catid to determine the row
        :param catid:
        """
        return self.ucs_full_cat.loc[self.ucs_full_cat['CatID'] == catid]

    def get_rows_from_category(self, category: str) -> DataFrame:
        """

        :param category:
        :return:
        """
        return self.ucs_full_cat.loc[self.ucs_full_cat['Category'] == category]


class Defaults:
    """
    Default values
    """
    UCS_FULL_CAT_FILE: str = 'ucs_full_category_list.feather'
    UCS_FULL_TRANS_FILE: str = 'ucs_full_translations_list.feather'
    UCS_TOP_LEVEL_FILE: str = 'ucs_full_top_level_categories.feather'
