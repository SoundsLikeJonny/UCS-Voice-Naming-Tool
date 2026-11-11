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

import subprocess
import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtWidgets import QApplication


def main():
    """
    Create a new build
    """
    app = QApplication()
    try:
        command = str(Path.joinpath(Path().absolute(), 'env/Scripts/pyinstaller.exe'))
        windowed = '--w'
        args = str(Path.joinpath(Path().absolute(), 'build.spec'))
        current_date_time = '\n\n\nNEW BUILD\n=========\n' + str(
            datetime.now().strftime("%d %B, %Y %H:%M,%S")) + '\n\n\n'
        err = open('build_log.txt', 'a')
        err.write(current_date_time)
        err.flush()
        print([command, windowed, args])
        c = subprocess.Popen([command, args], stderr=err, shell=True, close_fds=True, universal_newlines=True)
        print(str(c))
        c.wait()
    except Exception as e:
        print(e)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
