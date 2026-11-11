# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReviewFileInfo.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Frame_window(object):
    def setupUi(self, Frame_window):
        if not Frame_window.objectName():
            Frame_window.setObjectName(u"Frame_window")
        Frame_window.resize(871, 178)
        self.verticalLayout = QVBoxLayout(Frame_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_main = QFrame(Frame_window)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy)
        self.frame_main.setMinimumSize(QSize(0, 160))
        self.frame_main.setMaximumSize(QSize(16777215, 300))
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Sunken)
        self.frame_main.setLineWidth(3)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_main)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.label_ucsnaming = QLabel(self.frame_main)
        self.label_ucsnaming.setObjectName(u"label_ucsnaming")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_ucsnaming.sizePolicy().hasHeightForWidth())
        self.label_ucsnaming.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        self.label_ucsnaming.setFont(font)

        self.horizontalLayout.addWidget(self.label_ucsnaming)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_3 = QLabel(self.frame_main)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_file = QLabel(self.frame_main)
        self.label_file.setObjectName(u"label_file")
        sizePolicy2.setHeightForWidth(self.label_file.sizePolicy().hasHeightForWidth())
        self.label_file.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_file)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_5 = QLabel(self.frame_main)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_description = QLabel(self.frame_main)
        self.label_description.setObjectName(u"label_description")
        sizePolicy2.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_description)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.treeWidget_details = QTreeWidget(self.frame_main)
        self.treeWidget_details.headerItem().setText(0, "")
        self.treeWidget_details.headerItem().setText(1, "")
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_details)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.treeWidget_details.setObjectName(u"treeWidget_details")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.treeWidget_details.sizePolicy().hasHeightForWidth())
        self.treeWidget_details.setSizePolicy(sizePolicy3)
        self.treeWidget_details.setMaximumSize(QSize(16777215, 300))
        self.treeWidget_details.setFrameShape(QFrame.NoFrame)
        self.treeWidget_details.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.treeWidget_details.setAlternatingRowColors(False)
        self.treeWidget_details.setAutoExpandDelay(0)
        self.treeWidget_details.setAnimated(False)
        self.treeWidget_details.header().setVisible(False)
        self.treeWidget_details.header().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.treeWidget_details)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.checkBox_include = QCheckBox(self.frame_main)
        self.checkBox_include.setObjectName(u"checkBox_include")
        sizePolicy1.setHeightForWidth(self.checkBox_include.sizePolicy().hasHeightForWidth())
        self.checkBox_include.setSizePolicy(sizePolicy1)
        self.checkBox_include.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_include)

        self.pushButton = QPushButton(self.frame_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_remove = QPushButton(self.frame_main)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setMaximumSize(QSize(20, 16777215))
        self.pushButton_remove.setFlat(False)

        self.horizontalLayout_4.addWidget(self.pushButton_remove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(Frame_window)

        QMetaObject.connectSlotsByName(Frame_window)
    # setupUi

    def retranslateUi(self, Frame_window):
        Frame_window.setWindowTitle(QCoreApplication.translate("Frame_window", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame_window", u"UCS Naming:     ", None))
        self.label_ucsnaming.setText(QCoreApplication.translate("Frame_window", u"TESTName_", None))
        self.label_3.setText(QCoreApplication.translate("Frame_window", u"File:                      ", None))
        self.label_file.setText(QCoreApplication.translate("Frame_window", u"*", None))
        self.label_5.setText(QCoreApplication.translate("Frame_window", u"Description:        ", None))
        self.label_description.setText(QCoreApplication.translate("Frame_window", u"*", None))

        __sortingEnabled = self.treeWidget_details.isSortingEnabled()
        self.treeWidget_details.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget_details.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Frame_window", u"Details", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Frame_window", u"Raw Description", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem.child(1)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Frame_window", u"Subcategory", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem.child(2)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Frame_window", u"New Subitem", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem.child(3)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Frame_window", u"New Subitem", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem.child(4)
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Frame_window", u"New Subitem", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem.child(5)
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Frame_window", u"New Subitem", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem.child(6)
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("Frame_window", u"test", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Frame_window", u"New Subitem", None));
        self.treeWidget_details.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.checkBox_include.setToolTip(QCoreApplication.translate("Frame_window", u"Include in bulk changes?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkBox_include.setStatusTip(QCoreApplication.translate("Frame_window", u"Include in bulk changes?", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_include.setText("")
        self.pushButton.setText(QCoreApplication.translate("Frame_window", u"Reload", None))
#if QT_CONFIG(tooltip)
        self.pushButton_remove.setToolTip(QCoreApplication.translate("Frame_window", u"Remove", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_remove.setText(QCoreApplication.translate("Frame_window", u"X", None))
    # retranslateUi

