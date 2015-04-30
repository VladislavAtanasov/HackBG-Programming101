import json
import matplotlib.pyplot as plt

class Histogram:

    def __init__(self):
        self.diction = {}

    def add(self, modul):
        if modul not in self.diction:
            self.diction[modul] = 1
        elif modul in self.diction:
            self.diction[modul] += 1

    def count(self, modul):
        if modul in self.diction:
            return self.diction[modul]
        else:
            return None

    def get_dict(self):
        return self.diction

    def read(self):
        with open("datacrawl.json", "r") as f:
            content = json.load(f)
        return content


def main():
    histogram = Histogram()
    data = histogram.read()
    content = [s.encode('utf-8') for s in data]
    for elem in content:
        histogram.add(elem)
    plt.bar(range(len(histogram.get_dict())), histogram.get_dict().values(), align='center')
    plt.xticks(range(len(histogram.get_dict())), histogram.get_dict().keys())
    plt.savefig("histogram.png")
    print(plt.show())

if __name__ == '__main__':
    main()
