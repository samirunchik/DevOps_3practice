from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        if self.path == '/health':
            self.wfile.write(b'OK')
        elif self.path == '/api/data':
            self.wfile.write(b'{"status": "connected"}')
        elif self.path == '/api/items/count':
            self.wfile.write(b'2')
        else:
            self.wfile.write(b'Hello DevOps')

HTTPServer(('0.0.0.0', 3000), Handler).serve_forever()
