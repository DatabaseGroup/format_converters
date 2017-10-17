grammar Bracket;
node : '{' LABEL? node* '}';
LABEL : [a-zA-Z0-9#_.:+-]+ ;
WS : [ \t\r\n]+ -> skip;
