import sys
import os
from os.path import join, getsize

def main():
    for root, dirs, files in os.walk(str(sys.argv[1])):
        print(sum(getsize(join(root, name)) for name in files), " bytes")


if __name__ == '__main__':
    main()
