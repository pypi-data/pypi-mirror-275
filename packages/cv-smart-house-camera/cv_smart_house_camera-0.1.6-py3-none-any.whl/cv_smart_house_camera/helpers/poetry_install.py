import subprocess

def poetry_install(poetry_path,):
    lock = [poetry_path, 'lock']
    install = [poetry_path, 'install']


    result = subprocess.run(lock, capture_output=True, text=True, check=True)
    print(result.stdout)
    result = subprocess.run(install, capture_output=True, text=True, check=True)
    print(result.stdout)
