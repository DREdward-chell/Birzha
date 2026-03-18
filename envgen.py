import os
import sys
import typing as tp

BACKEND_ENV = """
GO_HOST=0.0.0.0
GO_PORT=8080
"""

FRONTEND_ENV = """
HOSTNAME=0.0.0.0
PORT=3000
"""

DOCKER_ENV = """
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8080
FRONTEND_HOST=0.0.0.0
FRONTEND_PORT=3000
"""

def assert_not_exists(file: tp.Union[str, os.PathLike], dir: tp.Union[str, os.PathLike]):
    if file in os.listdir(dir):
        sys.exit(f'File {file} already exists')

def make_file(file: tp.Union[str, os.PathLike], content: str):
    if os.path.exists(file):
        print(f'File {file} already exists', file=sys.stderr)
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    print('Generating environment...')
    make_file('./backend/.env.dev', BACKEND_ENV)
    make_file('./backend/.env.prod', BACKEND_ENV)
    make_file('./frontend/.env.dev', BACKEND_ENV)
    make_file('./frontend/.env.prod', BACKEND_ENV)
    make_file('./.env', DOCKER_ENV)
    print('Done')
