#!/usr/bin/python3

"""
The MIT License (MIT)
Copyright (c) 2017 Daniel Kocher.

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

from antlr4 import *
from ..grammar.XMLLexer import XMLLexer
from ..grammar.XMLParser import XMLParser
from ..grammar.XMLParserListener import XMLParserListener

# This is our listener that is called while the XMLParser traverses the XML tree
# It has one member 'bn' that
#   - is built node-by-node during the parsing process, and
#   - represents the bracket notation of the XML tree once the parsing succeeds.
# One can receive the bracket notation as string using the
# 'get_bracket_notation' function.
class XMLBracketParserListener(XMLParserListener):
    # Constructor
    def __init__(self):
        # initialize empty string
        self.bn = ''

    # Called whenever an element is entered, i.e., a tag is opened by
    # '<element-name>'.
    def enterElement(self, ctx):
        # open a new node and its label
        self.bn += '{' + str(ctx.Name()[0].getText())

        # sort attributes by attribute names, always
        attributes = sorted(ctx.attribute(), key=lambda attribute: str(attribute.Name()))

        if attributes:
            # traverse sorted attributes
            for attribute in attributes:
                # for each attribute pair, open a new node having the attribute name as
                # label (attribute.Name()), and open another new node having the
                # attribute value as label (attribute.STRING()[1:-1]).
                # [1:-1] removes the "-prefix/-suffix from the returned string
                self.bn += '{' + str(attribute.Name()) + '{' + str(attribute.STRING())[1:-1] + '}}'

    # Called whenever an element is exited, i.e., a tag is closed by
    # '</element-name>'
    def exitElement(self, ctx):
        # simply close the node we opened in enterElement (the parser actually
        # traverses the node in the correct order)
        self.bn += '}'

    # Called whenever an element is entered, i.e., a pair 'key="value"' is occurs
    # within an element, i.e., '<element-name key1="value1" key2="value2">'.
    def enterAttribute(self, ctx):
        # to be able to order the attributes by their name, we process them in
        # enterElement and not here
        pass

    # Called whenever an element is exited.
    def exitAttribute(self, ctx):
        # to be able to order the attributes by their name, we process them in
        # enterElement and not here
        pass

    # Called whenever character/text data is entered, i.e., in between a closing
    # and an opening tag, i.e., '<element-name>text-data</element-name>'
    def enterChardata(self, ctx):
        # extract text data
        text = ctx.TEXT()

        # only add text data to bracket notation representation if it is not empty,
        # i.e., whitespaces only
        # NOTE: Spaces are removed due to the current bracket notation grammar
        #       and converter.
        #       Later this can have another approach: Split long strings into
        #       sibling nodes by spaces.
        if text:
            self.bn += '{' + str(text).replace(" ", "") + '}'

    # Called whenever character/text data is exited.
    def exitChardata(self, ctx):
        # Nothing to do.
        pass

    # Getter for the bracket notation string.
    def get_bracket_notation(self):
        return self.bn

def convert(source):

      lexer = XMLLexer(InputStream(source))
      stream = CommonTokenStream(lexer)
      parser = XMLParser(stream)
      tree = parser.document()

      # Define our BracketNotationXMLParserListener
      listener = XMLBracketParserListener()

      # Open a tree walker and associate our listener to be used while traversing
      # the XML tree
      walker = ParseTreeWalker()
      walker.walk(listener, tree)

      # Print the string our BracketNotationXMLParserListener generate while walking
      # the XML tree to stdout
      print(listener.get_bracket_notation())
