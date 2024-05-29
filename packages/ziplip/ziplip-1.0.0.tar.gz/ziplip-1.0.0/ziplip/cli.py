import argparse
import sys
from ziplip import main

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="ziplip",
        description="Find password for a zip file.",
        epilog="Author: Fidal. All rights reserved."
    )
    parser.add_argument("--file", required=True, help="Path to the zip file")
    parser.add_argument("--password", required=True, help="Path to the password file")
    parser.add_argument("-s", "--silent", action="store_true", help="Silent mode, only show the correct password")
    parser.add_argument("--only-pass", action="store_true", help="Only print the passwords tried")
    parser.add_argument("-v", "--version", action="version", version="ziplip 1.0", help="Show ziplip version")

    return parser.parse_args()

def cli():
    args = parse_arguments()
    password = main(args.file, args.password, args.silent, args.only_pass)
    if password:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    cli()
