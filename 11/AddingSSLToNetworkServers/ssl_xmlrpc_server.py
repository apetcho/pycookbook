#!/usr/bin/env python3
"""An example of an SSL-XMLRPC Server."""
import ssl
from xmlrpc.server import SimpleXMLRPCServer
from sslmixin import SSLMixin


class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


class KeyValueServer:
    _rpc_methods_ = ["get", "set", "delete", "exists", "keys"]

    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]
    
    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exits(self, name):
        return name in self._data
    
    def keys(self):
        return list(self._data)
    
    def serve_forever(self):
        self._serv.serve_forever()


def main():
    """Main entry."""
    KEYFILE = "server_key.pem"
    CERTFILE = "server_cert.pem"
    CA_CERTS = "client_cert.pem"

    kvserv = KeyValueServer(
        ("", 15000), keyfile=KEYFILE, certfile=CERTFILE,
        ca_certs=CA_CERTS, cert_reqs=ssl.CERT_REQUIRED,
    )
    kvserv.serve_forever()


if __name__ == "__main__":
    main()
