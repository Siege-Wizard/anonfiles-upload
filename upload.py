#!/usr/bin/env python3

import argparse
import json
import os
import sys

import requests


URL = 'https://api.anonfiles.com/upload'
TOKEN_SUFFIX = "?token="
TOKEN_ENV = "ANONFILES_TOKEN"


if __name__ == '__main__':
    # Parse the argument
    parser = argparse.ArgumentParser(description="Upload to AnonFiles.com")
    parser.add_argument('file')
    filename = parser.parse_args().file
    token = os.getenv(TOKEN_ENV)

    # Computing the final URL
    if token is None:
        url = URL
    else:
        url = f'{URL}{TOKEN_SUFFIX}{token}'

    # Validating filename
    if not os.path.exists(filename):
        print(f"ERROR: file {filename} couldn't be found")
        sys.exit(1)
    if os.path.isdir(filename):
        print(f"ERROR: a directory can't be uploaded")
        sys.exit(1)

    # Uploading the file
    with open(filename, 'rb') as file:
        print(f"Uploading {filename} ...")
        response = json.loads(requests.post(url, files={'file': file}).text)

        if response['status']:
            urls = response['data']['file']['url']
            print(f"Filed uploaded successfully to {urls['full']}")
            print(f"::set-output name=url::{urls['full']}")
            print(f"::set-output name=short::{urls['short']}")
        else:
            print(f"ERROR: {response['error']['message']}")
            sys.exit(1)
