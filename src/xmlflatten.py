#!/usr/bin/env python

import argparse
import sys
import string
import mmap
import re

import xml.etree.ElementTree as ET

def main():
    args = getArgs()
    printer_factory = ElementPrinterFactory(args.columns)
    flatten = XmlFlatten(args.input, args.element,
                         printer_factory.get_printer())
    flatten.flatten()


class XmlFlatten:
    """Flattens XML elements"""
    def __init__(self, file, element, callback):
        self.file = open(file, 'r')
        self.fname = file
        self.element = element
        self.start_re = re.compile(r'\<' + self.element + '.*\>')
        self.end_re = re.compile(r'\<\/' + self.element + '.*\>')
        self.callback = callback

    def flatten(self):
        """Read element, flatten and print; repeat"""
        with open(self.fname, 'r+b') as f:
            mp = mmap.mmap(f.fileno(), 0)
            start_pos = 0
            end_pos = 0
            chars = 0
            start_match = self.start_re.search(mp)
            while start_match:
                start_pos = end_pos + start_match.start()
                end_match = self.end_re.search(mp[start_pos:])
                if end_match:
                    end_pos = start_pos + end_match.end()
                    self.process(mp[start_pos: end_pos], self.callback)
                else:
                    break
                start_match = self.start_re.search(mp[end_pos:])

    def process(self, data, callback):
        root = ET.fromstring(data)
        callback(root)

class ElementPrinterFactory:
    """Printer factory"""
    def __init__(self, columns):
        self.columns = map(string.strip, string.split(columns, ','))

    def print_elem(self, data):
        """Print data matching columns input"""
        adict = {}
        self.__add_to_dict__(adict, data.tag, data)

        out_cols = []
        for col in self.columns:
            if col in adict.keys():
                out_cols.append(adict[col])
            else:
                out_cols.append('')
        print ",".join(out_cols)

    def __add_to_dict__(self, adict, prefix, data):
        """Add element data to dictionary"""
        if len(list(data)) > 0:
            for index, child in enumerate(data):
                connector = '' if prefix == data.tag else '[' + str(index) + ']'
                self.__add_to_dict__(adict, prefix + connector + '.' + child.tag, child)
        else:
            adict[prefix] = data.text

    def get_printer(self):
        return self.print_elem


def getArgs():
    parser = argparse.ArgumentParser(description='Flatten XML file')
    parser.add_argument('-i', '--input', help='Input XML file', required=True)
    parser.add_argument('-e', '--element',
                        help='Element to flatten', required=True)
    parser.add_argument('-c', '--columns',
                        help='Columns to print', required=True)
    return parser.parse_args()

if __name__ == '__main__':
    main()
