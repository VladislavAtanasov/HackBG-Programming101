import unittest
from histogram import Histogram


class HistogramTest(unittest.TestCase):

    def setUp(self):
        self.server_histogram = Histogram()

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.server_histogram, Histogram))

    def test_valid_members(self):
        self.assertEqual(self.server_histogram.data, {})

    def test_add_element_not_in_histogram(self):
        self.server_histogram.add("Apache", 2)
        self.assertEqual(self.server_histogram.data["Apache"], 2)

    def test_add_element_whi_is_in_histogram(self):
        self.server_histogram.data = {"nginx": 1}
        self.server_histogram.add("nginx", 2)
        self.assertEqual(self.server_histogram.data["nginx"], 3)

    def test_count_for_elements_in_histogram(self):
        self.server_histogram.data = {"Microsoft-IIS": 1, "nginx": 2}
        self.assertEqual(self.server_histogram.count("nginx"), 2)

    def test_count_for_elements_not_in_histogram(self):
        self.server_histogram.data = {"Apache": 1, "Microsoft-IIS": 30}
        self.assertEqual(self.server_histogram.count("nginx"), None)

    def test_get_data(self):
        self.server_histogram.data = {"Apache": 10, "nginx": 20}
        same_date = {"Apache": 10, "nginx": 20}
        self.assertEqual(self.server_histogram.get_data(), same_date)

if __name__ == '__main__':
    unittest.main()
