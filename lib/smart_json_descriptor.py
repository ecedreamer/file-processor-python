import json
import os.path
import sys

import magic

FILE_PATHS = [
    "files/citylots.jsonl",
]


def verify_json_file(file_path):
    if os.path.exists(file_path):
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(file_path)
        print(mime_type)
        if mime_type == "application/json":
            return True
        else:
            print("Not a valid json file")
    else:
        print("File does not exist.")
    return False


def describe_json_file(file_path) -> dict:
    description = {}
    with open(file_path) as json_file:
        try:
            file_content = json.load(json_file)
            print(type(file_content))
        except Exception as e:
            print(e)

    return description


def main():
    file_path = FILE_PATHS[0]
    # verify json file
    file_is_valid = verify_json_file(file_path)
    if not file_is_valid:
        return
    # describe file
    result = describe_json_file(file_path)
    print(result)


if __name__ == "__main__":
    main()
