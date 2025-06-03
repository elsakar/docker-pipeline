# From https://gist.github.com/davidbgk/b10113c3779b8388e96e6d0c44e03a74
import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'''<HTML>
        <BODY style="background:lightsalmon">
        Hello world from Mael THT.
        </BODY></HTML>''')


httpd = socketserver.TCPServer(('', 5000), Handler)
httpd.serve_forever()
