__author__ = 'pier'

import time
import threading
import socket
import os

PORT = 5022
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", PORT))
sock.listen(10)


class ServerThread(threading.Thread):
    def __init__(self, connection, address):
        super(ServerThread, self).__init__()
        self.path_or = ""
        self.connection = connection
        self.address = address
        self.path_end = ""

    def run(self):
        print("Accepted a connection from " + repr(self.address))

        self.connection.send(str.encode("Connection accepted, send name file"))
        temp = self.connection.recv(512)
        self.path_end = bytes(temp)

        f = open(self.path_end, "wb")

        while True:
            data = self.connection.recv(512)
            if not data:
                break
            f.write(data)

        self.connection.close()
        print("Closing connection...")
        print("Connection with " + repr(self.address,)+" closed")


def main():
    """
            Define main function
    """

    while 1:
        conn, addr = sock.accept()
        client_thread = ServerThread(conn, addr)
        client_thread.start()

if __name__ == '__main__':
    main()

