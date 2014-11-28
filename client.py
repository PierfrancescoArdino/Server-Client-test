__author__ = 'pier'
import socket
import choose_window
from PyQt4 import QtGui
import sys
import os

import threading
PORT = 5022
HOST = "127.0.0.1"
data_size = 0


class ClientThread(threading.Thread):
    def __init__(self, gui):
        super(ClientThread, self).__init__()
        self.gui = gui
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_size = 0

    def run(self):
        self.sock.connect((HOST, PORT))
        print(bytes.decode(self.sock.recv(1024)))
        while self.gui.file == "":
            continue
        if self.gui.file:

            print(self.gui.file)
            to_send = self.gui.save_file + "/" + os.path.basename(self.gui.file)
            print(to_send)
            self.sock.send(str.encode(to_send))
            f = open(self.gui.file, "rb")
        while True:
            data = f.readline(512)
            if not data:
                break
            self.gui.data_send += len(data)
            self.sock.send(data)
        self.gui.lbl_result.setText("Transfert Complete")
        print ("file sent")

def main():
    """
            Define main function
    """
    app = QtGui.QApplication(sys.argv)
    application = choose_window.Example()
    application.show()
    client_thread = ClientThread(application)
    client_thread.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()