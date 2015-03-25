import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        text = text_file.read()
        text_file.close()
        print(text)
    else:
        print("Give me a file to read!!!Version1")

if __name__ == '__main__':
    main()
