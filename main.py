"""Launch the prototype landing page with Python's standard library."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


if __name__ == '__main__':
    os.chdir(Path(__file__).resolve().parent)
    host, port = '127.0.0.1', 8000
    print(f'УчиЛесно: http://{host}:{port}', flush=True)
    ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler).serve_forever()
