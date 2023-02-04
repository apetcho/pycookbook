#!/usr/bin/env python3
"""An XML_RPC client that verifies the server certificate."""
from xmlrpc.client import SafeTransport, ServerProxy
import ssl


class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        super().__init__()
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        sock = super().make_connection(host, {"context": self._ssl_context})
        return sock
    

def main():
    """Main entry."""
    # -*- Create the client proxy
    serv = ServerProxy(
        "https://localhost:15000",
        transport=VerifyCertSafeTransport(
            "server_cert.pem", "client_cert.pem", "client_key.pem"
        ),
        allow_none=True
    )
    serv.set("foo", "bar")
    serv.set("spam", [1, 2, 3])
    print(serv.keys())
    print(serv.get("foo"))
    print(serv.get("spam"))
    serv.delete("spam")
    print(serv.exists("spam"))
    

if __name__ == "__main__":
    main()
