from histogram import Histogram
from matplotlib import pyplot
from settings import IMAGE


class Plotter():

    @staticmethod
    def make_plot(keys, values):
        histogram = Histogram()

        for i in range(len(keys)):
            histogram.add(keys[i], values[i])

        keys = list(histogram.get_data_keys())
        values = list(histogram.get_data_values())

        X = list(range(len(keys)))

        pyplot.bar(X, values, align="center")
        pyplot.xticks(X, keys)

        pyplot.title("Crawled pages")
        pyplot.xlabel(histogram.get_data())
        pyplot.ylabel("Count")

        pyplot.savefig(IMAGE)
