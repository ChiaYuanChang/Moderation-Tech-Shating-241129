import os
import json


def get_credential(file_name: str):

    credentials = {}
    credential_path = os.path.dirname(__file__)

    file_path = os.path.join(credential_path, file_name)

    with open(file_path, "r") as cred:
        data = json.load(cred)
        credentials.update(data)

    return credentials


def get_credential_path(file_name: str):
    credential_path = os.path.dirname(__file__)
    file_path = os.path.join(credential_path, file_name)
    credential_file_path = os.path.abspath(file_path)

    return credential_file_path
