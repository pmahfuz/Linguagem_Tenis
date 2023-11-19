%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

LETTER [a-zA-Z]

%%

"\t"|"    "  {}
" " {}
"\n" { printf("BREAKLINE\n"); return BREAKLINE; }
"#" { printf("Token Identified: COMENTARIO\n"); return COMENTARIO; }
"%" { printf("Token Identified: ACAO\n"); return ACAO; }
"(" { printf("Token Identified: LEFT PARENTHESIS\n"); return LEFT_PARENTHESIS; }
")" { printf("Token Identified: RIGHT PARENTHESIS\n"); return RIGHT_PARENTHESIS; }
"," { printf("Token Identified: COMMA\n"); return COMMA; }
"SAQUE" { printf("Token Identified: SAQUE\n"); return SAQUE; }
"REBATER" { printf("Token Identified: REBATER\n"); return REBATER; }
"CORRER" { printf("Token Identified: CORRER\n"); return CORRER; }
"MARCAR_PONTO" { printf("Token Identified: MARCAR_PONTO\n"); return MARCAR_PONTO; }
"FINALIZAR" { printf("Token Identified: FINALIZAR\n"); return FINALIZAR; }
"ABERTO" | "FECHADO" | "CORPO" { printf("Token Identified: TIPO\n"); return TIPO; }
"ESQUERDA" | "DIREITA" | "FRENTE" { printf("Token Identified: DIRECAO\n"); return DIRECAO; }
"LEVE" | "MEDIO" | "FORTE" { printf("Token Identified: FORCA\n"); return FORCA; }

\"(\\.|[^\"\n])*\" { printf("Token Identified: STRING\n"); return STRING; }
[a-zA-Z_][_a-zA-Z0-9]* { printf("Token Identified: WORD\n"); return WORD; }

.  { printf("Unknown token: %s (ASCII: %d)\n", yytext, (int)yytext[0]); yyterminate(); };

%%