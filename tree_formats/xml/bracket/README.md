# Standard XML Parser in Python2

Implementation of a standard
[XML](https://de.wikipedia.org/wiki/Extensible_Markup_Language) parser using the
[Python2 target](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)
of [ANTLR](http://www.antlr.org/) and the officially provided
[XML grammar](https://github.com/antlr/grammars-v4/xml) for
[ANTLR](http://www.antlr.org/).

## Directories

[`grammar`] The XML grammar are located in this directory (provided by
https://github.com/antlr/grammars-v4/xml).

[`test`] Contains a simple XML test file.

# Prerequisites

Working [ANTLR](http://www.antlr.org/) installation (see [5] and [6] for further
information).

# Build Process

If you have aliased the `antlr4` command, just use it as given below. If this
does not work for you, try using the following command instead of `antlr4`:

```bash
java -Xmx500M -cp "path/to/antlr-x.x.x-complete.jar:$CLASSPATH" org.antlr.v4.Tool
```

Of course you need to replace `path/to/antlr-x.x.x-complete.jar` with the
correct path on your system, e.g., `/opt/antlr4/antlr-4.7-complete.jar`.

Then, one can start the to build the parser classes using
[ANTLR](http://www.antlr.org/) as follows (assuming you are in the root
directory where this file is located):

```bash
# navigate to grammar subdirectory
cd grammar/

# build XMLLexer using Python2
# generates the files XMLLexer.py and XMLLexer.tokens in antlr_gen subdirectory
antlr4 -Dlanguage=Python2 -o ../antlr_gen XMLLexer.g4 

# build XMLLexer using Python2
# generates the files XMLParser.py, XMLParserListener.py, and XMLParser.tokens in antlr_gen subdirectory
antlr4 -Dlanguage=Python2 -o ../antlr_gen -lib ../antlr_gen XMLParser.g4

# navigate to xml root directory and generate __init__.py in antlr_gen subdir
cd .. && touch antlr_gen/__init__.py
```

Now, to execute the actual bracket notation converter just use the following
command:

```bash
python XMLToBracketNotationConverter.py test/test.xml
```

This should print the bracket notation representation of `test/test.xml` to
`stdout`.

# Example

Example XML file:

```xml
<dblp>
    <inproc year="2010" conf="ICDE">
        <author>N. Augsten</author>
        <author>D. Barbosa</author>
        <author>M. Boehlen</author>
        <author>T. Palpanas</author>
        <title>TASM: Top-k Approximate Subtree Matching</title>
    </inproc>
    <inproc year="2013" conf="SIGMOD">
        <author>S. Cohen</author>
        <title>Indexing for Subtree Similarity-Search using Edit Distance</title>
    </inproc>
</dblp>
```

Corresponding example tree (`o` denotes a node)

```
dblp
 o
 |        inproc
 +----------o
 |          |         conf       ICDE
 |          +----------o----------o
 |          |         year       2010
 |          +----------o----------o
 |          |        author    N. Augsten
 |          +----------o----------o
 |          |        author    D. Barbosa
 |          +----------o----------o
 |          |        author    M. Boehlen
 |          +----------o----------o
 |          |        author    T. Palpanas
 |          +----------o----------o
 |          |         title    TASM: Top-k Approximate Subtree Matching
 |          +----------o----------o
 |
 |        inproc
 +----------o
            |         conf       SIGMOD
            +----------o----------o
            |         year       2013
            +----------o----------o
            |        author    S. Cohen
            +----------o----------o
            |         title    Indexing for Subtree Similarity-Search using Edit Distance
            +----------o----------o
```

Corresponding bracket notation:

```
{dblp{inproc{conf{ICDE}}{year{2010}}{author{N. Augsten}}{author{D. Barbosa}}{author{M. Boehlen}}{author{T. Palpanas}}{title{TASM: Top-k Approximate Subtree Matching}}}{inproc{conf{SIGMOD}}{year{2013}}{author{S. Cohen}}{title{Indexing for Subtree Similarity-Search using Edit Distance}}}}
```

# References

[1] XML: https://de.wikipedia.org/wiki/Extensible_Markup_Language

[2] ANTLR Python targets: https://github.com/antlr/antlr4/blob/master/doc/python-target.md

[3] ANTLR: http://www.antlr.org/

[4] ANTLR grammars: https://github.com/antlr/grammars-v4

[5] ANTLR Download/Installation: http://www.antlr.org/download.html

[6] ANTLR Getting Started: https://github.com/antlr/antlr4/blob/master/doc/getting-started.md