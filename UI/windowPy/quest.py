# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuestWindow(object):
    def setupUi(self, QuestWindow):
        QuestWindow.setObjectName("QuestWindow")
        QuestWindow.resize(378, 114)
        self.centralwidget = QtWidgets.QWidget(QuestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        QuestWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QuestWindow)
        QtCore.QMetaObject.connectSlotsByName(QuestWindow)

    def retranslateUi(self, QuestWindow):
        _translate = QtCore.QCoreApplication.translate
        QuestWindow.setWindowTitle(_translate("QuestWindow", "Авторизация кроссовка Назара"))
        QuestWindow.setWindowIcon(QtGui.QIcon('obladaet.ico'))
        self.radioButton_2.setText(_translate("QuestWindow", "Авторизация через ВКонтакте"))
        self.radioButton.setText(_translate("QuestWindow", "Без авторизации"))
        self.label.setText(_translate("QuestWindow", "Это нужно для того чтобы мы видили сколько шмота ты прикупил"))
        self.pushButton.setText(_translate("QuestWindow", "Ok"))

