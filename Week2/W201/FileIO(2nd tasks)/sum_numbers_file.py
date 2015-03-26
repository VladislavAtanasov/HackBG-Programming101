import sys

def main():
    suma = 0
    with open(sys.argv[1]) as f:
        content = f.read().split(" ")
        for x in range(len(content) - 1):
            suma += int(content[x])
    f.close()
    print(suma)



if __name__ == '__main__':
    main()
