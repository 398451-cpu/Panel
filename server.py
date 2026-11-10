"""Serve the imported login page without exposing workspace files."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PAGE = Path(__file__).with_name("login.html")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?", 1)[0] not in ("/", "/login.html"):
            self.send_error(404)
            return
        content = PAGE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    print("Serving the login page on port 5000", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
