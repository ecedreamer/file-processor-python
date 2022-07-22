
def line_gen(buffer):
    yield from buffer.splitlines()


class LineParser:
    def __init__(self, _from=None) -> None:
        self.buffer = ""
        self.gen = iter("")
        # to tell the batch processor and not breaking existing thing
        self.line_parser = True
        self._from = _from
        
    def write(self, data):
        self.buffer += data
        self.gen = line_gen(self.buffer)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._from != "file_processor":
            self.buffer = ""
        return next(self.gen)
    