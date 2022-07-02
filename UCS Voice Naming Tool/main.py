#
import sys

from src.ui.UIMainWindow import MainWindow
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

app = QApplication(sys.argv)

flags = Qt.WindowFlags()
obj = MainWindow()
obj.show()


sys.exit(app.exec_())
