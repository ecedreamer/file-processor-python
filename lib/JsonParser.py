# import orjson as json
import json


def json_object_gen(parser):
    json_string = ""
    start = False
    stack = []

    for c in parser.buffer:
        if c == "{":
            start = True
            stack.append("{")
        if c == "\n":
            continue
        if start:
            json_string += c
        if c == "}":
            try:
                stack.pop()
                if not stack:
                    start = False
                    yield json.loads(json_string)
                    json_string = ""
            except Exception as e:
                print(f"EXCEPTION at Parser: {e}")
                yield json_string

    parser.buffer = json_string


class JsonParser:
    def __init__(self, _from=None) -> None:
        self.buffer = ""
        self.gen = iter("")
        # to tell the batch processor and not breaking existing thing
        self.json_parser = True
        self.array_key = None
        self._from = _from

    def write(self, data):
        array_key = f'"{self.array_key}":'
        if self.array_key and array_key in data:
            data = data.split(array_key)[-1]
            print(data, "---------------")
        self.buffer += data
        self.gen = json_object_gen(self)

    def __iter__(self):
        return self

    def __next__(self):
        if self._from != "file_processor":
            self.buffer = ""
        return next(self.gen)
