# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_of_Map.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyMap(object):
    def setupUi(self, MyMap):
        MyMap.setObjectName("MyMap")
        MyMap.resize(841, 694)
        MyMap.setAutoFillBackground(False)
        MyMap.setStyleSheet("background:url(C:/Users/Administrator/Desktop/Distribution of cameras.jpg)")
        self.cam_24 = QtWidgets.QRadioButton(MyMap)
        self.cam_24.setGeometry(QtCore.QRect(36, 120, 16, 16))
        self.cam_24.setAutoFillBackground(False)
        self.cam_24.setStyleSheet("")
        self.cam_24.setText("")
        self.cam_24.setObjectName("cam_24")
        self.label_cam24 = QtWidgets.QLabel(MyMap)
        self.label_cam24.setGeometry(QtCore.QRect(40, 140, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam24.setPalette(palette)
        self.label_cam24.setAutoFillBackground(True)
        self.label_cam24.setStyleSheet("background: url();")
        self.label_cam24.setObjectName("label_cam24")
        self.cam_25 = QtWidgets.QRadioButton(MyMap)
        self.cam_25.setGeometry(QtCore.QRect(380, 180, 16, 16))
        self.cam_25.setAutoFillBackground(False)
        self.cam_25.setStyleSheet("")
        self.cam_25.setText("")
        self.cam_25.setObjectName("cam_25")
        self.label_cam25 = QtWidgets.QLabel(MyMap)
        self.label_cam25.setGeometry(QtCore.QRect(380, 200, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam25.setPalette(palette)
        self.label_cam25.setAutoFillBackground(True)
        self.label_cam25.setStyleSheet("background: url();")
        self.label_cam25.setObjectName("label_cam25")
        self.cam_18 = QtWidgets.QRadioButton(MyMap)
        self.cam_18.setGeometry(QtCore.QRect(440, 180, 16, 16))
        self.cam_18.setAutoFillBackground(False)
        self.cam_18.setStyleSheet("")
        self.cam_18.setText("")
        self.cam_18.setObjectName("cam_18")
        self.label_cam18 = QtWidgets.QLabel(MyMap)
        self.label_cam18.setGeometry(QtCore.QRect(440, 200, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam18.setPalette(palette)
        self.label_cam18.setAutoFillBackground(True)
        self.label_cam18.setStyleSheet("background: url();")
        self.label_cam18.setObjectName("label_cam18")
        self.cam_36 = QtWidgets.QRadioButton(MyMap)
        self.cam_36.setGeometry(QtCore.QRect(410, 160, 16, 16))
        self.cam_36.setAutoFillBackground(False)
        self.cam_36.setStyleSheet("")
        self.cam_36.setText("")
        self.cam_36.setObjectName("cam_36")
        self.label_cam36 = QtWidgets.QLabel(MyMap)
        self.label_cam36.setGeometry(QtCore.QRect(410, 140, 16, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam36.setPalette(palette)
        self.label_cam36.setAutoFillBackground(True)
        self.label_cam36.setStyleSheet("background: url();")
        self.label_cam36.setObjectName("label_cam36")
        self.cam_20 = QtWidgets.QRadioButton(MyMap)
        self.cam_20.setGeometry(QtCore.QRect(780, 120, 16, 16))
        self.cam_20.setAutoFillBackground(False)
        self.cam_20.setStyleSheet("")
        self.cam_20.setText("")
        self.cam_20.setObjectName("cam_20")
        self.label_cam20 = QtWidgets.QLabel(MyMap)
        self.label_cam20.setGeometry(QtCore.QRect(780, 140, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam20.setPalette(palette)
        self.label_cam20.setAutoFillBackground(True)
        self.label_cam20.setStyleSheet("background: url();")
        self.label_cam20.setObjectName("label_cam20")
        self.cam_27 = QtWidgets.QRadioButton(MyMap)
        self.cam_27.setGeometry(QtCore.QRect(450, 280, 16, 16))
        self.cam_27.setAutoFillBackground(False)
        self.cam_27.setStyleSheet("")
        self.cam_27.setText("")
        self.cam_27.setObjectName("cam_27")
        self.label_cam27 = QtWidgets.QLabel(MyMap)
        self.label_cam27.setGeometry(QtCore.QRect(450, 300, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam27.setPalette(palette)
        self.label_cam27.setAutoFillBackground(True)
        self.label_cam27.setStyleSheet("background: url();")
        self.label_cam27.setObjectName("label_cam27")
        self.cam_28 = QtWidgets.QRadioButton(MyMap)
        self.cam_28.setGeometry(QtCore.QRect(450, 420, 16, 16))
        self.cam_28.setAutoFillBackground(False)
        self.cam_28.setStyleSheet("")
        self.cam_28.setText("")
        self.cam_28.setObjectName("cam_28")
        self.label_cam28 = QtWidgets.QLabel(MyMap)
        self.label_cam28.setGeometry(QtCore.QRect(470, 420, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam28.setPalette(palette)
        self.label_cam28.setAutoFillBackground(True)
        self.label_cam28.setStyleSheet("background: url();")
        self.label_cam28.setObjectName("label_cam28")
        self.cam_19 = QtWidgets.QRadioButton(MyMap)
        self.cam_19.setGeometry(QtCore.QRect(40, 580, 16, 16))
        self.cam_19.setAutoFillBackground(False)
        self.cam_19.setStyleSheet("")
        self.cam_19.setText("")
        self.cam_19.setObjectName("cam_19")
        self.label_cam19 = QtWidgets.QLabel(MyMap)
        self.label_cam19.setGeometry(QtCore.QRect(40, 560, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam19.setPalette(palette)
        self.label_cam19.setAutoFillBackground(True)
        self.label_cam19.setStyleSheet("background: url();")
        self.label_cam19.setObjectName("label_cam19")
        self.cam_17 = QtWidgets.QRadioButton(MyMap)
        self.cam_17.setGeometry(QtCore.QRect(380, 520, 16, 16))
        self.cam_17.setAutoFillBackground(False)
        self.cam_17.setStyleSheet("")
        self.cam_17.setText("")
        self.cam_17.setObjectName("cam_17")
        self.label_cam17 = QtWidgets.QLabel(MyMap)
        self.label_cam17.setGeometry(QtCore.QRect(360, 530, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam17.setPalette(palette)
        self.label_cam17.setAutoFillBackground(True)
        self.label_cam17.setStyleSheet("background: url();")
        self.label_cam17.setObjectName("label_cam17")
        self.cam_37 = QtWidgets.QRadioButton(MyMap)
        self.cam_37.setGeometry(QtCore.QRect(410, 540, 16, 16))
        self.cam_37.setAutoFillBackground(False)
        self.cam_37.setStyleSheet("")
        self.cam_37.setText("")
        self.cam_37.setObjectName("cam_37")
        self.label_cam25_2 = QtWidgets.QLabel(MyMap)
        self.label_cam25_2.setGeometry(QtCore.QRect(410, 560, 16, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam25_2.setPalette(palette)
        self.label_cam25_2.setAutoFillBackground(True)
        self.label_cam25_2.setStyleSheet("background: url();")
        self.label_cam25_2.setObjectName("label_cam25_2")
        self.cam_23 = QtWidgets.QRadioButton(MyMap)
        self.cam_23.setGeometry(QtCore.QRect(440, 520, 16, 16))
        self.cam_23.setAutoFillBackground(False)
        self.cam_23.setStyleSheet("")
        self.cam_23.setText("")
        self.cam_23.setObjectName("cam_23")
        self.label_cam23 = QtWidgets.QLabel(MyMap)
        self.label_cam23.setGeometry(QtCore.QRect(460, 530, 16, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam23.setPalette(palette)
        self.label_cam23.setAutoFillBackground(True)
        self.label_cam23.setStyleSheet("background: url();")
        self.label_cam23.setObjectName("label_cam23")
        self.cam_21 = QtWidgets.QRadioButton(MyMap)
        self.cam_21.setGeometry(QtCore.QRect(780, 580, 16, 16))
        self.cam_21.setAutoFillBackground(False)
        self.cam_21.setStyleSheet("")
        self.cam_21.setText("")
        self.cam_21.setObjectName("cam_21")
        self.label_cam21 = QtWidgets.QLabel(MyMap)
        self.label_cam21.setGeometry(QtCore.QRect(780, 560, 16, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_cam21.setPalette(palette)
        self.label_cam21.setAutoFillBackground(True)
        self.label_cam21.setStyleSheet("background: url();")
        self.label_cam21.setObjectName("label_cam21")

        self.retranslateUi(MyMap)
        QtCore.QMetaObject.connectSlotsByName(MyMap)

    def retranslateUi(self, MyMap):
        _translate = QtCore.QCoreApplication.translate
        MyMap.setWindowTitle(_translate("MyMap", "Distribution of cameras"))
        self.label_cam24.setText(_translate("MyMap", "24"))
        self.label_cam25.setText(_translate("MyMap", "25"))
        self.label_cam18.setText(_translate("MyMap", "18"))
        self.label_cam36.setText(_translate("MyMap", "36"))
        self.label_cam20.setText(_translate("MyMap", "20"))
        self.label_cam27.setText(_translate("MyMap", "27"))
        self.label_cam28.setText(_translate("MyMap", "28"))
        self.label_cam19.setText(_translate("MyMap", "19"))
        self.label_cam17.setText(_translate("MyMap", "17"))
        self.label_cam25_2.setText(_translate("MyMap", "35"))
        self.label_cam23.setText(_translate("MyMap", "23"))
        self.label_cam21.setText(_translate("MyMap", "21"))

