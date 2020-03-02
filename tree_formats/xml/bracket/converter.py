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
    def __init__(self, tokanization):
        # initialize empty string
        self.bn = ''
        self.tokanization = tokanization

    # Called whenever an element is entered, i.e., a tag is opened by
    # '<element-name>'.
    def enterElement(self, ctx):
        # Open a new tag-node with its name as its label.
        self.bn += '{' + str(ctx.Name()[0].getText())
        # Sort attributes by their names.
        attributes = sorted(ctx.attribute(), key=lambda attribute: str(attribute.Name()))
        if attributes:
            # Traverse sorted attributes.
            for attribute in attributes:
                # For each attribute-value pair, create two nodes in
                # a parent-child relationship such that:
                #   - parent's label is the attribute's name (attribute.Name()),
                #   - child's label is the attribute's value (attribute.STRING()[1:-1]).
                # NOTE: [1:-1] removes the "-prefix/-suffix from the returned string.
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
        # Extract text data.
        text = ctx.TEXT()
        # Only add text data to bracket notation representation if it is a
        # non-empty string (whitespaces only amke an empty string too).
        if text:
            if self.tokanization == 'content-long-strings':
                self.bn += '{' + str(text) + '}'
            if self.tokanization == 'content-by-whitespace':
                string_tokens = str(text).split()
                string_tokens = "".join(["{%s}" % t for t in string_tokens])
                self.bn += string_tokens

    # Called whenever character/text data is exited.
    def exitChardata(self, ctx):
        # Nothing to do.
        pass

    # Getter for the bracket notation string.
    def get_bracket_notation(self):
        return self.bn

# We implement multiple ways of obtaining a tree structure from an XML file.
# The differences lie in how we map XML elements (attributes, tags, and long
# strings text data) to nodes and labels.
#
# Labels must follow the bracket notation grammar:
#     tree_formats/bracket/grammar/Bracket.g4
#
# content-long-strings (default)
#     Each tag is a node with tag's name as label.
#     Each attribute is a direct child of its tag's node with label being
#     attribute's name and a single child with the label being attribute's
#     value.
#     Each tag-node has a child with the label being tag's contents.
#     Given a tag, its attribute-nodes and children-tag-nodes are siblings.
#     Attribute-nodes are sorted by their name and come before tag-nodes.
#     Sibling-tag-nodes are composed as present in the XML file (without
#     further ordering).
#
# content-by-whitespace
#     As tags-long-strings.
#     Additionally, multi-words tag contents are split by whitespaces into
#     multiple sibling nodes. No ordering is appied.
#     IDEA: Unify the string tokens: upper/lower case, punctuations, ets.
#     IDEA: Remove in titles.
#     IDEA: Split the urls.
#
def convert(source, tokanization='content-long-strings'):

    lexer = XMLLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    tree = parser.document()

    # Define our BracketNotationXMLParserListener
    listener = XMLBracketParserListener(tokanization)

    # Open a tree walker and associate our listener to be used while traversing
    # the XML tree
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Print the string our BracketNotationXMLParserListener generate while walking
    # the XML tree to stdout
    return listener.get_bracket_notation()
