import unittest
import tdd2
import datetime


class TestTdd(unittest.TestCase):
    def test_add_five(self):
        self.assertEqual(8, tdd2.add_five(3))

    def test_find_max(self):
        self.assertEqual(5, tdd2.my_max([1, 2, 3, 4, 5]))

    def test_find_min(self):
        self.assertEqual(1, tdd2.my_min([1, 2, 3, 4, 5]))

    def test_has_string(self):
        self.assertEqual(["Mary had"],
                         tdd2.has_string(
                             ["Mary had",
                              "a little lamb",
                              "little lamb",
                              "Whose fleece",
                              ], "Mary"))

    def test_to_date(self):
        dt = tdd2.to_date("2010-08-02")
        self.assertIsInstance(dt, datetime.date)
        self.assertEqual(2010, dt.year)
        self.assertEqual(8, dt.month)
        self.assertEqual(2, dt.day)

    def test_date_diff(self):
        self.assertEqual(1, tdd2.date_diff("2018-09-02", "2018-09-01"))

    def test_days_from_end(self):
        days_from_epoch = datetime.date(2012, 12, 21)-datetime.date(2018, 9, 1)
        self.assertEqual(days_from_epoch.days, tdd2.days_from_end("2018-09-01"))
