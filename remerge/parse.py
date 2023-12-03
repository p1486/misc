from argparse import ArgumentParser
from enum import Enum
from actions import install, remove, search, upgrade


class Actions(Enum):
    Install = "install"
    Remove = "remove"
    Search = "search"
    Upgrade = "upgrade"


    def __str__(self):
        return self.value


def parse():
    parser = ArgumentParser()
    parser.add_argument("actions", type=Actions, choices=list(Actions))
    parser.add_argument("packages", nargs="*")
    parser.add_argument("-p", "--pretend", action="store_true")
    args = parser.parse_args()
    package = " ".join(args.packages)
    match args.actions:
        case Actions.Install:
            install(args.pretend, package)
        case Actions.Remove:
            remove(args.pretend, package)
        case Actions.Search:
            search(package)
        case Actions.Upgrade:
            upgrade(args.pretend)


if __name__=="__main__":
    pass
