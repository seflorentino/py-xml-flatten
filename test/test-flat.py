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
        print 'text', output[0].tag
        self.assertEquals(output[0].tag, 'node', 'Must match root tag')
        self.assertEquals(output[0].find('lastName').text, 'Pig', 'Must match lastName')
        self.assertEquals(output[0].find('occupation').text, 'Architect', 'Must match occupation')
        self.assertEquals(output[1].find('firstName').text, 'Mr', 'Must match firstName')
        self.assertEquals(output[1].find('lastName').text, 'Potato', 'Must match lastName')
        self.assertEquals(output[1].find('occupation').text, 'Entertainer', 'Must match occupation')
        self.assertEquals(output[2].find('firstName').text, 'Mr', 'Must match firstName')
        self.assertEquals(output[2].find('lastName').text, 'Zebra', 'Must match lastName')
        self.assertEquals(output[2].find('occupation').text, 'Postman', 'Must match occupation')

class DataCollector():
    def __init__(self):
        self.data = []

    def collect(self, _dict):
        self.data.append(_dict)

    def get_data(self):
        return self.data

if __name__ == '__main__':
    unittest.main()
