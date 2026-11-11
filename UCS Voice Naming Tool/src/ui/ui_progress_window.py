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
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtCore import (
    Qt
)

from PySide6.QtWidgets import (
    QDialog
)

from project_info import Info
from src.ui.gui.Progress import Ui_Dialog


class ProgressWindow(Ui_Dialog, QDialog):
    """
    .
    """

    def __init__(self, *args: object, parent=None, **kwargs: object) -> None:
        super(ProgressWindow, self).__init__(parent, *args, **kwargs)

        self.init_all_ui()

    def init_all_ui(self) -> None:
        """
        Initialize UI window
        :return: None
        """
        self.setupUi(self)

        self.setWindowIcon(QIcon(Info.ICON_PATH))
        # self.setWindowFlags(Qt.FramelessWindowHint)

        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.buttonBox.rejected.connect(self.reject)
        self.show()

    def reject(self) -> None:
        """
        Override to ensure proper closure of window
        """
        super().reject()

    def closeEvent(self, event):
        """
        Override to ensure proper closure of window
        :param event:
        """
        self.reject()

    def close(self) -> None:
        """
        Override to ensure proper closure of window
        """
        self.reject()
