#!/bin/sh

# A list of grammars of all converters that will be compiled.
# NOTE: If parser is separate form lexer, '-lib' option must be provided.
GRAMMARS_TO_COMPILE=(\
  bracket/grammar/Bracket.g4\
  newick/grammar/Newick.g4\
  xml/grammar/XMLLexer.g4\
  "-lib xml/grammar xml/grammar/XMLParser.g4"
)

INIT_DIRS=(\
  bracket\
  bracket/dot\
  bracket/grammar\
)

# Java command.
JAVA="java -jar"

# Path to ANTLR4 Jar file.
ANTLR4_JAR="antlr-4.7-complete.jar"

# Common parameters of ANTLR4.
ANTLR4_PARAMS="-Dlanguage=Python3"

# Compile all grammars.
# for g in "${GRAMMARS_TO_COMPILE[@]}" ; do
  # $JAVA $ANTLR4_JAR $ANTLR4_PARAMS $g ;
# done

# Generate empty python __init__.py files.
# for id in "${INIT_DIRS[@]}" ; do
#   touch $id/__init__.py ;
# done
