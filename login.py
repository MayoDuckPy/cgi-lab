#!/usr/bin/env python3
import cgi
import secret

def main():
    request = cgi.parse()
    try:
        username = request['username'][0]
        password = request['password'][0]
    except KeyError:
        print('Content-Type: text/html\n')
        print(f'<p>Username and password must be supplied</p>')
        return

    if username == secret.username and password == secret.password:
        print('Set-Cookie: authenticated=true')
        print('Content-Type: text/html\n')
        return

    print('Content-Type: text/html\n')
    print(f'<p>Login Failed</p>')

if __name__ == '__main__':
    main()
