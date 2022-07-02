#!/env/Scripts/python.exe
#
#
#
#
#
#
#
#

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from os import path


class MainWindow(QMainWindow):
    def __int__(self, **kwargs):

        super(MainWindow, self).__init__()
        uic.loadUi('/gui/MainWindow.ui')
        self.show()

