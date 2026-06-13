#!/usr/bin/python3
"""Module for http server"""

import json
import http.server


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """RequestHandler subclass of BaseHTTPRequestHandler"""
    def do_GET(self):
        """Method to handle GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", 'UTF-8')) 
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('UTF-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("OK", 'UTF-8'))
        elif self.path =="/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('UTF-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", 'UTF-8'))

if __name__ == "__main__":
    server = http.server.HTTPServer(("localhost", 8000), RequestHandler)
    server.serve_forever()
