import json
import datetime as dt

def json_dumps_nan(content):
    s = json.dumps(content, indent = 4, separators=(',', ': '), default=datetime_string)
    s = s.replace("NaN", "null")
    return s


def datetime_string(v):
    if type(v) in (dt.datetime, dt.date):
        return v.__str__()