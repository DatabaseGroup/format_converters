"""
The MIT License (MIT)
Copyright (c) 2017 Mateusz Pawlik.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import argparse
import tree_formats.bracket.dot.converter as BDConverter
import tree_formats.newick.bracket.converter as NBConverter
import tree_formats.xml.bracket.converter as XBConverter

def main(argv):
    _BD = 'bracket-dot'
    _NB = 'newick-bracket'
    _XB = 'xml-bracket'
    _XD = 'xml-dot'
    parser = argparse.ArgumentParser(
        description='Format converter of the Database Research Group. \
                     Description can be found in README.md.')
    parser.add_argument(
        'source',
        type=str,
        help='Source string to convert.'
    )
    parser.add_argument(
        'conversion_type',
        type=str,
        choices=[_BD, _NB, _XB, _XD],
        help='Conversion type.'
    )
    args = parser.parse_args()

    if args.conversion_type == _BD:
        BDConverter.convert(args.source)

    if args.conversion_type == _NB:
        NBConverter.convert(args.source)

    if args.conversion_type == _XB:
        XBConverter.convert_to_print(args.source)

    if args.conversion_type == _XD:
        BDConverter.convert(XBConverter.convert_to_string(args.source))

if __name__ == '__main__':
  main(sys.argv)
