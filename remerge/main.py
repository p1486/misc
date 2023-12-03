#!/usr/bin/env python3


from logging import basicConfig, getLogger, WARNING
from parse import parse


def main():
    basicConfig()
    getLogger().setLevel(level=WARNING)
    try:
        parse()
    except KeyboardInterrupt:
        getLogger("remerge").warning("KeyboardInterrupt")


if __name__=="__main__":
    main()
