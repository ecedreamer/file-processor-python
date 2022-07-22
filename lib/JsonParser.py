import json


def json_object_gen(parser):
    json_string = ""
    start = False
    for c in parser.buffer:
        if c == "{":
            start = True
        if c == "\n":
            continue
        if start:
            json_string += c
        if c == "}":
            start = False
            try:
                yield json.loads(json_string)
            except Exception as e:
                print(f"EXCEPTION at Parser: {e}")
                yield json_string
            json_string = ""

    parser.buffer = json_string




class JsonParser:
    def __init__(self, _from=None) -> None:
        self.buffer = ""
        self.gen = iter("")
        # to tell the batch processor and not breaking existing thing
        self.json_parser = True
        self._from = _from
        
    def write(self, data):
        self.buffer += data
        self.gen = json_object_gen(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._from != "file_processor":
            self.buffer = ""
        return next(self.gen)
    