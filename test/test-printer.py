#!/usr/bin/env python

import unittest
import sys

import xml.etree.ElementTree as ET

sys.path.append('src')

import xmlflatten

class TestPrinter(unittest.TestCase):
    def test_simple(self):
        cols = './name,./value'

        factory = xmlflatten.ElementPrinterFactory(cols)
        printer = factory.get_printer()

        data = ET.fromstring('<node><name>Test</name><value>100</value></node>')
        output = printer(data)

        self.assertEquals('Test,100', output)

    def test_nested(self):
        cols = './branch/name,./branch/value'

        factory = xmlflatten.ElementPrinterFactory(cols)
        printer = factory.get_printer()

        data = ET.fromstring('<node><branch><name>Test</name><value>100</value></branch></node>')
        output = printer(data)

        self.assertEquals('Test,100', output)

    def test_multiple(self):
        cols = './type,./items/item[1],./items/item[2]'

        factory = xmlflatten.ElementPrinterFactory(cols)
        printer = factory.get_printer()

        data = ET.fromstring('<node><type>A</type><items><item>item1</item><item>item2</item></items></node>')
        output = printer(data)

        self.assertEquals('A,item1,item2', output)

if __name__ == '__main__':
    unittest.main()
