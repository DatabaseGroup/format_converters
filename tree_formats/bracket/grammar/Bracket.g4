grammar Bracket;
node : '{' LABEL? node* '}';
LABEL : [ a-zA-Z0-9#_.,:+/-]+; /* [a-zA-Z0-9#_.:+-/]+ yields an error. */
WS : [\t\r\n]+ -> skip;

/* TODO: Escape curly brackets and allow in labels (ANTLR4 book p78).*/
