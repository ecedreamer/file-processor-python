import json
import os.path
import pprint

import magic

FILE_PATHS = [
    "files/citylots.jsonl",
    "files/sample_json_file.json",
    "files/sample_json_file2.json",
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


def describe_file_content(file_content):
    description = {
        "type": type(file_content).__name__
    }
    if isinstance(file_content, dict):
        description["length"] = len(file_content)
        dict_description = {}
        for key, value in file_content.items():
            dict_description[key] = describe_file_content(value)
        description["keys"] = dict_description

    elif isinstance(file_content, list):
        description["length"] = len(file_content)
        for data in file_content:
            description["items"] = describe_file_content(data)
    elif isinstance(file_content, str):
        description["length"] = len(file_content)
    else:
        description["type"] = type(file_content).__name__
    return description


def describe_json_file(file_path) -> dict:
    description = None
    with open(file_path) as json_file:
        try:
            file_content = json.load(json_file)
            description = describe_file_content(file_content)
        except json.decoder.JSONDecodeError as e:
            print(e)

    return description


def main():
    file_path = FILE_PATHS[1]
    # verify json file
    file_is_valid = verify_json_file(file_path)
    if not file_is_valid:
        return
    # describe file
    result = describe_json_file(file_path)
    print(result)


if __name__ == "__main__":
    main()
