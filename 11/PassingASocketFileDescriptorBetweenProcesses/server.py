#!/usr/bin/env python3
from io import FileIO
import socket
import struct
import signal
import sys


def _sighandler(num, args):
    if num == signal.SIGINT:
        sys.exit(0)


def send_fd(sock:socket.socket, fd:FileIO):
    """Send a single file descriptor."""
    sock.sendmsg(
        [b"x"],
        [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack('i', fd))]
    )
    ack = sock.recv(2)
    assert ack == b"OK"


def server(work_addr, port):
    """Wait for the worker to connect."""
    work_serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    work_serv.bind(work_addr)
    work_serv.listen(1)
    worker, addr = work_serv.accept()
    # -*- Now run a TCP/IP server and send clients to worker -*-
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        sock.bind(("", port))
        sock.listen(1)
        while True:
            client, addr = sock.accept()
            print(f"SERVER: Got connection from {addr}")
            send_fd(worker, client.fileno())
            client.close()


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, _sighandler)
    worker_addr = ("", 3000)
    port = 6000
    server(worker_addr, port)


if __name__ == "__main__":
    main()
