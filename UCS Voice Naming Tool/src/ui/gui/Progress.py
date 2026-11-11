# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Progress.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(675, 186)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout_2.addWidget(self.label_title)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_info1 = QLabel(self.frame)
        self.label_info1.setObjectName(u"label_info1")

        self.verticalLayout_2.addWidget(self.label_info1)

        self.label_info2 = QLabel(self.frame)
        self.label_info2.setObjectName(u"label_info2")

        self.verticalLayout_2.addWidget(self.label_info2)

        self.label_info3 = QLabel(self.frame)
        self.label_info3.setObjectName(u"label_info3")

        self.verticalLayout_2.addWidget(self.label_info3)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.progressBar.setFormat(QCoreApplication.translate("Dialog", u"%p%", None))
        self.label_info1.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.label_info2.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.label_info3.setText(QCoreApplication.translate("Dialog", u"*", None))
    # retranslateUi

