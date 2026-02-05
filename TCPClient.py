import socket
import json
from urllib.parse import urlparse

HOST = '127.0.0.1'
PORT = 5000


def urlParser(url):
    parsed = urlparse(url)

    return {
        "scheme": parsed.scheme,
        "netloc": parsed.netloc,
        "path": parsed.path,
        "query": parsed.query,
        "fragment": parsed.fragment
    }


url = "https://www.example.com/path/page?name=parth#section1"

url_dict = urlParser(url)
json_data = json.dumps(url_dict)

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.sendall(json_data.encode("utf-8"))

    print("URL parts sent to server.")

    client_socket.close()

except ConnectionRefusedError:
    print("Server is not running.")
