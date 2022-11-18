#!/env/Scripts/python.exe

"""
Author: Jon Evans
Last Modified: August 3, 2022
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


from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from pathlib import Path
import pandas as pd
from pandas import (
    DataFrame
)

from pyarrow import (
    feather
)

import pickle

import os


# MODEL_SENTENCES = [["AIRHiss", "Compressed", "Air", "Escaping", "Thermos", "Thin", "Hiss", "Slight", "Hollow", "Hum"],
#                    ["AIRHiss", "Compressed", "Air", "Escaping", "Thermos", "Thin", "Hiss", "Slight", "Hollow", "Hum"],
#                    ["AEROProp", "Airplane", "Interior", "Loop", "Aircraft", "Plane", "Propeller", "Engine", "Noise",
#                     "Idle", "Revving", "RPM"]
#                    ]
#
# xlsx_file = 'PSE_CORE3PRO-metadata.xlsx'
#
# data_file = pd.read_excel(xlsx_file)
# #
# w2v_model = Word2Vec(sentences, min_count=1)
# result = w2v_model.wv.most_similar(positive=['Airplane'])
#
# # row = data_file.loc[:0]
# row = data_file['Filename'].tolist()
#
# print(row[0])


def add_data_to_model(model_path: str, data_path: str, sentence_data: list[str]):
    """
    Add the string data to the model

    """

    validate_model_data(sentence_data)

    if not os.path.isfile(model_path):
        # raise FileNotFoundError
        pass

    if not os.path.isfile(data_path):
        create_data_file(data_path)
        raise FileNotFoundError

    # with open(data_path, 'wb') as gfile:
    #     pass


def create_data_file(file_path: str, data: list[str] = None) -> None:
    """
    Create a new data file if one does not exist
    """
    if not os.path.isfile(file_path):
        try:
            with open(file_path, 'wb') as file:
                if data is not None:
                    pickle.dump(data, file)
                else:
                    pickle.dump([], file)
        except Exception as e:
            print(str(e))


def add_to_data_file(file_path: str, data: list[str]) -> None:
    """
    Data list data to the data file
    :param data: a list of strings to add to the data file
    :param file_path: the location of the file
    :return:
    """
    file_data = get_data_file(file_path)
    if file_data:
        file_data.append(data)


def get_data_file(file_path: str) -> list | None:
    """
    Get the nested list with all the dataa
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
            return data
        except Exception as e:
            print(str(e))
    print('not found')


def validate_model_data(sentence_data: list[str]) -> None:
    """
    Ensure that the data is a list of strings
    """
    if not isinstance(sentence_data, list):
        raise TypeError

    for data in sentence_data:
        if not isinstance(data, str):
            raise TypeError


class ML:

    def __init__(self) -> None:
        pass


class Defaults:
    global_ucs_model = 'global_ucs_model.bin'
    global_ucs_data = 'global_ucs_model_data.txt'

    local_ucs_model = 'local_ucs_model.bin'
    local_ucs_data = 'local_ucs_model_data.txt'
