# -*- coding: utf-8 -*-
# python3.4

import sys
import getopt
import os

# vars
file1 = None
file2 = None
results = []


def main(argv):
    helptext = ('Uses python 3.4\n\n'
                'Usage: python compare.py <file1> <file2>\n\n'
                'Necessary modules: sys, getopt, os')

    # prints the help text when -h or --help is used
    try:
        opts, args = getopt.getopt(argv, 'h', ['help'])
    except getopt.GetoptError:
        print(helptext)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(helptext)
            sys.exit()

    global file1
    global file2

    if len(sys.argv) > 0:
        file1 = sys.argv[1]
    if len(sys.argv) > 1:
        file2 = sys.argv[2]

    if file1 is None:
        file1 = input('File 1: ')
    if file2 is None:
        file2 = input('File 1: ')

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    main(sys.argv[1:])

    read_file1 = open(file1, 'r')
    read_file2 = open(file2, 'r')

    file1_lines = read_file1.readlines()
    file2_lines = read_file2.readlines()

    for line in file1_lines:
        file1_code = line.split()[0]
        filename = line.split()[1]
        filename = filename.split('/')[-1]

        matching = [s for s in file2_lines if filename in s]

        for matching_lines in matching:
            file2_code = matching_lines.split()[0]

            if file1_code == file2_code:
                break
            else:
                results.append(line.split()[1])
                break

    if len(results) >= 1:
        print("Hash codes don't match for file(s):")
        for line in results:
            print(line)
    else:
        print('All files are OK')
