# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 654)
        MainWindow.setMinimumSize(QSize(959, 0))
        MainWindow.setMaximumSize(QSize(1000, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_Main = QTabWidget(self.centralwidget)
        self.tabWidget_Main.setObjectName(u"tabWidget_Main")
        self.tabWidget_Main.setStyleSheet(u"")
        self.tabWidget_Main.setMovable(True)
        self.tab_Voice = QWidget()
        self.tab_Voice.setObjectName(u"tab_Voice")
        self.gridLayout_9 = QGridLayout(self.tab_Voice)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.DEBUG_label_test1 = QLabel(self.tab_Voice)
        self.DEBUG_label_test1.setObjectName(u"DEBUG_label_test1")

        self.gridLayout_9.addWidget(self.DEBUG_label_test1, 0, 0, 1, 1)

        self.line = QFrame(self.tab_Voice)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.tab_Voice)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 200))
        self.widget.setMaximumSize(QSize(300, 300))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.frame_DragDrop = QFrame(self.widget)
        self.frame_DragDrop.setObjectName(u"frame_DragDrop")
        self.frame_DragDrop.setMinimumSize(QSize(0, 200))
        palette = QPalette()
        brush = QBrush(QColor(81, 86, 102, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame_DragDrop.setPalette(palette)
        self.frame_DragDrop.setAcceptDrops(True)
        self.frame_DragDrop.setAutoFillBackground(False)
        self.frame_DragDrop.setStyleSheet(u"background-color: rgb(81, 86, 102);")
        self.gridLayout_3 = QGridLayout(self.frame_DragDrop)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_22 = QLabel(self.frame_DragDrop)
        self.label_22.setObjectName(u"label_22")
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_22.setFont(font)
        self.label_22.setFrameShape(QFrame.Box)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_DragDrop, 0, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.doubleSpinBox = QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(-70.000000000000000)
        self.doubleSpinBox.setMaximum(-10.000000000000000)
        self.doubleSpinBox.setValue(-24.000000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 3, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.checkBox_SkipFileSelection = QCheckBox(self.widget)
        self.checkBox_SkipFileSelection.setObjectName(u"checkBox_SkipFileSelection")

        self.horizontalLayout_15.addWidget(self.checkBox_SkipFileSelection)

        self.checkBox_SkipNamingReview = QCheckBox(self.widget)
        self.checkBox_SkipNamingReview.setObjectName(u"checkBox_SkipNamingReview")

        self.horizontalLayout_15.addWidget(self.checkBox_SkipNamingReview)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_Naming = QWidget(self.widget_2)
        self.widget_Naming.setObjectName(u"widget_Naming")
        self.widget_Naming.setMinimumSize(QSize(595, 0))
        self.verticalLayout = QVBoxLayout(self.widget_Naming)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.label_CatID = QLabel(self.widget_Naming)
        self.label_CatID.setObjectName(u"label_CatID")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_CatID.sizePolicy().hasHeightForWidth())
        self.label_CatID.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        self.label_CatID.setFont(font1)
        self.label_CatID.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.horizontalLayout_12.addWidget(self.label_CatID)

        self.label_UserCatHyphen = QLabel(self.widget_Naming)
        self.label_UserCatHyphen.setObjectName(u"label_UserCatHyphen")
        sizePolicy.setHeightForWidth(self.label_UserCatHyphen.sizePolicy().hasHeightForWidth())
        self.label_UserCatHyphen.setSizePolicy(sizePolicy)
        self.label_UserCatHyphen.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_UserCatHyphen)

        self.label_UserCat = QLabel(self.widget_Naming)
        self.label_UserCat.setObjectName(u"label_UserCat")
        sizePolicy.setHeightForWidth(self.label_UserCat.sizePolicy().hasHeightForWidth())
        self.label_UserCat.setSizePolicy(sizePolicy)
        self.label_UserCat.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_UserCat)

        self.label_16 = QLabel(self.widget_Naming)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.label_VendorCat = QLabel(self.widget_Naming)
        self.label_VendorCat.setObjectName(u"label_VendorCat")
        sizePolicy.setHeightForWidth(self.label_VendorCat.sizePolicy().hasHeightForWidth())
        self.label_VendorCat.setSizePolicy(sizePolicy)
        self.label_VendorCat.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_VendorCat)

        self.label_VendorCatHyphen = QLabel(self.widget_Naming)
        self.label_VendorCatHyphen.setObjectName(u"label_VendorCatHyphen")
        sizePolicy.setHeightForWidth(self.label_VendorCatHyphen.sizePolicy().hasHeightForWidth())
        self.label_VendorCatHyphen.setSizePolicy(sizePolicy)
        self.label_VendorCatHyphen.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_VendorCatHyphen)

        self.label_21 = QLabel(self.widget_Naming)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.horizontalLayout_12.addWidget(self.label_21)

        self.label_20 = QLabel(self.widget_Naming)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_20)

        self.label_CreatorID = QLabel(self.widget_Naming)
        self.label_CreatorID.setObjectName(u"label_CreatorID")
        sizePolicy.setHeightForWidth(self.label_CreatorID.sizePolicy().hasHeightForWidth())
        self.label_CreatorID.setSizePolicy(sizePolicy)
        self.label_CreatorID.setFont(font1)
        self.label_CreatorID.setStyleSheet(u"color: rgb(170, 74, 74);")

        self.horizontalLayout_12.addWidget(self.label_CreatorID)

        self.label_26 = QLabel(self.widget_Naming)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_26)

        self.label_SourceID = QLabel(self.widget_Naming)
        self.label_SourceID.setObjectName(u"label_SourceID")
        sizePolicy.setHeightForWidth(self.label_SourceID.sizePolicy().hasHeightForWidth())
        self.label_SourceID.setSizePolicy(sizePolicy)
        self.label_SourceID.setFont(font1)
        self.label_SourceID.setStyleSheet(u"color: rgb(170, 74, 74);")

        self.horizontalLayout_12.addWidget(self.label_SourceID)

        self.label_UserDataUnderscore = QLabel(self.widget_Naming)
        self.label_UserDataUnderscore.setObjectName(u"label_UserDataUnderscore")
        sizePolicy.setHeightForWidth(self.label_UserDataUnderscore.sizePolicy().hasHeightForWidth())
        self.label_UserDataUnderscore.setSizePolicy(sizePolicy)
        self.label_UserDataUnderscore.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_UserDataUnderscore)

        self.label_UserData = QLabel(self.widget_Naming)
        self.label_UserData.setObjectName(u"label_UserData")
        sizePolicy.setHeightForWidth(self.label_UserData.sizePolicy().hasHeightForWidth())
        self.label_UserData.setSizePolicy(sizePolicy)
        self.label_UserData.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_UserData)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 20)
        self.label_18 = QLabel(self.widget_Naming)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.label_17 = QLabel(self.widget_Naming)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.label_15 = QLabel(self.widget_Naming)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(170, 74, 74);")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_3 = QSpacerItem(10, 3, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_CatID = QGroupBox(self.widget_Naming)
        self.groupBox_CatID.setObjectName(u"groupBox_CatID")
        self.groupBox_CatID.setMinimumSize(QSize(145, 0))
        self.groupBox_CatID.setStyleSheet(u"")
        self.groupBox_CatID.setFlat(True)
        self.groupBox_CatID.setCheckable(True)
        self.groupBox_CatID.setChecked(False)
        self.gridLayout_11 = QGridLayout(self.groupBox_CatID)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.comboBox_CatID = QComboBox(self.groupBox_CatID)
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.addItem("")
        self.comboBox_CatID.setObjectName(u"comboBox_CatID")

        self.gridLayout_11.addWidget(self.comboBox_CatID, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_CatID)

        self.groupBox_UserCat = QGroupBox(self.widget_Naming)
        self.groupBox_UserCat.setObjectName(u"groupBox_UserCat")
        self.groupBox_UserCat.setMinimumSize(QSize(111, 50))
        self.groupBox_UserCat.setMaximumSize(QSize(111111, 16777215))
        self.groupBox_UserCat.setFlat(True)
        self.groupBox_UserCat.setCheckable(True)
        self.groupBox_UserCat.setChecked(True)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_UserCat)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_UserCat = QLineEdit(self.groupBox_UserCat)
        self.lineEdit_UserCat.setObjectName(u"lineEdit_UserCat")
        self.lineEdit_UserCat.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_UserCat.setFrame(False)

        self.verticalLayout_2.addWidget(self.lineEdit_UserCat)


        self.horizontalLayout_2.addWidget(self.groupBox_UserCat)

        self.groupBox_VendorCat = QGroupBox(self.widget_Naming)
        self.groupBox_VendorCat.setObjectName(u"groupBox_VendorCat")
        self.groupBox_VendorCat.setMinimumSize(QSize(111, 50))
        self.groupBox_VendorCat.setMaximumSize(QSize(1111, 16777215))
        self.groupBox_VendorCat.setFlat(True)
        self.groupBox_VendorCat.setCheckable(True)
        self.groupBox_VendorCat.setChecked(True)
        self.gridLayout_4 = QGridLayout(self.groupBox_VendorCat)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_VendorCat = QLineEdit(self.groupBox_VendorCat)
        self.lineEdit_VendorCat.setObjectName(u"lineEdit_VendorCat")
        self.lineEdit_VendorCat.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_VendorCat.setFrame(False)

        self.gridLayout_4.addWidget(self.lineEdit_VendorCat, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_VendorCat)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_FXName = QGroupBox(self.widget_Naming)
        self.groupBox_FXName.setObjectName(u"groupBox_FXName")
        self.groupBox_FXName.setMinimumSize(QSize(0, 63))
        self.groupBox_FXName.setFlat(False)
        self.groupBox_FXName.setCheckable(True)
        self.groupBox_FXName.setChecked(False)
        self.gridLayout_10 = QGridLayout(self.groupBox_FXName)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_4 = QLineEdit(self.groupBox_FXName)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 20))
        self.lineEdit_4.setFrame(False)

        self.gridLayout_10.addWidget(self.lineEdit_4, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_FXName, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.widget_Naming)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_12.addWidget(self.frame_3, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_CreatorID = QGroupBox(self.widget_Naming)
        self.groupBox_CreatorID.setObjectName(u"groupBox_CreatorID")
        self.groupBox_CreatorID.setMinimumSize(QSize(90, 50))
        self.groupBox_CreatorID.setStyleSheet(u"color: rgb(170, 74, 74);")
        self.groupBox_CreatorID.setFlat(False)
        self.gridLayout_7 = QGridLayout(self.groupBox_CreatorID)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_CreatorID = QLineEdit(self.groupBox_CreatorID)
        self.lineEdit_CreatorID.setObjectName(u"lineEdit_CreatorID")
        self.lineEdit_CreatorID.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_CreatorID.setFrame(False)
        self.lineEdit_CreatorID.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_7.addWidget(self.lineEdit_CreatorID, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_CreatorID)

        self.groupBox_SourceID = QGroupBox(self.widget_Naming)
        self.groupBox_SourceID.setObjectName(u"groupBox_SourceID")
        self.groupBox_SourceID.setStyleSheet(u"color: rgb(170, 74, 74);")
        self.groupBox_SourceID.setFlat(False)
        self.gridLayout_8 = QGridLayout(self.groupBox_SourceID)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_SourceID = QLineEdit(self.groupBox_SourceID)
        self.lineEdit_SourceID.setObjectName(u"lineEdit_SourceID")
        self.lineEdit_SourceID.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_SourceID.setFrame(False)

        self.gridLayout_8.addWidget(self.lineEdit_SourceID, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_SourceID)

        self.groupBox_UserData = QGroupBox(self.widget_Naming)
        self.groupBox_UserData.setObjectName(u"groupBox_UserData")
        self.groupBox_UserData.setMinimumSize(QSize(111, 0))
        self.groupBox_UserData.setMaximumSize(QSize(1111, 16777215))
        self.groupBox_UserData.setCheckable(True)
        self.groupBox_UserData.setChecked(True)
        self.gridLayout_6 = QGridLayout(self.groupBox_UserData)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_UserData = QLineEdit(self.groupBox_UserData)
        self.lineEdit_UserData.setObjectName(u"lineEdit_UserData")
        self.lineEdit_UserData.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_UserData.setFrame(False)

        self.gridLayout_6.addWidget(self.lineEdit_UserData, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_UserData)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_5.addWidget(self.widget_Naming, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.widget_2, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.scrollArea_AnalysisPrefs = QScrollArea(self.tab_Voice)
        self.scrollArea_AnalysisPrefs.setObjectName(u"scrollArea_AnalysisPrefs")
        self.scrollArea_AnalysisPrefs.setMinimumSize(QSize(0, 130))
        self.scrollArea_AnalysisPrefs.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_AnalysisPrefs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_AnalysisPrefs.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_AnalysisPrefs.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 954, 128))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.widget_AnalysisPrefs = QWidget(self.scrollAreaWidgetContents)
        self.widget_AnalysisPrefs.setObjectName(u"widget_AnalysisPrefs")
        self.horizontalLayout_AnalysisPrefs = QHBoxLayout(self.widget_AnalysisPrefs)
        self.horizontalLayout_AnalysisPrefs.setObjectName(u"horizontalLayout_AnalysisPrefs")
        self.horizontalLayout_AnalysisPrefs.setContentsMargins(-1, -1, -1, 1)
        self.groupBox_OnlyAnalyseEndsOfFiles = QGroupBox(self.widget_AnalysisPrefs)
        self.groupBox_OnlyAnalyseEndsOfFiles.setObjectName(u"groupBox_OnlyAnalyseEndsOfFiles")
        self.groupBox_OnlyAnalyseEndsOfFiles.setMinimumSize(QSize(71, 100))
        self.groupBox_OnlyAnalyseEndsOfFiles.setMaximumSize(QSize(222, 16777215))
        self.groupBox_OnlyAnalyseEndsOfFiles.setCheckable(True)
        self.groupBox_OnlyAnalyseEndsOfFiles.setChecked(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, 0)
        self.label_3 = QLabel(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.spinBox_StartOnlyAnalyseEndsOfFiles = QSpinBox(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.spinBox_StartOnlyAnalyseEndsOfFiles.setObjectName(u"spinBox_StartOnlyAnalyseEndsOfFiles")
        self.spinBox_StartOnlyAnalyseEndsOfFiles.setMaximum(120)
        self.spinBox_StartOnlyAnalyseEndsOfFiles.setValue(30)

        self.horizontalLayout_5.addWidget(self.spinBox_StartOnlyAnalyseEndsOfFiles)

        self.label_7 = QLabel(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 3)
        self.label_4 = QLabel(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.spinBox_EndOnlyAnalyseEndsOfFiles = QSpinBox(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.spinBox_EndOnlyAnalyseEndsOfFiles.setObjectName(u"spinBox_EndOnlyAnalyseEndsOfFiles")
        self.spinBox_EndOnlyAnalyseEndsOfFiles.setMaximum(120)
        self.spinBox_EndOnlyAnalyseEndsOfFiles.setValue(30)
        self.spinBox_EndOnlyAnalyseEndsOfFiles.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.spinBox_EndOnlyAnalyseEndsOfFiles)

        self.label_8 = QLabel(self.groupBox_OnlyAnalyseEndsOfFiles)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_AnalysisPrefs.addWidget(self.groupBox_OnlyAnalyseEndsOfFiles)

        self.groupBox_OnlyReadBetweenMarkers = QGroupBox(self.widget_AnalysisPrefs)
        self.groupBox_OnlyReadBetweenMarkers.setObjectName(u"groupBox_OnlyReadBetweenMarkers")
        self.groupBox_OnlyReadBetweenMarkers.setMinimumSize(QSize(200, 100))
        self.groupBox_OnlyReadBetweenMarkers.setMaximumSize(QSize(230, 16777215))
        self.groupBox_OnlyReadBetweenMarkers.setCheckable(True)
        self.groupBox_OnlyReadBetweenMarkers.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_OnlyReadBetweenMarkers)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, 0)
        self.label_5 = QLabel(self.groupBox_OnlyReadBetweenMarkers)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.groupBox_OnlyReadBetweenMarkers)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(True)

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.groupBox_OnlyReadBetweenMarkers)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.groupBox_OnlyReadBetweenMarkers)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setFrame(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_AnalysisPrefs.addWidget(self.groupBox_OnlyReadBetweenMarkers)

        self.frame_2 = QFrame(self.widget_AnalysisPrefs)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_AnalysisPrefs.addWidget(self.frame_2)

        self.groupBox_UseTakeMarkers = QGroupBox(self.widget_AnalysisPrefs)
        self.groupBox_UseTakeMarkers.setObjectName(u"groupBox_UseTakeMarkers")
        self.groupBox_UseTakeMarkers.setMinimumSize(QSize(202, 95))
        self.groupBox_UseTakeMarkers.setMaximumSize(QSize(202, 16777215))
        self.groupBox_UseTakeMarkers.setCheckable(True)
        self.groupBox_UseTakeMarkers.setChecked(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_UseTakeMarkers)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, 0)
        self.label_9 = QLabel(self.groupBox_UseTakeMarkers)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.groupBox_UseTakeMarkers)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFrame(True)

        self.horizontalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.checkBox_3 = QCheckBox(self.groupBox_UseTakeMarkers)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_6.addWidget(self.checkBox_3)


        self.horizontalLayout_AnalysisPrefs.addWidget(self.groupBox_UseTakeMarkers)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_AnalysisPrefs.addItem(self.horizontalSpacer_2)


        self.gridLayout_15.addWidget(self.widget_AnalysisPrefs, 0, 0, 1, 1)

        self.scrollArea_AnalysisPrefs.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea_AnalysisPrefs)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label = QLabel(self.tab_Voice)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.gridLayout_9.addLayout(self.verticalLayout_3, 4, 0, 1, 1)

        self.tabWidget_Main.addTab(self.tab_Voice, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_Main.addTab(self.tab, "")
        self.tab_MicList = QWidget()
        self.tab_MicList.setObjectName(u"tab_MicList")
        self.tabWidget_Main.addTab(self.tab_MicList, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_Main.addTab(self.tab_2, "")
        self.tab_Settings = QWidget()
        self.tab_Settings.setObjectName(u"tab_Settings")
        self.gridLayout_13 = QGridLayout(self.tab_Settings)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget_4 = QWidget(self.tab_Settings)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 50)
        self.groupBox_2 = QGroupBox(self.widget_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout_14 = QGridLayout(self.groupBox_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_LoadTopLevelCSV = QLabel(self.groupBox_2)
        self.label_LoadTopLevelCSV.setObjectName(u"label_LoadTopLevelCSV")

        self.gridLayout_14.addWidget(self.label_LoadTopLevelCSV, 3, 3, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_14.addWidget(self.label_13, 4, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_10, 2, 2, 1, 1)

        self.toolButton_LoadFullCatCSV = QToolButton(self.groupBox_2)
        self.toolButton_LoadFullCatCSV.setObjectName(u"toolButton_LoadFullCatCSV")

        self.gridLayout_14.addWidget(self.toolButton_LoadFullCatCSV, 2, 4, 1, 1)

        self.label_LoadTransCSV = QLabel(self.groupBox_2)
        self.label_LoadTransCSV.setObjectName(u"label_LoadTransCSV")

        self.gridLayout_14.addWidget(self.label_LoadTransCSV, 4, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_14.addWidget(self.label_10, 3, 0, 1, 1)

        self.toolButton_LoadTopLevelCSV = QToolButton(self.groupBox_2)
        self.toolButton_LoadTopLevelCSV.setObjectName(u"toolButton_LoadTopLevelCSV")

        self.gridLayout_14.addWidget(self.toolButton_LoadTopLevelCSV, 3, 4, 1, 1)

        self.toolButton_LoadTransCSV = QToolButton(self.groupBox_2)
        self.toolButton_LoadTransCSV.setObjectName(u"toolButton_LoadTransCSV")

        self.gridLayout_14.addWidget(self.toolButton_LoadTransCSV, 4, 4, 1, 1)

        self.label_LoadFullCatCSV = QLabel(self.groupBox_2)
        self.label_LoadFullCatCSV.setObjectName(u"label_LoadFullCatCSV")

        self.gridLayout_14.addWidget(self.label_LoadFullCatCSV, 2, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_14.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_11, 3, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_12, 4, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_14.addWidget(self.label_11, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.groupBox_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.gridLayout_13.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tabWidget_Main.addTab(self.tab_Settings, "")

        self.gridLayout.addWidget(self.tabWidget_Main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.groupBox_CatID, self.comboBox_CatID)
        QWidget.setTabOrder(self.comboBox_CatID, self.groupBox_FXName)
        QWidget.setTabOrder(self.groupBox_FXName, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.groupBox_UserData)
        QWidget.setTabOrder(self.groupBox_UserData, self.groupBox_OnlyAnalyseEndsOfFiles)
        QWidget.setTabOrder(self.groupBox_OnlyAnalyseEndsOfFiles, self.spinBox_StartOnlyAnalyseEndsOfFiles)
        QWidget.setTabOrder(self.spinBox_StartOnlyAnalyseEndsOfFiles, self.spinBox_EndOnlyAnalyseEndsOfFiles)
        QWidget.setTabOrder(self.spinBox_EndOnlyAnalyseEndsOfFiles, self.groupBox_OnlyReadBetweenMarkers)
        QWidget.setTabOrder(self.groupBox_OnlyReadBetweenMarkers, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.tabWidget_Main)
        QWidget.setTabOrder(self.tabWidget_Main, self.toolButton_LoadFullCatCSV)
        QWidget.setTabOrder(self.toolButton_LoadFullCatCSV, self.toolButton_LoadTopLevelCSV)
        QWidget.setTabOrder(self.toolButton_LoadTopLevelCSV, self.toolButton_LoadTransCSV)

        self.retranslateUi(MainWindow)
        self.groupBox_UserData.toggled.connect(self.label_UserData.setVisible)
        self.groupBox_UserData.toggled.connect(self.label_UserDataUnderscore.setVisible)
        self.groupBox_VendorCat.toggled.connect(self.label_VendorCat.setVisible)
        self.groupBox_VendorCat.toggled.connect(self.label_VendorCatHyphen.setVisible)
        self.groupBox_UserCat.toggled.connect(self.label_UserCat.setVisible)
        self.groupBox_UserCat.toggled.connect(self.label_UserCatHyphen.setVisible)
        self.lineEdit_CreatorID.textChanged.connect(self.label_CreatorID.setText)
        self.lineEdit_CreatorID.textChanged.connect(self.groupBox_CreatorID.repaint)
        self.lineEdit_SourceID.textChanged.connect(self.label_SourceID.setText)
        self.comboBox_CatID.currentTextChanged.connect(self.label_CatID.setText)
        self.lineEdit_UserCat.textChanged.connect(self.label_UserCat.setText)
        self.lineEdit_VendorCat.textChanged.connect(self.label_VendorCat.setText)
        self.lineEdit_UserData.textChanged.connect(self.label_UserData.setText)

        self.tabWidget_Main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UCS Voice Naming Tool", None))
        self.DEBUG_label_test1.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"DROP FILES HERE", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Silence Threshold:", None))
        self.checkBox_SkipFileSelection.setText(QCoreApplication.translate("MainWindow", u"Skip File Selection", None))
        self.checkBox_SkipNamingReview.setText(QCoreApplication.translate("MainWindow", u"Skip Naming Review", None))
        self.label_CatID.setText(QCoreApplication.translate("MainWindow", u"CatID", None))
        self.label_UserCatHyphen.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_UserCat.setText(QCoreApplication.translate("MainWindow", u"UserCat", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_VendorCat.setText(QCoreApplication.translate("MainWindow", u"VendorCat", None))
        self.label_VendorCatHyphen.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"FXName", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_CreatorID.setText(QCoreApplication.translate("MainWindow", u"CreatorID", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_SourceID.setText(QCoreApplication.translate("MainWindow", u"SourceID", None))
        self.label_UserDataUnderscore.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_UserData.setText(QCoreApplication.translate("MainWindow", u"UserData", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"* Optional (manual input)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"* Speech-To-Text Attempt", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"* Required (manual input)", None))
        self.groupBox_CatID.setTitle(QCoreApplication.translate("MainWindow", u"Override CatID", None))
        self.comboBox_CatID.setItemText(0, QCoreApplication.translate("MainWindow", u"AIRBlow", None))
        self.comboBox_CatID.setItemText(1, QCoreApplication.translate("MainWindow", u"AMBPubl", None))
        self.comboBox_CatID.setItemText(2, QCoreApplication.translate("MainWindow", u"AMBTraf", None))
        self.comboBox_CatID.setItemText(3, QCoreApplication.translate("MainWindow", u"AMBTraf", None))
        self.comboBox_CatID.setItemText(4, QCoreApplication.translate("MainWindow", u"BELLHand", None))
        self.comboBox_CatID.setItemText(5, QCoreApplication.translate("MainWindow", u"BIRDFowl", None))
        self.comboBox_CatID.setItemText(6, QCoreApplication.translate("MainWindow", u"CRWDConv", None))

        self.groupBox_UserCat.setTitle(QCoreApplication.translate("MainWindow", u"UserCat", None))
        self.lineEdit_UserCat.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. Garage Trinkets", None))
        self.groupBox_VendorCat.setTitle(QCoreApplication.translate("MainWindow", u"VendorCat", None))
        self.lineEdit_VendorCat.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. Wrestle Car Mania", None))
        self.groupBox_FXName.setTitle(QCoreApplication.translate("MainWindow", u"Custom FXName Template", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"$title ($ntake$vtake) - $subtitle - $prop, $verb, $descriptions", None))
        self.groupBox_CreatorID.setTitle(QCoreApplication.translate("MainWindow", u"CreatorID", None))
        self.lineEdit_CreatorID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. JKim", None))
        self.groupBox_SourceID.setTitle(QCoreApplication.translate("MainWindow", u"SourceID", None))
        self.lineEdit_SourceID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. HomeSFXLib", None))
        self.groupBox_UserData.setTitle(QCoreApplication.translate("MainWindow", u"UserData", None))
        self.lineEdit_UserData.setText("")
        self.lineEdit_UserData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. $num", None))
        self.groupBox_OnlyAnalyseEndsOfFiles.setTitle(QCoreApplication.translate("MainWindow", u"Only Analyse Ends Of Files", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"sec.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"End: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"sec.", None))
        self.groupBox_OnlyReadBetweenMarkers.setTitle(QCoreApplication.translate("MainWindow", u"Only Read Between Markers", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Start Phrase:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Start Analysis", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"End Phrase:  ", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"End Analysis", None))
        self.groupBox_UseTakeMarkers.setTitle(QCoreApplication.translate("MainWindow", u"Use Take Markers", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Phrase: ", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Take $num", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Create unique files at take", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2020 Values with this symbol will not be saved to preferences", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_Voice), QCoreApplication.translate("MainWindow", u"Voice", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Conflict Resolution", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_MicList), QCoreApplication.translate("MainWindow", u"Mic List", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Wild Cards", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"UCS Files (.csv)", None))
        self.label_LoadTopLevelCSV.setText(QCoreApplication.translate("MainWindow", u"[file not found]", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Full Translations List:", None))
        self.toolButton_LoadFullCatCSV.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_LoadTransCSV.setText(QCoreApplication.translate("MainWindow", u"[file not found]", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Top Level Categories:", None))
        self.toolButton_LoadTopLevelCSV.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_LoadTransCSV.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_LoadFullCatCSV.setText(QCoreApplication.translate("MainWindow", u"[file not found]", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Full Category List:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"** When importing .csv files, please sure to remove unnecessary rows", None))
        self.tabWidget_Main.setTabText(self.tabWidget_Main.indexOf(self.tab_Settings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

