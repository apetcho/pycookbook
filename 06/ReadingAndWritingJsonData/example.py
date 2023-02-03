#!/usr/bin/env python3
from collections import OrderedDict
import json
from typing import Dict


def _get_data() -> str:
    return '{"name": "ACME", "shares": 50, "price": 490.1}'


def _turning_json_into_an_ordereddict():
    data = json.loads(_get_data(), object_pairs_hook=OrderedDict)
    print(data)

# -*-
class JSONObject:
    def __init__(self, dct):
        self.__dict__ = dct

def _using_json_to_populate_an_instance():
    print()
    data = json.loads(_get_data(), object_hook=JSONObject)
    print(data.name)
    print(data.shares)
    print(data.price)

# -*-
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def _serialize_instance(obj):
    dct = {"__classname__": type(obj).__name__}
    dct.update(vars(obj))
    return dct

def _encoding_instances():
    print()
    point = Point(3, 4)
    data = json.dumps(point, default=_serialize_instance)
    print(data)



# -*-
classes = {"Point": Point}

def _deserialize_object(dct:Dict):
    clsname = dct.pop("__classname__", None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in dct.items():
            setattr(obj, key, value)
        return obj
    else:
        return dct

def _decoding_instances():
    pt = Point(3, 4)
    s = json.dumps(pt, default=_serialize_instance)
    data = json.loads(s, object_hook=_deserialize_object)
    print()
    print(data)
    print(f"{data.x}, {data.y}")


def main():
    """Main entry."""
    # -*- (a) Turning JSON into and OrderedDict
    _turning_json_into_an_ordereddict()
    # -*- (b) Using JSOn to populate an instance
    _using_json_to_populate_an_instance()
    # -*- (c) Encoding instances
    _encoding_instances()
    # -*- (d) Decoding instances
    _decoding_instances()


if __name__ == "__main__":
    main()
