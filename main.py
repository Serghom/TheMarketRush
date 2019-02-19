import sys
from QTwindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    questWindow = QuestWindow()
    questWindow.show()
    sys.exit(app.exec_())

