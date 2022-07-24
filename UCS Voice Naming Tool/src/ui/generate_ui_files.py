#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 23, 2022
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


import glob
import os
from pathlib import Path

"""
Creates the PySide6 Python UI files from .ui files
Created in UCS Voice Naming Tool\\src\\ui\\gui
"""
path_to_gui = Path().joinpath(os.getcwd(), 'src\\ui\\gui')

print(f"""
#################
#################
#################
#################

{path_to_gui}

#################
#################
#################
#################
""")

for file in glob.glob(f"{path_to_gui}\\*.ui"):
    py_filename = Path(f'{path_to_gui}{file}').stem
    py_filepath = Path(f'{path_to_gui}\\{py_filename}.py')
    os.system(f'pyside6-uic "{file}" -o "{py_filepath}"')


def main():
    """
    Unused
    :return:
    """
    pass


if __name__ == "__main__":
    main()
