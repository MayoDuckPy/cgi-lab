#!/usr/bin/env python3
import os
import secret

from templates import login_page, secret_page

env = dict(os.environ)

def get_environ_json():
    env_len = len(env)
    print('Content-Type: application/json\n')

    print('{')
    for i, key in enumerate(env):
        value = env[key].replace('"', '\\"')
        var = f'"{key}": "{value}"'
        if i+1 != env_len:
            var += ','

        print(var)
    print('}')

def main():
    # Check if user has auth cookie
    print('Content-Type: text/html\n')
    try:
        cookies = env['HTTP_COOKIE'].replace(' ', '').split(';')
        for cookie in cookies:
            cookie = cookie.split('=')
            if cookie[0] == 'authenticated' and cookie[1] == 'true':
                return print(secret_page(secret.username, secret.password))

    except KeyError:
        # No cookie; continue regular execution
        pass  

    print(login_page())

if __name__ == '__main__':
    main()
