import sys
import time
from lib.unpacker import unpack_file
from lib.utils import get_parser


def file_processor(parser_name, file_info):
    parser = get_parser(parser_name)(_from="file_processor")
    # if hasattr(parser, "line_parser") and parser.line_parser:
    #     for data in unpack_file(file_path=file_info.get("file_name")):
    #         parser.write(data)
    #         parsed_lines = list(parser)
    #         parser.buffer = "" if parser.buffer.endswith("\n") else parsed_lines.pop()
    #         yield from parsed_lines
    #
    # elif hasattr(parser, "json_parser") and parser.json_parser:
    #     parser.array_key = file_info.get("array_key")
    #     for data in unpack_file(file_path=file_info.get("file_name")):
    #         parser.write(data)
    #         yield from parser
    # else:
    #     print("Invalid parser provided")
    if file_info.get("array_key"):
        parser.array_key = file_info.get("array_key")
    for data in unpack_file(file_path=file_info.get("file_name")):
        parser.write(data)
        yield from parser


def write_to_file(file, data):
    file.write(f"{data}\n")


def main():
    parser_name = sys.argv[1] or "LineParser"
    file_info = {
        "file_name": "files/sample_json_file.json",
        "array_key": None
    }
    count = 0
    with open("files/output.txt", "w") as file:
        for data in file_processor(parser_name, file_info=file_info):
            count += 1
            write_to_file(file, data)
    print(count)


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("Total time taken:", t2-t1, "seconds")
