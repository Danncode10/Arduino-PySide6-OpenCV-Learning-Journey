# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(714, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 646, 591))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.webcam = QLabel(self.widget)
        self.webcam.setObjectName(u"webcam")
        self.webcam.setMinimumSize(QSize(640, 480))

        self.verticalLayout.addWidget(self.webcam)

        self.comboBox_mode = QComboBox(self.widget)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")
        self.comboBox_mode.setMaximumSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.comboBox_mode, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_led_off = QPushButton(self.widget)
        self.button_led_off.setObjectName(u"button_led_off")
        self.button_led_off.setMaximumSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.button_led_off, 0, Qt.AlignmentFlag.AlignHCenter)

        self.button_led_on = QPushButton(self.widget)
        self.button_led_on.setObjectName(u"button_led_on")
        self.button_led_on.setMaximumSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.button_led_on, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 714, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_mode.currentIndexChanged.connect(self.button_led_off.click)
        self.comboBox_mode.currentIndexChanged.connect(self.button_led_on.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.webcam.setText("")
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Manual", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Gesture", None))

        self.button_led_off.setText(QCoreApplication.translate("MainWindow", u"Turn LED ON", None))
        self.button_led_on.setText(QCoreApplication.translate("MainWindow", u"Turn LED ON", None))
    # retranslateUi

