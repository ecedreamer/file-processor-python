from . import LineParser, JsonParser


PARSERS = {
    "LineParser": LineParser.LineParser,
    "JsonParser": JsonParser.JsonParser
}


def get_parser(name="LineParser"):
    return PARSERS[name]