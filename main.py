import sys
from multiprocessing import freeze_support

sys.path.append('/usr/local/lib/python3.9/site-packages')

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

from home.view.ViewHome import ViewHome

if __name__ == '__main__':
    freeze_support()
    QCoreApplication.setApplicationName("MyApp")
    app = QApplication(sys.argv)
    view_home = ViewHome()
    view_home.showMaximized()
    sys.exit(app.exec())
