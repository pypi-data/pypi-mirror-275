import zipfile
import os

def find_password(zip_file, passwords, silent=False, only_pass=False):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for password in passwords:
                try:
                    zip_ref.extractall(pwd=password.encode())
                    if not only_pass:
                        print(f"Correct password found: {password}")
                    return password
                except Exception:
                    if not silent and not only_pass:
                        print(f"Password tried: {password}")
                    elif not silent:
                        print(password)
                    pass
            if not only_pass:
                print("Password not found.")
            return None
    except zipfile.BadZipFile:
        if not silent and not only_pass:
            print("Error: Invalid zip file.")
        return None

def main(zip_file, password_file, silent=False, only_pass=False):
    passwords = []
    if os.path.exists(password_file):
        with open(password_file, 'r') as f:
            passwords = [line.strip() for line in f]

    if passwords:
        found_password = find_password(zip_file, passwords, silent, only_pass)
        if found_password:
            return found_password
        else:
            return None
    else:
        if not silent and not only_pass:
            print("Error: Password file is empty or does not exist.")
        return None
          
