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

# sentences = [["AIRHiss", "Compressed", "Air", "Escaping", "Thermos", "Thin", "Hiss", "Slight", "Hollow", "Hum"],
#              ["AIRHiss", "Compressed", "Air", "Escaping", "Thermos", "Thin", "Hiss", "Slight", "Hollow", "Hum"],
#              ["AEROProp", "Airplane", "Interior", "Loop", "Aircraft", "Plane", "Propeller", "Engine", "Noise", "Idle", "Revving", "RPM"]
#              ]

xlsx_file = 'PSE_CORE3PRO-metadata.xlsx'

data_file = pd.read_excel(xlsx_file)
#
# w2v_model = Word2Vec(sentences, min_count=1)
# result = w2v_model.wv.most_similar(positive=['Airplane'])

# row = data_file.loc[:0]
row = data_file['Filename'].tolist()

print(row[0])
