#python 自带WEB服务器,该web服务器包含在http.server库模块中
#导入HTTP服务器、CGI模块
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8089
#创建一个HTTP服务器
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
#显示友好消息，并启动服务器
print("Starting simple_httpd on address: " + str(httpd.server_address))
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

