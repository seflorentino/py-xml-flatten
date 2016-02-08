#!/usr/bin/env python

import unittest
import sys

sys.path.append('src')

import xmlflatten

class TestChildrenFile(unittest.TestCase):
    def test_children_xml(self):
        collector = DataCollector()
        flatter = xmlflatten.XmlFlatten('test/data/children.xml', 'node', collector.collect)
        flatter.flatten()

        _assert = self.assertEquals

        output = collector.get_data()
        first = output[0]
        _assert(first.tag, 'node', 'Must match root tag')
        _assert(first.find('name').text, 'Peppa', 'Must match child value')

        first_items = first.find('items').findall('item')
        _assert(first_items[0].text, 'boots', 'Must match child value')
        _assert(first_items[1].text, 'teddy', 'Must match child value')

        second = output[1]
        _assert(second.tag, 'node', 'Must match root tag')
        _assert(second.find('name').text, 'George', 'Must match child value')
        _assert(second.find('items').findall('item')[0].text, 'dinosaur', 'Must match child value')

class DataCollector():
    def __init__(self):
        self.data = []

    def collect(self, _dict):
        self.data.append(_dict)

    def get_data(self):
        return self.data

if __name__ == '__main__':
    unittest.main()
