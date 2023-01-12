import preinstall
import time
import subprocess
import PySide6
from PyQt5 import QtWidgets, uic
import os
import json
import sys


preinstall.pre()
preinstall.git()
preinstall.bucketadd()

class Ui(QtWidgets.QMainWindow):
    def __init__(main):
        super(Ui, main).__init__()
        uic.loadUi('browsers.ui', main)
        
        # Buttons Functions

        def brave():
            browser = subprocess.Popen('scoop install brave', shell=True)
            browser.wait()

        def chrome():
            browser = subprocess.Popen('scoop install googlechrome', shell=True)
            browser.wait()

        def firefox():
            browser = subprocess.Popen('scoop install firefox', shell=True)
            browser.wait()

        def opera():
            browser = subprocess.Popen('scoop install opera', shell=True)
            browser.wait()

        def operagx():
            browser = subprocess.Popen('scoop install operagx', shell=True)
            browser.wait()

        def vivaldi():
            browser = subprocess.Popen('scoop install vivaldi', shell=True)
            browser.wait()

        main.pushButton.clicked.connect(brave)
        main.pushButton_2.clicked.connect(chrome)
        main.pushButton_3.clicked.connect(firefox)
        main.pushButton_4.clicked.connect(opera)
        main.pushButton_5.clicked.connect(operagx)
        main.pushButton_6.clicked.connect(vivaldi)

        # Show Window

        main.show()
        sys.exit(super.exec_())
