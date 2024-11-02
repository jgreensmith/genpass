"""  Script: generate_password.py
     Desc: generates random password using secrets module
     Author: James Greensmith
"""
import secrets
import string
from argparse import ArgumentParser
from pyperclip import copy

# Define default arguments
DEFAULT_CHARACTERS = string.ascii_letters + string.digits
DEFAULT_LENGTH = 12


class Arguments:
    """Class to be returned from handle_args"""

    def __init__(self, length: int, chars: str):
        self.length = length
        self.chars = chars


def handle_args() -> Arguments:
    """ Optional Arguments to specify length of password, and special characters
        default is 12, with special characters
    """
    # define arguments
    parser = ArgumentParser(
        description="A script to generate random passwords")
    parser.add_argument("-l", "--length", type=int,
                        help="Specify the length of the password, default is 12.")
    parser.add_argument("-ns", "--nospecial", action="store_true",
                        help="disable use of special characters")

    chars = DEFAULT_CHARACTERS
    args = parser.parse_args()

    # Check for arguments
    if args.length:
        length = args.length
    else:
        length = DEFAULT_LENGTH
    if not args.nospecial:
        chars = chars + "!@#$%^&*()-_=+[]|;:,.<>?/"

    return Arguments(length, chars)


def generate_password(args: Arguments) -> str:
    """choose a random character and combine list into string, acording to arguments"""

    password = []
    for _ in range(args.length):
        password.append(secrets.choice(args.chars))
    return "".join(password)


def main() -> None:
    """Test cases"""
    args = handle_args()
    copy(generate_password(args))
    print("Password copied to clip board")


# boilerplate that calls main() if run as script
if __name__ == "__main__":
    main()
