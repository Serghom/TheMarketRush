from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from UI.windowPy.quest import Ui_QuestWindow
import vkToken
import theMarketRush
import config

class QuestWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.qu = Ui_QuestWindow()
        self.qu.setupUi(self)

        self.qu.radioButton_2.setChecked(True)
        self.setAutorized()

        self.qu.radioButton_2.toggled.connect(self.setLabel)
        self.qu.radioButton.toggled.connect(self.setLabel)

        self.qu.pushButton.clicked.connect(self.vk)

    def setAutorized(self):
        try:
            vkToken.readToken()
            self.qu.radioButton_2.setText('Авторизация через ВКонтакте (Вы уже авторизированы)')
        except:
            pass

    def setLabel(self):
        if self.qu.radioButton_2.isChecked():
            self.qu.label.setText('Это нужно для того чтобы мы видили сколько шмота ты прикупил')
        else:
            self.qu.label.setText('В данном случае твое очко будет утеряно в безднах этого говнокода')

    def vk(self):
        if self.qu.radioButton_2.isChecked():
            print(vkToken.getToken())
            config.isAuthorized = True
            theMarketRush.mainFunction()

        else:
            theMarketRush.mainFunction()
        self.close()
