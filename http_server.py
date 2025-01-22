from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 12245


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())

        elif self.path == '/about':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"О Hac")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(f"Страница не найдена")
            
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Полученные данные:", post_data.decode())

        self.send_response(200)
        self.end_headers()
        response = "Данные получены!"
        self.wfile.write(response.encode())


if __name__ == "__main__":
    httpd = HTTPServer(("127.0.0.1", PORT), MyHandler)
    print(f"Сервер запущен на порту {PORT}")
    httpd.serve_forever()