#!/usr/bin/python3

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
from antlr4 import *
from bracket.grammar.BracketLexer import BracketLexer
from bracket.grammar.BracketParser import BracketParser
from bracket.grammar.BracketListener import BracketListener

class BracketNotationListener(BracketListener):
    node_id = 0             # used to store incremented preorder id of a node
    nodes_stack = []        # stores parent ids to be available at exit
    current_node_stack = [] # stores node ids to be available at exit

    def enterNode(self, ctx):
        current_node = self.node_id
        print(str(current_node) + " [label=\"" + str(ctx.LABEL()) + "\"];")
        # push id of current node to be available at exit
        self.current_node_stack.append(current_node)
        # for each child push id of current node as their parent
        children = ctx.node()
        for c in children:
            self.nodes_stack.append(current_node)
        self.node_id += 1

    def exitNode(self, ctx):
        if len(self.nodes_stack) > 0: # root node has no parent
            parent = self.nodes_stack.pop()
            current_node = self.current_node_stack.pop()
            print(str(parent) + "->" + str(current_node))

def main(argv):
    print("digraph G {\nnode [shape=none];\nedge [dir=none];") # dot preamble

    lexer = BracketNotationLexer(InputStream(argv[1]))
    stream = CommonTokenStream(lexer)
    parser = BracketNotationParser(stream)
    tree = parser.node()
    listener = BracketNotationListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("}") # dot final closing bracket

if __name__ == '__main__':
    main(sys.argv)
