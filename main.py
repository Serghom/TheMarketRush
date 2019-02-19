import sys
import vkToken
import theMarketRush
from QTwindow import *
# theMarketRush.mainFunction()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    questWindow = QuestWindow()
    questWindow.show()
    sys.exit(app.exec_())

