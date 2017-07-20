grammar BracketNotation;
node : '{' LABEL node* '}';
LABEL : [a-z0-9]+ ;
WS : [ \t\r\n]+ -> skip;
