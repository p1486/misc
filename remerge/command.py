from subprocess import run, Popen, PIPE


class Command:
    def __init__(self, cmd: str):
        self.cmd = cmd
        self.packages = ""
        self.options = ""


    def option(self, options: str):
        self.options = options
        return self

    
    def package(self, packages: str):
        self.packages = packages
        return self

    
    def exec(self):
        command = f"{self.cmd} {self.options} {self.packages}"
        run(command.split())


    def pipe_to(self, to: str):
        command = f"{self.cmd} {self.options} {self.packages}"
        pipe = Popen(command.split(), stdout=PIPE)
        run(to.split(), stdin=pipe.stdout)


if __name__=="__main__":
    pass
