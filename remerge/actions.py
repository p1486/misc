from command import Command


def install(pretend: bool, packages: str):
    install = Command("emerge").package(packages)
    if pretend:
        install.option("-pv").exec()
    else:
        install.option("-av").exec()


def remove(pretend: bool, packages: str):
    remove = Command("emerge").package(packages)
    if pretend:
        remove.option("-pcD").exec()
    else:
        remove.option("-acD").exec()
        Command("emerge").option("-acD").exec()
        Command("eclean-dist").option("-d").exec()


def search(packages: str):
    Command("emerge").option("-s").package(packages).pipe_to("less")


def upgrade(pretend: bool):
    Command("emerge-webrsync").exec()
    upgrade = Command("emerge").package("@world")
    if pretend:
        upgrade.option("-pvuDN").exec()
    else:
        upgrade.option("-avuDN").exec()
        Command("emerge").option("-acD").exec()
        Command("eclean-dist").option("-d").exec()


if __name__=="__main__":
    pass
