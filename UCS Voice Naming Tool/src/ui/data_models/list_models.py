#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: July 24, 2022
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

from typing import Union

from PySide6.QtCore import (
    QAbstractListModel,
    Qt,
    QPersistentModelIndex,
    QModelIndex,

)


class DefaultListModel(QAbstractListModel):
    """
    Extends QAbstractListModel to provide basic functionality for updating data and UI
    """

    def __init__(self, data_list: list = None) -> None:
        super().__init__()
        self.data_list = data_list or []

    def _data(self, index, role):
        """

        :param index:
        :param role:
        :return:
        """
        if role == Qt.DisplayRole:
            status, text = self.data_list[index.row()]
            return text

    def rowCount(self, index: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        """

        :param index:
        :return:
        """
        return len(self.data_list)
