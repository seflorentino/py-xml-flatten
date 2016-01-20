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

        self.assertEquals(output[0]['node.firstName'], 'Daddy', 'Must match firstName')
        self.assertEquals(output[0]['node.lastName'], 'Pig', 'Must match lastName')
        self.assertEquals(output[0]['node.occupation'], 'Architect', 'Must match occupation')
        self.assertEquals(output[1]['node.firstName'], 'Mr', 'Must match firstName')
        self.assertEquals(output[1]['node.lastName'], 'Potato', 'Must match lastName')
        self.assertEquals(output[1]['node.occupation'], 'Entertainer', 'Must match occupation')
        self.assertEquals(output[2]['node.firstName'], 'Mr', 'Must match firstName')
        self.assertEquals(output[2]['node.lastName'], 'Zebra', 'Must match lastName')
        self.assertEquals(output[2]['node.occupation'], 'Postman', 'Must match occupation')

class DataCollector():
    def __init__(self):
        self.data = []

    def collect(self, _dict):
        self.data.append(_dict)

    def get_data(self):
        return self.data

if __name__ == '__main__':
    unittest.main()
