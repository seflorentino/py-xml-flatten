py-xml-flatten
===============

## Overview

Simple Python script for transforming big XML files to flat CSV format.

# Usage

```
xmlflatten.py -i <src .xml> -e 'root_sub_element' -c 'xpath_columns'
```

Parameters:
* -i - input XML file. Must be a file composed of well-formed elements, i.e. can be parsed by ElementTree.
* -e - root sub element tag. The tag to search for and process as an individual document.
* -c - The columns to print as comma-separated xpath values.

Examples:
```
xmlflatten.py -i employees.xml -e 'employee' -c './firstName,./lastName'

xmlflatten.py -i students.xml -e 'student' -c './name,./subject[1]/teacher,./subject[2]/teacher'
```

## License

(The MIT License)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
