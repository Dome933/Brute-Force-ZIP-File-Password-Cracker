import zipfile
import itertools
import string

zip_file_path = "secret.zip"

try:
    with zipfile.ZipFile(zip_file_path) as zip_file:
        for password_length in range(1, 4):
            for password in itertools.product(string.ascii_letters + string.digits, repeat=password_length):
                password = "".join(password)
                try:
                    zip_file.extractall(pwd=password.encode())
                except Exception as e:
                    continue
                else:
                    print("[+] Password found:", password)
                    break
except Exception as e:
    print(f"An error occurred: {e}")
