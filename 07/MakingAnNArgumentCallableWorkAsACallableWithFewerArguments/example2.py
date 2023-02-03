#!/usr/bin/env python3
import logging
from multiprocessing import Pool
from functools import partial


def output_result(result, log=None):
    if log is not None:
        log.debug(f"Result: {result!r}")


def add(x, y):
    # -*- A sample function -*-
    return x + y


def main():
    """Main entry."""
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("test")

    pool = Pool()
    pool.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
