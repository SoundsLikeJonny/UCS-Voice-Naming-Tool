#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: Aug 12, 2022
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


from unittest import TestCase

from src.engine.stt import ml

import os


class TestML(TestCase):

    def test_create_data_file(self):
        ml.create_data_file(ml.Defaults.global_ucs_data)
        self.assertTrue(os.path.isfile(ml.Defaults.global_ucs_data))

    def test_add_data_to_model(self):
        self.fail()

    def test_get_data_file(self):
        result = ml.get_data_file(ml.Defaults.global_ucs_data)
        print(result)
