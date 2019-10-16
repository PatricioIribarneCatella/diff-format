#!/usr/bin/env python3

class Diff(object):

    def __init__(self, path, ignore_files):

        with open(path) as f:
            lines = f.readlines()
        
        chunks = {}
        file_name = ""

        for line in lines:

            if line.startswith("diff"):
                file_name = line.split(" ")[2]
                chunks[file_name] = []
            else:
                chunks[file_name].append(line)

        self.data = dict(filter(lambda e: e[0] not in ignore_files, chunks.items()))

        self._proccess()

    def _extract_code(self, code):

        funcs = {}
        f_name = []

        # remove unnecessary lines
        # starting with:
        # index ....
        # --- file
        # +++ file
        # - code
        code = list(filter(lambda x: x.startswith("+ ")\
                            or x.startswith("+\t")\
                            or x.startswith("+#")\
                            or x.startswith("@"), code))

        for line in code:

            if line.startswith("@"):
                f_name = line.split(" ")[4:]
                f_name = " ".join(f_name)
                if f_name not in funcs:
                    funcs[f_name] = []
                continue
            else:
                funcs[f_name].append(line[1:])

        return funcs

    def _proccess(self):

        file_funcs = {}

        for file_name, code in self.data.items():

            funcs_code = self._extract_code(code)
            file_funcs[file_name] = funcs_code

        self.data = file_funcs

    def print_data(self):

        for file_name, funcs_code in self.data.items():
            print(file_name)
            for func, code in funcs_code.items():
                print(func)
                for line in code:
                    print(line)

    def export(self, output):

        with open(output, "w") as f:
            for file_name, funcs_code in self.data.items():
                f.write(file_name + "\n")
                for func, code in funcs_code.items():
                    f.write(func + "\n")
                    for line in code:
                        f.write(line + "\n")

def main():

    IGNORE = ["GNUmakefile", ".gitignore", "gradelib.py", "grade-lab2"]
    
    d = Diff("out.diff", IGNORE)
    d.export("out.txt")

if __name__ == "__main__":
    main()

