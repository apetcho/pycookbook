#!/usr/bin/env python3
import cgi
import sys
import time
import signal
from wsgiref.simple_server import make_server

def sighandler(num, arg):
    if num == signal.SIGINT:
        sys.exit(0)

def notfound_404(env, startResponse):
    startResponse(
        "404 Not Found",
        [("Content-type", "text/plain")]
    )
    return [b"Not Found"]


class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, env, startResponse):
        path = env["PATH_INFO"]
        params = cgi.FieldStorage(env["wsgi.input"], environ=env)
        method = env["REQUEST_METHOD"].lower()
        env["params"] = {key:params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        handler(env, startResponse)

    def register(self, method, path, fun):
        self.pathmap[method.lower(), path] = fun
        return fun


_helloResponse = """\
<html>
    <head>
        <title>Hello {name}</title>
    </head>
    <body>
        <h1>Hello {name}!</h1>
    </body>
</html>"""


def hello_world(env, startResponse):
    startResponse("200 OK", [("Content-type", "text/html")])
    params = env["params"]
    response = _helloResponse.format(name=params.get("name"))
    yield response.encode("utf-8")


_localtimeResponse = """\
<?xml version="1.0"?>
<time>
    <year>{t.tm_year}</year>
    <month>{t.tm_mon}</month>
    <day>{t.tm_mday}</day>
    <hour>{t.tm_hour}</hour>
    <minute>{t.tm_min}</minute>
    <second>{t.tm_sec}</second>
</time>"""


def localtime(env, startResponse):
    startResponse("200 OK", [("Content-type", "application/xml")])
    response = _localtimeResponse.format(t=time.localtime())
    yield response.encode("utf-8")


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, sighandler)
    # -*- Create the path dispatcher and register functions
    dispatcher = PathDispatcher()
    dispatcher.register("GET", "/hello", hello_world)
    dispatcher.register("GET", "/localtime", localtime)

    # -*- Launch a basic server
    httpd = make_server("", 8080, dispatcher)
    print("Serving on port 8080...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
