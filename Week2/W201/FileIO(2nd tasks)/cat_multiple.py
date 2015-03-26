import sys
from pprint import pprint

def main():
    for item in range(1,len(sys.argv)):
        with open(sys.argv[item]) as f:
            read = f.read()
            new = read.split("\n")
            print("\n".join(new))
        f.close()


if __name__ == '__main__':
    main()
