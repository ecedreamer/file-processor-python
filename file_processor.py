import sys
import time
from lib.unpacker import unpack_file
from lib.utils import get_parser


def file_processor(parser_name):
    parser = get_parser(parser_name)(_from="file_processor")
    if hasattr(parser, "line_parser") and parser.line_parser:
        for data in unpack_file():
            parser.write(data)
            parsed_lines = list(parser)
            parser.buffer = "" if parser.buffer.endswith(
                "\n") else parsed_lines.pop()
            yield from parsed_lines
        if len(parser.buffer.splitlines()) == 1:
            yield parser.buffer
    elif hasattr(parser, "json_parser") and parser.json_parser:
        for data in unpack_file():
            parser.write(data)
            yield from parser
    else:
        print("Invalid parser provided")


def write_to_file(file, data):
    file.write(f"{data}\n")


def main():
    parser_name = sys.argv[1] or "LineParser"
    count = 0
    with open("files/output.txt", "w") as file:
        for data in file_processor(parser_name):
            count += 1
            write_to_file(file, data)
    print(count)


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("Total time taken:", t2-t1, "seconds")
