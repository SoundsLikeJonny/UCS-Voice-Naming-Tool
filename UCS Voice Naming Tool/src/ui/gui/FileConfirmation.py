# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileConfirmation.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QAbstractItemView, QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
                               QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(479, 462)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget_WavFileSelect = QListWidget(self.widget)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_WavFileSelect)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_WavFileSelect)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_WavFileSelect)
        __qlistwidgetitem2.setCheckState(Qt.Checked);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_WavFileSelect)
        __qlistwidgetitem3.setCheckState(Qt.Checked);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_WavFileSelect)
        __qlistwidgetitem4.setCheckState(Qt.Checked);
        self.listWidget_WavFileSelect.setObjectName(u"listWidget_WavFileSelect")
        self.listWidget_WavFileSelect.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_WavFileSelect.setAlternatingRowColors(False)
        self.listWidget_WavFileSelect.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_WavFileSelect.setTextElideMode(Qt.ElideLeft)
        self.listWidget_WavFileSelect.setSortingEnabled(True)

        self.gridLayout.addWidget(self.listWidget_WavFileSelect, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_SampleRate = QLabel(self.widget_2)
        self.label_SampleRate.setObjectName(u"label_SampleRate")
        sizePolicy.setHeightForWidth(self.label_SampleRate.sizePolicy().hasHeightForWidth())
        self.label_SampleRate.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_SampleRate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_Channels = QLabel(self.widget_2)
        self.label_Channels.setObjectName(u"label_Channels")
        sizePolicy.setHeightForWidth(self.label_Channels.sizePolicy().hasHeightForWidth())
        self.label_Channels.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_Channels)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_BitDepth = QLabel(self.widget_2)
        self.label_BitDepth.setObjectName(u"label_BitDepth")
        sizePolicy.setHeightForWidth(self.label_BitDepth.sizePolicy().hasHeightForWidth())
        self.label_BitDepth.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_BitDepth)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_Length = QLabel(self.widget_2)
        self.label_Length.setObjectName(u"label_Length")
        sizePolicy.setHeightForWidth(self.label_Length.sizePolicy().hasHeightForWidth())
        self.label_Length.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_Length)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalWidget = QWidget(self.widget_2)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.verticalWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)

        self.verticalLayout_2.addWidget(self.verticalWidget)

        self.gridLayout.addWidget(self.widget_2, 3, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        __sortingEnabled = self.listWidget_WavFileSelect.isSortingEnabled()
        self.listWidget_WavFileSelect.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_WavFileSelect.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"File 1", None));
        ___qlistwidgetitem1 = self.listWidget_WavFileSelect.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"File 2", None));
        ___qlistwidgetitem2 = self.listWidget_WavFileSelect.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"File 3", None));
        ___qlistwidgetitem3 = self.listWidget_WavFileSelect.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"File 4", None));
        ___qlistwidgetitem4 = self.listWidget_WavFileSelect.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"File 5", None));
        self.listWidget_WavFileSelect.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Dialog", u"Confirm files for speech analysis:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sample Rate:", None))
        self.label_SampleRate.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Channels:", None))
        self.label_Channels.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Bit Depth:", None))
        self.label_BitDepth.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Length: ", None))
        self.label_Length.setText(QCoreApplication.translate("Dialog", u"*", None))
    # retranslateUi