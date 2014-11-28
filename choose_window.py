#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this example, we select a file with a
QtGui.QFileDialog and display its contents
in a QtGui.QTextEdit.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT
import os


class Example(QtGui.QWidget):
    """
            Create a window with a label, a progress
            bar and a button that open a file dialog window

    """
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.file = ""
        self.save_file = ""
        self.lbl = None
        self.lbl_result = None
        self.pbar = None
        self.btn = None
        self.step = 0
        self.data_send = 0
        self.total_data = 0
        self.init_ui()
        self.to_set = 0

    def tempo(self):

        step = int(self.data_send/self.total_data)
        if step >= 100:
            self.timer.stop()
            return

        self.pbar.setValue(step)

    def init_ui(self):

        """
            Initialize the main window

        """
        self.lbl = QtGui.QLabel('No file selected', self)
        self.lbl.setGeometry(0, 0, 300, 20)
        self.lbl_result = QtGui.QLabel("0/0", self)
        self.btn = QtGui.QPushButton("Choose file", self)
        self.btn.clicked.connect(self.show_dialog)
        self.btn.setGeometry(120, 100, 100, 50)
        self.pbar = QtGui.QProgressBar(self)
        self.timer = QtCore.QBasicTimer()
        self.btn.clicked.connect(self.tempo)
        self.pbar.setGeometry(10, 400, 480, 50)
        self.pbar.setValue(0)
        self.lbl_result.setGeometry(0, 450, 500, 50)
        self.lbl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.setGeometry(300, 300, 500, 500)

    def timerEvent(self, e):

        if self.to_set >= 100:
            self.timer.stop()
            self.lbl_result.setText("Transfer complete")
            return
        self.to_set = int((self.data_send/self.total_data)*100)
        self.pbar.setValue(self.to_set)
        self.lbl_result.setText(str(self.data_send) + "/" + str(self.total_data))

    def tempo(self):

        if self.timer.isActive():
            self.timer.stop()

        else:
            self.timer.start(100, self)

    def show_dialog(self):
        """
            Initialize the file dialog window and get file's path
        """
        file = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(),
                                                 'Open file', '/home')
        save_file = QtGui.QFileDialog.getExistingDirectory(QtGui.QFileDialog(), 'Save file directory', '/home',
                                                           QtGui.QFileDialog.ShowDirsOnly)
        self.file = file
        self.save_file = save_file
        if self.file:
            self.lbl.setText(self.file)
            self.total_data = os.stat(self.file).st_size





