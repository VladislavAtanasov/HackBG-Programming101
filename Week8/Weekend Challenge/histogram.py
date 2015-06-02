class Histogram():

    def __init__(self):
        self.data = {}

    def add(self, element, times):
        if element in self.data:
            self.data[element] += times
        elif element not in self.data:
            self.data[element] = times

    def count(self, element):
        if element in self.data:
            return self.data[element]
        elif element not in self.data:
            return None

    def get_data(self):
        return self.data

    def get_data_keys(self):
        return self.data.keys()

    def get_data_values(self):
        return self.data.values()
