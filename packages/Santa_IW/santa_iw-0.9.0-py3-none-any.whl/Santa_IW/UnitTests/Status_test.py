# Santa Is Watching aka Santa_IW (Code and Documentation) is published under an MIT License
# Copyright (c) 2024 Steven Goncalo
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import unittest
from enum import Enum

from Santa_IW.Status import StatusSummation, Status


class S(Enum):
    A = 1
    B = 2
    C = 3


class MyTestCase(unittest.TestCase):
    def test_best_worst(self):
        lst = [Status.OK, Status.WARNING, Status.NODATA]
        ss = StatusSummation(lst)
        worst = ss.worst()
        self.assertEqual(Status.WARNING, worst)

    def test_worst(self):
        lst = [x for x in Status]
        self.assertEqual(6, len(lst))
        self.assertEqual(Status.NODATA, min(lst))
        self.assertEqual(Status.CRITICAL, max(lst))


if __name__ == '__main__':
    unittest.main()
