%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

LETTER [a-zA-Z]

%%

"\t"|"    "  {}
" " { printf("SPACE\n"); return SPACE; }
"\n" { printf("BREAKLINE\n"); return BREAKLINE; }
"#" { printf("Token Identified: TITULO\n"); return TITULO; }
"%" { printf("Token Identified: ACAO\n"); return ACAO; }
"&" { printf("Token Identified: VARIAVEL \n"); return VARIAVEL; }
"(" { printf("Token Identified: LEFT PARENTHESIS\n"); return LEFT_PARENTHESIS; }
")" { printf("Token Identified: RIGHT PARENTHESIS\n"); return RIGHT_PARENTHESIS; }
"," { printf("Token Identified: COMMA\n"); return COMMA; }
"SAQUE" { printf("Token Identified: SAQUE\n"); return SAQUE; }
"REBATER" { printf("Token Identified: REBATER\n"); return REBATER; }
"CORRER" { printf("Token Identified: CORRER\n"); return CORRER; }
"MARCAR_PONTO" { printf("Token Identified: MARCAR_PONTO\n"); return MARCAR_PONTO; }
"FINALIZAR" { printf("Token Identified: FINALIZAR\n"); return FINALIZAR; }
"aberto"|"fechado"|"corpo" { printf("Token Identified: TIPO\n"); return TIPO; }
"esquerda"|"direita"|"frente" { printf("Token Identified: DIRECAO\n"); return DIRECAO; }
"fraco"|"medio"|"forte" { printf("Token Identified: FORCA\n"); return FORCA; }

\"(\\.|[^\"\n])*\" { printf("Token Identified: STRING\n"); return STRING; }
[a-zA-Z_][_a-zA-Z0-9]* { printf("Token Identified: WORD\n"); return WORD; }

.  { printf("Unknown token: %s (ASCII: %d)\n", yytext, (int)yytext[0]); yyterminate(); };

%%