import os
import pathlib
import sys

import mysql.connector as mc
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from UI.logged_ui import Ui_mw_logged_in

root_folder = r'{}'.format(pathlib.Path(__file__).parent.absolute().parent)

sys.path.append(os.path.join(root_folder, 'App_main'))
from main import Main


class MainLogged(qtw.QMainWindow, Ui_mw_logged_in):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_icons()

        self.signal = Main()
        self.signal.one_sygnal.connect(self.show)
        self.signal.show()
    
    def setup_icons(self):
        root = r''.format(pathlib.Path(__file__).parent.absolute().parent)
        main_path = os.path.join(root, 'App_icons')
        
        self.setWindowIcon(
            qtg.QIcon('{}\\{}'.format(main_path, 'admin_thumb.png'))
        )




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainLogged()
    # window.show()
    sys.exit(app.exec())
