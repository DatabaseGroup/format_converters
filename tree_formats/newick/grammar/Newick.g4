grammar Newick;

tree: node ';';
node : label?                          // Leaf Node.
     | '(' node (',' node)* ')' label? // Internal node with at least one child.
     ;
label : key | ':' value | key ':' value;
key : (INT | FLOAT | STR) | ('\'' INT '\'' | '\'' FLOAT '\'' | '\'' STR '\'');
value : (FLOAT | INT);
// STR consist of at least one letter.
STR : [0-9_#|-]*[a-zA-Z][a-zA-Z0-9._#|-]*;
INT : [0-9]+;
// allows to write float in "10.1e-3" format
FLOAT : [0-9]+ '.' [0-9]+ ([Ee] [+-] [0-9]+)?;

WS : [ \t\r\n]+ -> skip;
