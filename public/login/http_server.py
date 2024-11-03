import http.server
import socketserver
import os

directory_to_serve = "//root/PP/public/login"

os.chdir(directory_to_serve)

PORT = 9004

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()