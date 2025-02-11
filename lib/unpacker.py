import json

import magic


# data size default to 1 KB = 1024 Bytes
def file_reader(file_obj, data_size=1024 * 15):
    while True:
        if data := file_obj.read(data_size):
            yield data
        else:
            yield "\n"
            break


def describe_json(file_path):
    with open(file_path) as file_obj:
        try:
            json_data = json.load(file_obj)
            if isinstance(json_data, dict):
                list_list = []
                for key in json_data.keys():
                    if isinstance(json_data[key], list):
                        list_list.append({"key": key, "count": len(json_data[key])})
                print(list_list)
        except Exception as e:
            print(e)
            return None


def unpack_plaintext_file(file_path):
    with open(file_path, encoding="ISO-8859-1") as file_obj:
        file_obj.seek(0)
        yield from file_reader(file_obj)


def unpack_json_file(file_path):
    result = describe_json(file_path)
    # make it possible to select either it is json line or json object. if its a json object, we should ask for the
    # keys hwere logs are located.
    with open(file_path, encoding="ISO-8859-1") as file_obj:
        file_obj.seek(0)
        yield from file_reader(file_obj)


SUPPORTED_MIME_TYPES = {
    "application/json": unpack_json_file,
    "text/plain": unpack_plaintext_file,
    "text/csv": unpack_plaintext_file,
}


def unpack_file(file_path):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(file_path)
    print("MIME TYPE   :::  ", mime_type)
    yield from SUPPORTED_MIME_TYPES[mime_type](file_path)
