# This python file can be used to convert the Newick notation to the bracket
# notation.

import argparse

from antlr4 import *
from ..grammar.NewickLexer import NewickLexer
from ..grammar.NewickParser import NewickParser
from ..grammar.NewickListener import NewickListener

class BracketNotationNewickParserListerner(NewickListener):


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


def main():
  # Set up command-line argument parser and specify the XML file to parse as
  # required command-line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('newickfile')
    args = parser.parse_args()

  # Open given XML file and associated lexer/parser with it
    input = FileStream(args.newickfile)
    lexer = newickLexer.newickLexer(input)
    stream = CommonTokenStream(lexer)
    parser = newickParser.newickParser(stream)
    tree = parser.tree()

  # Define our BracketNotationXMLParserListener
    listener = BracketNotationNewickParserListerner()

  # Open a tree walker and associate our listener to be used while traversing
  # the XML tree
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

  # Print the string our BracketNotationXMLParserListener generate while walking
  # the XML tree to stdout
    print(listener.get_bracket_notation())

if __name__ == '__main__':
    main()
