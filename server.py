from http.server import HTTP server, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer (server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
