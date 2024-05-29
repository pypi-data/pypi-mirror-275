import zipfile
import os

def find_password(zip_file, passwords, silent=False, only_pass=False, print_output=True):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for password in passwords:
                try:
                    # Set password without extracting the files
                    zip_ref.setpassword(password.encode())
                    # Try to access a file within the zip
                    zip_ref.testzip()
                    if print_output:
                        if only_pass:
                            print(password)
                        else:
                            print(f"Correct password found: {password}")
                    return password
                except Exception:
                    if not silent and not only_pass and print_output:
                        print(f"Password tried: {password}")
                    pass
            if not only_pass and print_output:
                print("Password not found.")
            return None
    except zipfile.BadZipFile:
        if not silent and not only_pass and print_output:
            print("Error: Invalid zip file.")
        return None

def main(zip_file, password_file, silent=False, only_pass=False, print_output=True):
    passwords = []
    if os.path.exists(password_file):
        with open(password_file, 'r') as f:
            passwords = [line.strip() for line in f]

    if passwords:
        found_password = find_password(zip_file, passwords, silent, only_pass, print_output)
        if found_password:
            return found_password
        else:
            return None
    else:
        if not silent and not only_pass and print_output:
            print("Error: Password file is empty or does not exist.")
        return None
                
