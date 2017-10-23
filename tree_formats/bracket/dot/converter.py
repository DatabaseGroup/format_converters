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

from antlr4 import *
from ..grammar.BracketLexer import BracketLexer
from ..grammar.BracketParser import BracketParser
from ..grammar.BracketListener import BracketListener

class BracketDotListener(BracketListener):
    # Constructor
    def __init__(self):
        # initialize empty string
        self.bn = ''
        self.node_id = 0             # used to store incremented preorder id of a node
        self.nodes_stack = []        # stores parent ids to be available at exit
        self.current_node_stack = [] # stores node ids to be available at exit

    def enterNode(self, ctx):
        current_node = self.node_id
        self.bn += (str(current_node) + " [label=\"" + str(ctx.LABEL()) + "\"];\n")
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
            self.bn += (str(parent) + "->" + str(current_node) + "\n")

    # Getter for the bracket notation string.
    def get_dot_notation(self):
        return self.bn

def convert(source):

    lexer = BracketLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = BracketParser(stream)
    tree = parser.node()
    listener = BracketDotListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    output = "digraph G {\nnode [shape=none];\nedge [dir=none];\n" # dot preamble
    output += listener.get_dot_notation()
    output += "}" # dot final closing bracket

    return output
