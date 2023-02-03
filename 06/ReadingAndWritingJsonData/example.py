#!/usr/bin/env python3
from collections import OrderedDict
import json


def _get_data() -> str:
    return '{"name": "ACME", "shares": 50, "price": 490.1}'


def _turning_json_into_an_ordereddict():
    data = json.loads(_get_data(), object_pairs_hook=OrderedDict)
    print(data)


def _using_json_to_populate_an_instance():
    pass


def _encoding_instances():
    pass


def _decoding_instances():
    pass


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
