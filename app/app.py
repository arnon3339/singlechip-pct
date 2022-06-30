from .modules import mywidgets
from PyQt5.QtWidgets import QApplication
import sys

def run():
    app = QApplication(sys.argv)
    w = mywidgets.MyWidget()
    w.show()
    sys.exit(app.exec_())