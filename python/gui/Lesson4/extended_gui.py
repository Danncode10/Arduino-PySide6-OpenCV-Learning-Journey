# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extended_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLCDNumber,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QScrollBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(358, 315)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.led_label = QLabel(self.centralwidget)
        self.led_label.setObjectName(u"led_label")

        self.gridLayout.addWidget(self.led_label, 0, 0, 1, 1)

        self.red_label = QLabel(self.centralwidget)
        self.red_label.setObjectName(u"red_label")

        self.gridLayout.addWidget(self.red_label, 1, 0, 1, 1)

        self.red_value = QLCDNumber(self.centralwidget)
        self.red_value.setObjectName(u"red_value")

        self.gridLayout.addWidget(self.red_value, 1, 2, 1, 1)

        self.blue_label = QLabel(self.centralwidget)
        self.blue_label.setObjectName(u"blue_label")

        self.gridLayout.addWidget(self.blue_label, 3, 0, 1, 1)

        self.green_label = QLabel(self.centralwidget)
        self.green_label.setObjectName(u"green_label")

        self.gridLayout.addWidget(self.green_label, 2, 0, 1, 1)

        self.btn_led_toggle = QPushButton(self.centralwidget)
        self.btn_led_toggle.setObjectName(u"btn_led_toggle")
        self.btn_led_toggle.setCheckable(True)

        self.gridLayout.addWidget(self.btn_led_toggle, 0, 1, 1, 1)

        self.green_value = QLCDNumber(self.centralwidget)
        self.green_value.setObjectName(u"green_value")

        self.gridLayout.addWidget(self.green_value, 2, 2, 1, 1)

        self.blue_value = QLCDNumber(self.centralwidget)
        self.blue_value.setObjectName(u"blue_value")

        self.gridLayout.addWidget(self.blue_value, 3, 2, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)

        self.blue_scroll = QScrollBar(self.centralwidget)
        self.blue_scroll.setObjectName(u"blue_scroll")
        self.blue_scroll.setMaximum(255)
        self.blue_scroll.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.blue_scroll, 3, 1, 1, 1)

        self.green_scroll = QScrollBar(self.centralwidget)
        self.green_scroll.setObjectName(u"green_scroll")
        self.green_scroll.setMaximum(255)
        self.green_scroll.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.green_scroll, 2, 1, 1, 1)

        self.signal_placeholder = QLabel(self.centralwidget)
        self.signal_placeholder.setObjectName(u"signal_placeholder")

        self.gridLayout.addWidget(self.signal_placeholder, 4, 2, 1, 1)

        self.red_scroll = QScrollBar(self.centralwidget)
        self.red_scroll.setObjectName(u"red_scroll")
        self.red_scroll.setMaximum(255)
        self.red_scroll.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.red_scroll, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 358, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.blue_scroll.actionTriggered.connect(self.blue_value.display)
        self.green_scroll.actionTriggered.connect(self.green_value.display)
        self.red_scroll.actionTriggered.connect(self.red_value.display)
        self.btn_led_toggle.clicked.connect(self.signal_placeholder.clear)
        self.comboBox.activated.connect(self.signal_placeholder.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Buzzer", None))
        self.led_label.setText(QCoreApplication.translate("MainWindow", u"LED:", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.btn_led_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle LED", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Beep", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Alarm", None))

        self.signal_placeholder.setText("")
    # retranslateUi

