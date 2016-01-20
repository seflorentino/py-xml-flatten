#!/usr/bin/python

import argparse
import sys
import xml.sax

def main():
    args = getArgs()

    printer_factory = ElementPrinterFactory(args.columns)

    flatten = XmlFlatten(args.input, args.element, printer_factory.get_printer())

    flatten.flatten()

class XmlFlatten:
    def __init__(self, file, element, callback):
        self.file = open(file, 'r')
        self.element = element
        self.handler = ElementContentHandler(element, callback)

    def flatten(self):
        xml.sax.parse(self.file, self.handler)

class ElementContentHandler(xml.sax.ContentHandler):
    def __init__(self, rootElement, callback):
        xml.sax.ContentHandler.__init__(self)
        self.rootElement = rootElement
        self.callback = callback or print_me
        self.dict = {}
        self.content = ''
        self.prefix = []
        self.isReadingElement = False

    def startElement(self, name, attrs):
        if name == self.rootElement:
            self.isReadingElement = True
            self.content = ''
            self.prefix = [name]
        elif self.isReadingElement:
            self.prefix.append(name)

    def endElement(self, name):
        if name == self.rootElement:
            self.isReadingElement = False
            self.callback(self.dict.copy())
        elif self.isReadingElement:
            self.dict['.'.join(self.prefix)] = self.content
            self.prefix.pop()

    def characters(self, content):
        if self.isReadingElement:
            self.content = content

class ElementPrinterFactory:
    def __init__(self, columns):
        self.columns = columns or ''

    def print_dict(self, _dict):
        cols = self.columns.split(',')
        output = []
        for col in cols:
            output.append(_dict[col])
        print ','.join(output)

    def get_printer(self):
        return self.print_dict

def print_me(the_dict):
    print(the_dict)

def getArgs():
    parser = argparse.ArgumentParser(description='Flatten XML file')
    parser.add_argument('-i', '--input', help='Input XML file', required=True)
    parser.add_argument('-e', '--element', help='Element to flatten', required=True)
    parser.add_argument('-c', '--columns', help='Columns to print', required=False)
    return parser.parse_args();

if __name__ == '__main__':
    main()
