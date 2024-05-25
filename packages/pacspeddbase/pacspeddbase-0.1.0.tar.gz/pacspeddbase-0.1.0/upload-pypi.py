import os
import subprocess
import sys

if __name__ == '__main__':
    option = sys.argv[1]
    if option in ['view', 'show', 'list']:
        subprocess.run(['gh', 'workflow', 'view'])
    elif option in ['setup', 'pypi']:
        subprocess.run(['python', '-m', 'pip', 'install', 'twine'])
        token = sys.argv[2]
        HOME = os.environ.get(['HOME'])
        PYPIRC = os.path.join(HOME, '.pypirc')
        with open(PYPIRC, 'w') as f:
            text1 = "[pypi]"
            text2 = "username = __token__"
            text3 = f"password = {token}"
            f.write(text1)
            f.write(text2)
            f.write(text3)
    elif option in ['upload', 'publish']:
        pid = sys.argv[2]
        cdir = os.getcwd()
        build = os.path.join(cdir, 'build')
        os.chdir(build)
        subprocess.run(['gh', 'run', 'download', pid])
        folder = os.listdir(build)
        for fold in folder:
            files = os.listdir(fold)
            for file in files:
                filepath = os.path.join(fold, file)
                subprocess.run(['python', '-m', 'twine', 'upload', filepath])