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

import base64
import gzip
import ast

from project_info import FileTypes


class FileData:
    """
    Not intended to be instanced.
    Contains static methods to be used in the reading and writing of custom filetypes according to the project info
    """

    @staticmethod
    def save(data: any, filename: str) -> None:
        """

        :param data:
        :param filename:
        :return:
        """
        if not FileTypes.is_file_of_filetype(filename):
            print('Invalid filetype of project')
            return None

        if isinstance(filename, str):
            data = FileData._encode_data(data)
            FileData._write_data(data, filename)

    @staticmethod
    def _encode_data(data: any):
        """
        Not intended to be called outside the class
        Encode the data to base 64 then compress
        :param data: What to encode
        :return: compressed and encoded data
        """
        data = "[{}]".format(data).encode()
        data = base64.b64encode(data)
        return gzip.compress(data)

    @staticmethod
    def _write_data(data: any, filename: str):
        """
        Not intended to be called outside the class
        Write the data to the file
        :param data:
        :param filename:
        :return:
        """
        try:
            open(filename, "wb").write(data)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def load(filename: str) -> any:
        """
        Load and return the data from a file if it's a known project filetype
        :param filename:
        :return:
        """
        try:
            data = open(filename, "rb").read()
        except Exception as e:
            print(e)
            return None

        data = gzip.decompress(data)
        data = base64.b64decode(data)
        data = ast.literal_eval(data.decode())[0]

        if not data:
            print('No data to load')
            return None

        return data
