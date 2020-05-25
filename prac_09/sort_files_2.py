"""
Author: Han Su
Date: 25/05/2020
https://github.com/HanSu52/cp1404practicals
"""
import os
import shutil


def main():
    """Sort all the files base on their file types."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        directory_name = input("What category would you like to sort {} files into?".format(extension))

        try:
            os.mkdir(directory_name)
        except FileExistsError:
            pass

        shutil.move(os.path.abspath(filename), os.path.abspath(directory_name))


if __name__ == '__main__':
    main()
