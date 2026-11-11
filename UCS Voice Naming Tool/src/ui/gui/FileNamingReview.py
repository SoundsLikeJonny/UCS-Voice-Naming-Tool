# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileNamingReview.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1137, 655)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.checkBox_switch_views = QCheckBox(Dialog)
        self.checkBox_switch_views.setObjectName(u"checkBox_switch_views")

        self.horizontalLayout_4.addWidget(self.checkBox_switch_views)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1_tableview = QWidget()
        self.page_1_tableview.setObjectName(u"page_1_tableview")
        self.verticalLayout = QVBoxLayout(self.page_1_tableview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.page_1_tableview)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_1_tableview)
        self.page_2_summaryview = QWidget()
        self.page_2_summaryview.setObjectName(u"page_2_summaryview")
        self.gridLayout_3 = QGridLayout(self.page_2_summaryview)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea1 = QScrollArea(self.page_2_summaryview)
        self.scrollArea1.setObjectName(u"scrollArea1")
        self.scrollArea1.setFrameShape(QFrame.NoFrame)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1101, 557))
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea1, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2_summaryview)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_4.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Refresh UCS Naming", None))
        self.checkBox_switch_views.setText(QCoreApplication.translate("Dialog", u"Box/Table View", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Path", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"New Column", None));
    # retranslateUi

