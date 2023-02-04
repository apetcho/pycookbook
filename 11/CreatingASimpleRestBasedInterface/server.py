#!/usr/bin/env python3
import cgi


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
