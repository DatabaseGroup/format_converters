# This python file can be used to convert the Newick notation to the bracket
# notation.

"""
The MIT License (MIT)
Copyright (c) 2017 Manuel Kocher.

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
from ..grammar.NewickLexer import NewickLexer
from ..grammar.NewickParser import NewickParser
from ..grammar.NewickListener import NewickListener

class NewickBracketListerner(NewickListener):


    # Creates a string self.n
    def __init__(self):
        self.n = ''


    # Called when Node is entered
    def enterNode(self, ctx):

        self.n += '{'

        if ctx.label() != None:

            # If cases to detect what parts of a label are present

            if ctx.label().key() != None:
                if ctx.label().key().INT() != None:
                    self.n += str(ctx.label().key().INT())
                elif ctx.label().key().FLOAT() != None:
                    self.n += str(ctx.label().key().FLOAT())
                elif ctx.label().key().STR() != None:
                    self.n += str(ctx.label().key().STR())
                else:
                    self.n += ''

            if ctx.label().value() != None:

                if ctx.label().value().INT() != None:
                    self.n += ':' + str(ctx.label().value().INT())

                elif ctx.label().value().FLOAT() != None:
                    self.n += ':' + str(ctx.label().value().FLOAT())

                else:
                    self.n += ''
        pass

    # The following methods can be used for debugging

    # Called when Node is exited
    def exitNode(self, ctx):
        #print "Exit Leaf"
        self.n += '}'

        pass

    # Called when Key is entered
    def enterKey(self, ctx):
        #print "Enter Key"
        pass

    # Called when Key is exited
    def exitKey(self, ctx):
        #print "Exit Key"
        pass


    # Called when Value is entered
    def enterValue(self, ctx):
        #print "Enter Value"
        pass

    # Called when Value is exited
    def exitValue(self, ctx):
        #print "Enter Value"
        pass

    # Returns a string with the Bracket Notation
    def get_bracket_notation(self):
        return self.n


def convert(source):

    lexer = NewickLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = NewickParser(stream)
    tree = parser.tree()

  # Define our BracketNotationXMLParserListener
    listener = NewickBracketListerner()

  # Open a tree walker and associate our listener to be used while traversing
  # the XML tree
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

  # Print the string our BracketNotationXMLParserListener generate while walking
  # the XML tree to stdout
    print(listener.get_bracket_notation())
