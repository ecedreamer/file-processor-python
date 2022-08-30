import json
from profiler import time_profile


def json_object_gen(parser):

    for c in parser.buffer:


class JsonParser:
    def __init__(self) -> None:
        self.buffer = ""
        self.gen = iter('')

    def write(self, data):
        self.buffer += data
        self.gen = json_object_gen(self)

    @time_profile
    @staticmethod
    def is_valid(file_path):
        try:
            with open(file_path, 'r') as file:
                json_file = json.load(file)
                return True
        except Exception as e:
            print(e)
            return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._from != "file_processor":
            self.buffer = ""
        return next(self.gen)


if __name__ == "__main__":
    file_path = "files/sample_file2"
    is_valid_json = JsonParser.is_valid(file_path)
    print("File is valid JSON ==> ", is_valid_json)
