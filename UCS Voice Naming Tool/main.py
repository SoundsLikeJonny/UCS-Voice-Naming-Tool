
#
import sys

from src.ui import UIMainWindow
from PyQt5.QtWidgets import *

obj = UIMainWindow.MainWindow()
obj.show()
print('Hello World!')


app = QApplication([])
sys.exit(app.exec_())
