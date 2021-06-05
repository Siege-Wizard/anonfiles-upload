#!/usr/bin/env python3

import argparse
import os
import sys

from anonfile import AnonFile


if __name__ == '__main__':
    # Parse the argument
    parser = argparse.ArgumentParser(description="Upload to AnonFiles.com")
    parser.add_argument('file')
    filename = parser.parse_args().file

    # Validating filename
    if not os.path.exists(filename):
        print(f"ERROR: file {filename} couldn't be found")
        sys.exit(1)
    if os.path.isdir(filename):
        print(f"ERROR: a directory can't be uploaded")
        sys.exit(1)

    # Uploading the file
    upload = AnonFile(os.getenv("ANONFILES_TOKEN", "")).upload(filename, True)
    print(upload, type(upload))
    if upload.status:
        print(f"Filed uploaded successfully to {upload.url}")
        print(f"::set-output name=url::{upload.url}")
    else:
        sys.exit(1)
