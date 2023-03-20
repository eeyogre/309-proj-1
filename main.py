"""
    This module is just designed to confirm that you have a working python installation, that you can install
    modules and that the installation is able to read and write files.
"""
import os
import sys
import uu
import numpy
import difflib


def diff_files(file1, file2):
    """
    Simple function to compare two text files.
    
    :param file1: the first file to compare 
    :param file2: the second file to compare
    :return: the differences between the files as a diff result
    """
    with open(file1) as f1:
        with open(file2) as f2:
            text1 = f1.readlines()
            text2 = f2.readlines()
            return ''.join(difflib.ndiff(text1, text2))


def main():
    """
    Writes some information about the python and numpy versions, decodes a text file, writes out a diff result,
    and deletes a temporary file
    """

    output_file = 'output.txt'
    cipher_file = 'cipher.txt'
    temp_file = 'temp.txt'
    plain_file = 'plain.txt'

    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, 'w') as f:
        f.write(f'Python version: {sys.version_info.major}.{sys.version_info.minor}\n')
        f.write(f'Numpy version: {numpy.__version__}\n')
        f.write(f'Working directory: {os.getcwd()}\n')
        f.write('\n')
        uu.decode(cipher_file, temp_file)
        f.write(diff_files(temp_file, plain_file))
        os.remove(temp_file)


if __name__ == '__main__':
    main()
