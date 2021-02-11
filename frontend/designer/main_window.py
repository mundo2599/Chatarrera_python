# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend\designer\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("frontend\\designer\\../resources/materiales.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftBar = QtWidgets.QWidget(self.centralwidget)
        self.leftBar.setMinimumSize(QtCore.QSize(50, 0))
        self.leftBar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.leftBar.setObjectName("leftBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftBar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonMateriales = QtWidgets.QPushButton(self.leftBar)
        self.buttonMateriales.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonMateriales.setText("")
        self.buttonMateriales.setIcon(icon)
        self.buttonMateriales.setIconSize(QtCore.QSize(48, 48))
        self.buttonMateriales.setFlat(True)
        self.buttonMateriales.setObjectName("buttonMateriales")
        self.verticalLayout.addWidget(self.buttonMateriales)
        self.labelMateriales = QtWidgets.QLabel(self.leftBar)
        self.labelMateriales.setObjectName("labelMateriales")
        self.verticalLayout.addWidget(self.labelMateriales)
        self.buttonCompras = QtWidgets.QPushButton(self.leftBar)
        self.buttonCompras.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("frontend\\designer\\../resources/compras.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCompras.setIcon(icon1)
        self.buttonCompras.setIconSize(QtCore.QSize(48, 48))
        self.buttonCompras.setFlat(True)
        self.buttonCompras.setObjectName("buttonCompras")
        self.verticalLayout.addWidget(self.buttonCompras)
        self.labelCompras = QtWidgets.QLabel(self.leftBar)
        self.labelCompras.setObjectName("labelCompras")
        self.verticalLayout.addWidget(self.labelCompras)
        self.buttonVentas = QtWidgets.QPushButton(self.leftBar)
        self.buttonVentas.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("frontend\\designer\\../resources/ventas.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonVentas.setIcon(icon2)
        self.buttonVentas.setIconSize(QtCore.QSize(48, 48))
        self.buttonVentas.setFlat(True)
        self.buttonVentas.setObjectName("buttonVentas")
        self.verticalLayout.addWidget(self.buttonVentas)
        self.labelVentas = QtWidgets.QLabel(self.leftBar)
        self.labelVentas.setObjectName("labelVentas")
        self.verticalLayout.addWidget(self.labelVentas)
        self.buttonConfigs = QtWidgets.QPushButton(self.leftBar)
        self.buttonConfigs.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("frontend\\designer\\../resources/configs.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonConfigs.setIcon(icon3)
        self.buttonConfigs.setIconSize(QtCore.QSize(48, 48))
        self.buttonConfigs.setFlat(True)
        self.buttonConfigs.setObjectName("buttonConfigs")
        self.verticalLayout.addWidget(self.buttonConfigs)
        self.labelConfigs = QtWidgets.QLabel(self.leftBar)
        self.labelConfigs.setObjectName("labelConfigs")
        self.verticalLayout.addWidget(self.labelConfigs)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.leftBar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMateriales.setText(_translate("MainWindow", "Materiales"))
        self.labelCompras.setText(_translate("MainWindow", "Compras"))
        self.labelVentas.setText(_translate("MainWindow", "Ventas"))
        self.labelConfigs.setText(_translate("MainWindow", "Ajustes"))
