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
from unittest import TestCase

from src.engine.ucs.ucs_data import (
    UCS,
    Defaults,
    create_feather_from_csv,
    exists_top_level_feather,
    exists_full_trans_feather,
    exists_full_cat_feather,
    _exists_feather_path
)
from src.engine.utilities import get_file
from src.tests import test_testdata


class TestUCS(TestCase):

    def setUp(self) -> None:
        self.ucs_obj_good = UCS()

    def tearDown(self) -> None:
        del self.ucs_obj_good

    def test_create_feather_from_csv(self) -> None:
        ucs_file = get_file(test_testdata.Defaults.VALID_UCS_CSV)
        create_feather_from_csv(ucs_file, Defaults.UCS_FULL_CAT_FILE)
        self.assertTrue(os.path.exists(Defaults.UCS_FULL_CAT_FILE))
        create_feather_from_csv(ucs_file, Defaults.UCS_TOP_LEVEL_FILE)
        self.assertTrue(os.path.exists(Defaults.UCS_TOP_LEVEL_FILE))
        create_feather_from_csv(ucs_file, Defaults.UCS_FULL_TRANS_FILE)
        self.assertTrue(os.path.exists(Defaults.UCS_FULL_TRANS_FILE))

    def test_exists_full_cat_feather(self):
        self.assertTrue(exists_full_cat_feather())

    def test_exists_top_level_feather(self):
        self.assertTrue(exists_top_level_feather())

    def test_exists_full_trans_feather(self):
        self.assertTrue(exists_full_trans_feather())

    def test__exists_feather_path(self):
        self.assertTrue(_exists_feather_path(Defaults.UCS_FULL_TRANS_FILE))

    def test_load_feathers(self):
        self.assertIsNotNone(self.ucs_obj_good.ucs_full_cat)
        self.assertIsNotNone(self.ucs_obj_good.ucs_full_trans)
        self.assertIsNotNone(self.ucs_obj_good.ucs_top_level)
