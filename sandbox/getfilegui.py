#!/usr/bin/env python3
import os
import sys
import time
import socket
import tkinter as tk
import tkinter.messagebox as mbox
from threading import Thread
from typing import Dict, List, Optional


class Form:
    EntrySize = 40

    def __init__(self, labels:List[str], parent=None):
        labelsize = max(len(x) for x in labels) + 2
        self._box = box = tk.Frame(parent)
        box.pack(expand=tk.YES, fill=tk.X)
        rows = tk.Frame(box, bd=2, relief=tk.GROOVE)
        rows.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)
        self.content:Dict[str, tk.Entry] = {}
        for label in labels:
            row = tk.Frame(rows)
            row.pack(fill=tk.X)
            tk.Label(row, text=label, width=labelsize).pack(side=tk.LEFT)
            entry = tk.Entry(row, width=Form.EntrySize)
            entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            self.content[label] = entry
        tk.Button(
            box, text="Cancel", command=self.on_cancel
        ).pack(side=tk.RIGHT)
        tk.Button(
            box, text="Submit", command=self.on_submit
        ).pack(side=tk.RIGHT)
        box.master.bind("<Return>", (lambda event: self.on_submit()))

    def on_submit(self):
        for key in self.content:
            print(f"{key} --> {self.content[key].get()}")

    def on_cancel(self):
        self._box.master.quit()


class Network:
    BUFSIZE = 1024
    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 5500


    def __init__(self):
        self._port = None
        self._host = None

    @property
    def port(self):
        return self._port
    
    @property
    def host(self):
        return self._host

    @staticmethod
    def now():
        return time.asctime(time.localtime())
    
    @staticmethod
    def handle_client(filename, host=None, port=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = host or Network.DEFAULT_HOST
        port = port or Network.DEFAULT_PORT
        sock.connect((host, port))
        sock.send(f"{filename}\n".encode("utf-8"))
        dropdir = os.path.split(filename)[1]
        with open(dropdir, "wb") as fp:
            while True:
                data = sock.recv(Network.BUFSIZE)
                if not data:
                    break
                fp.write(data)
            sock.close()
        print(f"Client go {filename} at {Network.now()}")

    @staticmethod
    def server_thread_target(clientsock:socket.socket):
        sockfile = clientsock.makefile("r")
        filename = sockfile.readline()[:-1]
        try:
            with open(filename, "rb") as fp:
                while True:
                    data = fp.read(Network.BUFSIZE)
                    if not data:
                        break
                    sent = clientsock.send(data)
                    assert sent==len(data)
        except Exception as err:
            print(f"Error downloading file on server: {filename}")
        clientsock.close()

    def run_forever(self, host, port):
        self._host = host
        self._port = port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(5)
        while True:
            clientsock, clientaddr = sock.accept()
            print(f"{clientaddr} connected to server at {Network.now()}")
            thd = Thread(target=Network.handle_client, args=(clientsock,))
            thd.daemon = True
            thd.start()


class GetfileForm(Form):
    def __init__(self, oneshot=False):
        self._root = root = tk.Tk()
        root.wm_title("Getfile App")
        labels = ["Server Name", "Port Number", "File Name", "Local Dir?"]
        Form.__init__(self, labels, root)
        self.oneshot = oneshot
        self._host = labels[0]
        self._port = labels[1]
        self._filename = labels[2]
        self._localdir = labels[3]

    def on_submit(self):
        Form.on_submit(self)
        localdir = self.content[self._localdir].get()
        portnum = int(self.content[self._port].get())
        server = self.content[self._host].get()
        filename = self.content[self._filename].get()
        if localdir:
            os.chdir(localdir)
        Network.handle_client(server, portnum, filename)
        mbox.showinfo("GetFileApp", "Download complete")
        if self.oneshot:
            self._root.quit()


def netdemo():
    server:Optional[Network] = None
    args = sys.argv[1:]
    host, port, filename = None, None, None
    if "-host" in args:
        idx = args.index("-host")
        host = args[(idx+1)]
    if "-port" in args:
        idx = args.index("-port")
        port = int(args[(idx+1)])

    if "-file" in args:
        idx = args.index("-file")
        filename = args[(idx+1)]

    if host is None or host == "localhost":
        host = ""
        port = port or Network.DEFAULT_PORT
    if filename is None:
        # Network.run_forever(host, port)
        server = Network()
        server.run_forever(host, port)
    else:
        port = port or Network.DEFAULT_PORT
        host = host or Network.DEFAULT_HOST
        Network.handle_client(host, port, filename)
    

if __name__ == "__main__":
    netdemo()
