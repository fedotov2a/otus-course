import socket
import re
from pprint import pprint
from http import HTTPStatus


end_of_stream = '\r\n\r\n'

def handle_client(connection, client_address):
    client_data = ''

    with connection:
        while True:
            data = connection.recv(1024)

            print('Received:', data)

            if not data:
               break

            client_data += data.decode()

            if end_of_stream in client_data:
                break

        client_data = client_data.split('\n')

        templates = [
            re.compile('(?P<method>\w+)\s(\/.*status=(?P<code>\d+).*|.*[^status].*)\\r$'),
            re.compile('^(?P<header>\S+:.*)\\r$')
        ]

        method = None
        code = None
        status_code = None
        host = None
        headers = []

        for data in client_data:
            if data == '\r':
                break

            for template in templates:
                res = template.match(data)

                if res is None:
                    continue

                res = res.groupdict()

                if 'header' in res:
                    headers.append(res['header'])
                elif 'method' in res and 'code' in res:
                    method = res['method']
                    code = res['code']

        code = 200 if code is None else int(code)
        status_code = next(filter(lambda s: s == code, list(HTTPStatus)), None)

        if status_code is None:
            code = 200
            status_code = 'OK'
        else:
            status_code = status_code.phrase

        http_response = (
            'HTTP/1.0 200 OK\r\n'
            'Content-Type: text/html; charset=UTF-8\r\n'
            '\r\n'
            f'Request Method: {method}\r\n'
            f'Request Source: ({client_address})\r\n'
            f'Response Status: {code} {status_code}\r\n'
        )

        for header in headers:
            http_response += header + '\r\n'

        http_response += '\r\n\r\n'
        connection.send(http_response.encode('utf-8'))


with socket.socket() as server_sock:
    server_sock.bind(('127.0.0.1', 40404));
    server_sock.listen();

    while True:
        client_sock, client_address = server_sock.accept();
        handle_client(client_sock, client_address)
        print(f'Sent data to {client_sock}');
