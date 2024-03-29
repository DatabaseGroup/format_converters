# Format Converters for Tree-Structured Data

This repository contains format converters developed in the [Database Research Group](https://dbresearch.uni-salzburg.at/) for similarity search on tree-structured data.

## Bracket notation

The base format of our converters is the so-called **Bracket** notation. We convert to and from it. The bracket notation uses nested parentheses to represent the tree structure (nodes and labels).

A grammar describing the bracket notation currently looks as follows (in [ANTLR](http://www.antlr.org/) format):
```
node  : '{' LABEL? node* '}';
LABEL : [a-zA-Z0-9#_.:+-]+ ;
```

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

## Available converters

The following converters are currently available:
- **XML** to **Bracket**.
- **Newick** to **Bracket**: [Newick format](http://evolution.genetics.washington.edu/phylip/newicktree.html) is used to represent phylogenetic trees in evolutional biology.
- **Bracket** to **Dot**: Dot is a format to represent graphs used by [Graphviz](http://www.graphviz.org/).

## Licence

The source code is published under the MIT licence found in the root directory of the project and in the header of each source file.

**TODO:** The XML grammars have a BSD licence. It that a problem?

## Building process

Here we describe the general building process of our converters. Converter-specific execution details and examples are listed in the respective README files.

### Prerequisites

We've implemented our converters in [Python3](https://www.python.org/). We use [ANTLR4](http://www.antlr.org/) for grammars and parser generation.

#### ANTLR Tool
Download [ANTLR jar file](http://www.antlr.org/download.html) to the root directory of the format converters.
```
wget http://www.antlr.org/download/antlr-4.8-complete.jar
```

#### ANTLR Python runtime
The easiest method is to use pip. See [package website](https://pypi.python.org/pypi/antlr4-python3-runtime) for details.
Use `pip3` instead of `pip` on Debian.
```
pip install antlr4-python3-runtime
```

#### Compile all grammars
Execute the ``make.sh`` script to compile all grammars.
```
./make.sh
```

## Execution manual

Execute ``python format_converters --help`` for help.

## Using as a module in other projects.

Lets assume you have a Python script in the parent directory to ``format_converters`` and you want to import the bracket-to-dot converter. Then, you can import it and use as follows.
```python
import format_converters.tree_formats.bracket.dot.converter as BDConverter

source = "{a{b{d{f}}{e}}{c}}"
print(BDConverter.convert(source))
```
