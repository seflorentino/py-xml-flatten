#!/usr/bin/env python

import unittest
import sys
sys.path.append('src')

import xmlflatten

class TestFlatFile(unittest.TestCase):

    def test_flat_xml(self):
        collector = DataCollector()
        flatter = xmlflatten.XmlFlatten('test/data/flat.xml', 'node', collector.collect)
        flatter.flatten()

        output = collector.get_data()

        _assEq = self.assertEquals

        first = output[0]
        _assEq(first.tag, 'node', 'Must match root tag')
        _assEq(first.find('lastName').text, 'Pig', 'Must match lastName')
        _assEq(first.find('occupation').text, 'Architect', 'Must match occupation')

        second = output[1]
        _assEq(second.find('firstName').text, 'Mr', 'Must match firstName')
        _assEq(second.find('lastName').text, 'Potato', 'Must match lastName')
        _assEq(second.find('occupation').text, 'Entertainer', 'Must match occupation')

        third = output[2]
        _assEq(third.find('firstName').text, 'Mr', 'Must match firstName')
        _assEq(third.find('lastName').text, 'Zebra', 'Must match lastName')
        _assEq(third.find('occupation').text, 'Postman', 'Must match occupation')

class DataCollector():
    def __init__(self):
        self.data = []

    def collect(self, _dict):
        self.data.append(_dict)

    def get_data(self):
        return self.data

if __name__ == '__main__':
    unittest.main()
