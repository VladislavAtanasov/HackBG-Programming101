import sys
from random import randint

def main():
    file1 = open("number1.txt", "w")
    for x in range(int(sys.argv[2])):
        file1.write(str(randint(0,1000)) + " ")
    file1.close()

if __name__ == '__main__':
    main()
