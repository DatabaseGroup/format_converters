grammar newick;

tree: node ';';
node : label?                          // Leaf Node.
     | '(' node (',' node)* ')' node? // Internal node with at least one child.
     ;
label : key | ':' value | key ':' value;
key : (INT | FLOAT | STR) | ('\'' STR '\'' | '\'' INT '\'' | '\'' FLOAT '\'');
value : (INT | FLOAT);
// STR consist of at least one letter.
STR : [a-zA-Z0-9._#]*[a-zA-Z][a-zA-Z0-9._#]*;
INT : [0-9]+;
// allows to write float in "10e-3" format
FLOAT : [0-9]+ '.' [0-9]+ ([Ee] [+-] [0-9]+)?; 

WS : [ \t\r\n]+ -> skip;
