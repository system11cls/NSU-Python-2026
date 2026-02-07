from sys import argv, stderr
from os import listdir, stat
from os.path import isfile, join, isdir


if len(argv)  < 2:
    print("No path to scan", file=stderr)
    exit(1)

cor_path = argv[1]
if not(isdir(cor_path)):
    print("arg is not a path to a directory", file=stderr)
    exit(1)

files = {}

def set_files_in_dir(dir):
    files_in_dir = listdir(dir)
    for file in files_in_dir:
        file_path = join(dir, file)
        if isfile(file_path):
            info = stat(file_path)
            files[file_path] = info.st_size
        elif isdir(file_path):
            set_files_in_dir(file_path)

set_files_in_dir(cor_path)

res_dict = dict(sorted(files.items(), key=lambda item: (-1) * item[1]))
for (file, size) in res_dict.items():
    print(f'{file} -> {size/1024} KB')