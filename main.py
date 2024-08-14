import sys
from multiprocessing import freeze_support

from PyQt5.QtWidgets import QApplication

from home.view.ViewHome import ViewHome

if __name__ == '__main__':
    freeze_support()
    app = QApplication(sys.argv)
    vista_home = ViewHome()
    vista_home.showMaximized()
    sys.exit(app.exec())
