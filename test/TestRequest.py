import unittest
from Fecha import Fecha
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def testInit(self):
        fecha = Fecha("26-12-2015", "%d-%m-%Y")
        self.assertEqual(fecha.date, datetime(2015, 12, 26))

    def testAddDay(self):
        fecha = Fecha("26-12-2015", "%d-%m-%Y")
        fecha.addDay(3)
        self.assertEqual(fecha.date, datetime(2015, 12, 29))

    def testSustractDay(self):
        fecha = Fecha("26-12-2015", "%d-%m-%Y")
        fecha.addDay(-3)
        self.assertEqual(fecha.date, datetime(2015, 12, 23))

    def testToString(self):
        fecha = Fecha("26-12-2015", "%d-%m-%Y")
        self.assertEqual("26-12-2015", fecha.toString())

    def testToStringWithFormat(self):
        fecha = Fecha("26-12-2015", "%d-%m-%Y")
        self.assertEqual("2015-12-26", fecha.toString("%Y-%m-%d"))

    def testWihtTime(self):
        fecha = Fecha("2016-01-14 11:27:53")
        self.assertEqual("2016-01-14 11:27:53", fecha.toString("%Y-%m-%d %H:%M:%S"))