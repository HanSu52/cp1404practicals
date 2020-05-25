"""
Author: Han Su
Date: 25/05/2020
https://github.com/HanSu52/cp1404practicals
"""
import os
import shutil


def main():
    """Sort all the files base on their extensions."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        shutil.move(os.path.abspath(filename), os.path.abspath(extension))


if __name__ == '__main__':
    main()
