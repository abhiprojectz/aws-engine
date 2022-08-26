from cryptography.fernet import Fernet
import os
import argparse
from argparse import ArgumentError
# from start_script import upload 

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\"

def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--acc",
        dest="acc",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-z",
        "--slot",
        dest="slot",
        type=str,
        required=True,
    ) 
    
    parser.add_argument(
        "-y",
        "--target_url",
        dest="target_url",
        type=str,
        required=True,
    ) 

    parser.add_argument(
        "-a",
        "--type_content",
        dest="type_content",
        type=str,
        required=True,
    ) 
    parser.add_argument(
        "-m",
        "--key",
        dest="key",
        type=str,
        required=True,
    )
    return parser


def write_key():
    key = Fernet.generate_key()
    print(dir_path)
    with open(dir_path + "key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(dir_path + "key.key", "rb").read()


def encrypt(filename, key):
    f = Fernet(key)

    with open(dir_path + filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(dir_path + filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(dir_path + filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(dir_path + filename, "wb") as file:
        file.write(decrypted_data)

# write_key()
# # load the key
file = "start_script.py"
file1 = "titles_db.py"
file2 = "titles_db_sandeep.py"
file3 = "xdotool_commands.py"
file4 = "ytdeb_content/content_db.py"
file5 = "ytdeb_content/main.py"
file6 = "aws_studio.py"


def encrypt_all():
    key = load_key()
    encrypt(file, key)
    encrypt(file1, key)
    encrypt(file2, key)
    encrypt(file3, key)
    encrypt(file4, key)
    encrypt(file5, key)
    encrypt(file6, key)

def decrypt_all():
    key = load_key()
    decrypt(file, key)
    decrypt(file1, key)
    decrypt(file2, key)
    decrypt(file3, key)
    decrypt(file4, key)
    decrypt(file5, key)
    decrypt(file6, key)


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    decrypt_all()
    # upload(args.acc, args.slot, args.type_content, args.target_url)


decrypt_all()
# key = load_key()
# decrypt(file, key)
# encrypt(file, key)

# if __name__ == "__main__":
#     main()