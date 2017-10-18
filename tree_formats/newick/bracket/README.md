# Converter of Newick Notation to Bracket Notation

Implements of a newick notation parser using the
[Python2 target](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)
of [ANTLR](http://www.antlr.org/). The parser is used to convert the newick notation into a corresponding bracket notation.

## Files

`newick.g4` Contains a newick notation grammar.

`NewickToBracketNotationConverter.py` Takes tree in newick notation from stdin and outputs the corresponding tree in bracket notation to stdout.

# Prerequisites

## ANTLR4

### ANTLR Tool
Download [ANTLR jar file](http://www.antlr.org/download.html) to root directory of `NewickNotationToBracketNotation`.

### ANTLR Python runtime
The easiest method is to use pip3. See [package website](https://pypi.python.org/pypi/antlr4-python2-runtime) for details.
```
pip3 install antlr4-python2-runtime
```

# Build Process
Generate the parser files.
```bash
java -jar antlr-4.7-complete.jar -Dlanguage=Python2 newick.g4
```

# Execution
To execute the converter, use the following command:
```bash
python NewickToBracketNotationConverter.py <your newick file here>
```

# Examples
Example tree in newick notation:
```
(A:10,(C:30,D:40):50):60;
```
and its more natural view:
```
      :60
     /    \
   :50    A:10
  /   \
C:30  D:40

```
The command:
```bash
python NewickToBracketNotationConverter.py example.newick;
```
results in the following bracket output:
```
{:60{A:10}{:50{C:30}{D:40}}}
```
