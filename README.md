# Linguagem_Tenis

### EBNF:  
```
TENIS = { INSTRUCAO } ;
INSTRUCAO = ( TITULO | EQUIPAMENTO | ACAO | COMENTARIO ) ;
TITULO = "#", TEXTO, "\n" ;
EQUIPAMENTO = "@", TEXTO, [ " ", QUANTIDADE ], "\n" ;
ACAO = "%", ( SAQUE | REBATER | CORRER | MARCAR_PONTO | FINALIZAR ), "\n" ;
SAQUE = "SAQUE", "(", DIRECAO, ",", FORCA, ")" ;
REBATER = "REBATER", "(", DIRECAO, ",", FORCA, ")" ;
CORRER = "CORRER", "(", DIRECAO, ")" ;
MARCAR_PONTO = "MARCAR_PONTO" ;
FINALIZAR = "FINALIZAR" ;
COMENTARIO = "//", TEXTO, "\n" ;
QUANTIDADE = NUMERO, " ", UNIDADE ;
DIRECAO = ( "ESQUERDA" | "DIREITA" | "FRENTE" | "ATRAS" ) ;
FORCA = ( "LEVE" | "MEDIO" | "FORTE" ) ;
IDENTIFICADOR = LETRA, { LETRA | DIGITO | "_" } ;
NUMERO = DIGITO, { DIGITO } ;
LETRA = ( "a" | ... | "z" | "A" | ... | "Z" ) ;
DIGITO = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ) ;
TEXTO = { LETRA | DIGITO | " " | "-" | "_" } ;
UNIDADE = { LETRA } ;
```
