import magic


# data size default to 1 KB = 1024 Bytes
def file_reader(file_obj, data_size=1024 * 15):
    while True:
        if data := file_obj.read(data_size):
            yield data
        else:
            break


def unpack_plaintext_file(file_path):
    with open(file_path, encoding = "ISO-8859-1") as file_obj:

        file_obj.seek(0)
        yield from file_reader(file_obj)


def unpack_json_file(file_path):
    with open(file_path, encoding = "ISO-8859-1") as file_obj:
        file_obj.seek(0)
        yield from file_reader(file_obj)

SUPPORTED_MIME_TYPES = {
    "application/json": unpack_json_file,
    "text/plain": unpack_plaintext_file,
    "text/csv": unpack_plaintext_file,
}

def unpack_file(file_path="files/sample_file2.txt"):
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(file_path)
    print("MIME TYPE   :::  ", mime_type)
    yield from SUPPORTED_MIME_TYPES[mime_type](file_path)