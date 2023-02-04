"""Simple authentication routine for network services."""
import hmac
import os


def client_authenticate(connection, secret_key):
    """Authenticate client to a remote service.
    
    `connection` represents a network connection; `secret_key` is a key
    known only to both client/server.
    """
    message = connection.recv(32)
    _hash = hmac.new(secret_key, message)
    digest = _hash.digest()
    connection.send(digest)


def server_authenticate(connection, secret_key):
    """Request client authentication."""
    message = os.urandom(32)
    connection.send(message)
    _hash = hmac.new(secret_key, message)
    digest = _hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)
