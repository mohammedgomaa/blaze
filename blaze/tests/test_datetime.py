from __future__ import absolute_import, division, print_function

import unittest
from datetime import date, datetime

import blaze
from datashape import dshape
from blaze.datadescriptor import dd_as_py


class TestDate(unittest.TestCase):
    def test_create(self):
        a = blaze.array(date(2000, 1, 1))
        self.assertEqual(a.dshape, dshape('date'))
        self.assertEqual(dd_as_py(a._data), date(2000, 1, 1))
        a = blaze.array([date(1490, 3, 12), date(2020, 7, 15)])
        self.assertEqual(a.dshape, dshape('2 * date'))
        self.assertEqual(dd_as_py(a._data),
                         [date(1490, 3, 12), date(2020, 7, 15)])
        a = blaze.array(['1490-03-12', '2020-07-15'], dshape='date')
        self.assertEqual(a.dshape, dshape('2 * date'))
        self.assertEqual(dd_as_py(a._data),
                         [date(1490, 3, 12), date(2020, 7, 15)])

    def test_properties(self):
        a = blaze.array(['1490-03-12', '2020-07-15'], dshape='date')
        y = a.year
        self.assertEqual(dd_as_py(blaze.eval(y)._data), [1490, 2020])
        m = a.month
        self.assertEqual(dd_as_py(blaze.eval(m)._data), [3, 7])
        d = a.day
        self.assertEqual(dd_as_py(blaze.eval(d)._data), [12, 15])
