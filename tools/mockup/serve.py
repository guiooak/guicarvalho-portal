"""Serves /mockup on http://localhost:8000 with caching turned off, so the
browser always loads the latest CSS and JS after a regeneration.

    python3 tools/mockup/serve.py [port]
"""
import functools, http.server, os, sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "mockup")


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def log_message(self, *args):
        pass


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
http.server.ThreadingHTTPServer(("", port), functools.partial(NoCache, directory=ROOT)).serve_forever()
