# Converter of bracket notation to dot

Implements of a bracket notation parser using the
[Python3 target](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)
of [ANTLR](http://www.antlr.org/). The parser is used to convert the input into a corresponding dot output.

## Files

`BracketNotation.g4` Contains a simple bracket notation grammar.

`bracket-to-dot.py` Takes tree in bracket notation from stdin and outputs the corresponding tree in dot to stdout.

# Prerequisites

## graphviz

Install [graphviz](http://www.graphviz.org/Download.php).

## ANTLR4

### ANTLR Tool
Download [ANTLR jar file](http://www.antlr.org/download.html) to root directory of `BracketNotationToDotConverter`.

### ANTLR Python runtime
The easiest method is to use pip3. See [package website](https://pypi.python.org/pypi/antlr4-python3-runtime) for details.
```
pip3 install antlr4-python3-runtime
```

# Build Process
Generate the parser files.
```bash
java -jar antlr-4.7-complete.jar -Dlanguage=Python3 BracketNotation.g4
```

# Execution
To execute the converter, use the following command:
```bash
python3 bracket-to-dot.py <your tree here>
```
To immediately view the dot graph in a viewer use:
```bash
python3 bracket-to-dot.py <your tree here> | dot -Tpng | <your PNG viewer here>
```
For MacOS use `open -f -a /Applications/Preview.app` for `<your PNG viewer here>`.

# Examples
Example tree in bracket notation:
```
{a{b{d{f}}{e}}{c}}
```
and its more natural view:
```
     a
    / \
   b   c
  / \
 d   e
 |
 f
```
The command:
```bash
python3 bracket-to-dot.py {a{b{d{f}}{e}}{c}}
```
results in the following dot output:
```dot
digraph G {
node [shape=none];
edge [dir=none];
0 [label="a"];
1 [label="b"];
2 [label="d"];
3 [label="f"];
2->3
1->2
4 [label="e"];
1->4
0->1
5 [label="c"];
0->5
}
```
