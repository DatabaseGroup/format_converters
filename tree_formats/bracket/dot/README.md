# Bracket notation to Graphviz dot

Parses bracket notation and converts to a Graphviz dot file.

Uses bracket notation grammar ``tree_formats/bracket/grammar/BracketNotation.g4``.

## Prerequisites

### graphviz

Install [graphviz](http://www.graphviz.org/Download.php).

## Execution
To execute the converter, use the following command:
```bash
python3 format_converters.py <your tree here> bracket-dot
```
To immediately view the dot graph in a viewer use:
```bash
python3 format_converters.py <your tree here> | dot -Tpng | <your PNG viewer here>
```
On Debian use `display` of ImageMagick for `<your PNG viewer here>`.

On MacOS use `open -f -a /Applications/Preview.app` for `<your PNG viewer here>`.

## Examples
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
python3 format_converters.py {a{b{d{f}}{e}}{c}} bracket-dot
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
