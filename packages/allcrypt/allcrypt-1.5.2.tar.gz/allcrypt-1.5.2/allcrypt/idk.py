import PySimpleGUI as sg
import re
import os
import gzip
import psutil
import ctypes
import subprocess
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64


def main():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('USB Drive: Not Found', key='-USB-')],
        [sg.Text('Enter a message or encrypted bytes:')],
        [sg.InputText('Enter a message or encrypted bytes...', key='-MESSAGE-', size=(40, 5), justification='left', text_color='grey')],
        [sg.Button('Encrypt Message'), sg.Button('Decrypt Message')],
        [sg.Button('Encrypt File'), sg.Button('Decrypt File')],
        [sg.Button('Generate New Key for this USB')],
        [sg.Text(size=(40, 5), key='-OUTPUT-')],
    ]

    window = sg.Window('Allcrypt Encryption/Decryption', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Encrypt Message':
            encrypt_message(values['-MESSAGE-'])

        if event == 'Decrypt Message':
            decrypt_message(values['-MESSAGE-'])

    window.close()


def encrypt_message(message):
    try:
        key = get_key_from_usb(get_usb_drive(), get_password())
        fernet = Fernet(key)
        encrypted_bytes = fernet.encrypt(message.encode()).decode()
        sg.popup_ok('Encrypted Message:\n' + encrypted_bytes)
    except Exception as e:
        sg.popup_error(f'Encryption failed. Error: {str(e)}')


def decrypt_message(message):
    try:
        key = get_key_from_usb(get_usb_drive(), get_password())
        fernet = Fernet(key)
        decrypted_string = fernet.decrypt(message.encode()).decode()
        sg.popup_ok('Decrypted Message:\n' + decrypted_string)
    except Exception as e:
        sg.popup_error(f'Decryption failed. Error: {str(e)}')


def get_usb_drive():
    if sys.platform.startswith('win'):
        drives = psutil.disk_partitions()
        
        for drive in drives:
            if 'removable' in drive.opts:
                return drive.mountpoint
        raise FileNotFoundError("No USB drive found.")
    elif sys.platform.startswith('linux'):
        output = subprocess.run(['lsblk', '-o', 'NAME,MOUNTPOINT', '-p', '-n'], capture_output=True, text=True)
        lines = output.stdout.split('\n')
        usb_devices = []
        for line in lines:
            if '/media/' in line:
                usb_devices.append(line.strip().split()[-1])
        if usb_devices:
            return usb_devices[0]
        else:
            raise FileNotFoundError("No USB drive found.")
    else:
        raise NotImplementedError("USB drive detection and Allcrypt is not supported on this platform.")


def get_key_from_usb(usb_path, password):
    try:
        return decrypt_key_with_password(usb_path, password)
    except FileNotFoundError:
        raise FileNotFoundError("Encrypted key file not found on the USB drive.")
    except Exception as e:
        raise Exception(f"Error decrypting key: {str(e)}")


def decrypt_key_with_password(usb_path, password):
    with open(os.path.join(usb_path, "encrypted_key.key"), "rb") as encrypted_key_file:
        data = encrypted_key_file.read()
        salt = data[:16]
        encrypted_key = data[16:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000, 
        salt=salt,
        length=32,
        backend=default_backend()

    )
    key_derived = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    decrypted_key = Fernet(key_derived).decrypt(encrypted_key)
    return decrypted_key


def get_password():
    password = sg.popup_get_text('Enter your password:', password_char='*')
    return password


if __name__ == '__main__':
    main()
