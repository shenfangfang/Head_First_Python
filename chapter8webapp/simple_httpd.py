#python 自带服务器simplehttpd.py
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8089

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

