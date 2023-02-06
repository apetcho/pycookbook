#!usr/bin/env python3
import socket
import struct
import signal
import sys


def _sighandler(num, arg):
    if num == signal.SIGINT:
        sys.exit(0)


def recv_fd(sock: socket.socket):
    """Receive a single file descriptor."""
    msg, ancdata, flags, addr = sock.recvmsg(
        1, socket.CMSG_LEN(struct.calcsize("i"))
    )
    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level==socket.SOL_SOCKET and cmsg_type==socket.SCM_RIGHTS
    sock.sendall(b"OK")
    return struct.unpack("i", cmsg_data)[0]


def worker(server_addr):
    serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serv.connect(server_addr)
    while True:
        fd = recv_fd(serv)
        print(f"WORKER: Got fd {fd}")
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, fileno=fd
        ) as client:
            msg = client.recv(1024)
            if not msg:
                break
            print(f"WORKER: Received {msg!r}")
            client.send(msg)


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, _sighandler)
    server_addr = ("", 6000)
    worker(server_addr)


if __name__ == "__main__":
    main()
