from http.server import
simpleHTTPRequestHandler, HTTPServer

Server = HTTPServer (("localhost", 8000),
SimpleHTTPRequestHandler)

Print("Northstar support portal running at Http://localhost:8000")
Server.serve_forever()
