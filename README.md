# Linguagem_Tenis

### EBNF:  
```
TENIS = { GAME } ;
GAME = ( PONTO ) ;
PONTO = ( TITULO DISPUTA | FINALIZAR )
DISPUTA = ( ACAO )
TITULO = "#", TEXTO, "\n" ;
ACAO = "%", ( SAQUE | REBATER | CORRER | MARCAR_PONTO | FINALIZAR ), "\n" ;
SAQUE = "SAQUE", "(", TIPO, ",", FORCA, ")" ;
REBATER = "REBATER", "(", DIRECAO, ",", FORCA, ")" ;
CORRER = "CORRER", "(", DIRECAO, ")" ;
MARCAR_PONTO = "MARCAR_PONTO" ;
FINALIZAR = "FINALIZAR" ;
TIPO = ( "ABERTO" | "FECHADO" | "CORPO" ) ;
DIRECAO = ( "ESQUERDA" | "DIREITA" | "FRENTE" ) ;
FORCA = ( "FRACO" | "MEDIO" | "FORTE" ) ;
LETRA = ( "a" | ... | "z" | "A" | ... | "Z" ) ;
DIGITO = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ) ;
TEXTO = { LETRA | DIGITO | " " | "-" | "_" } ;
```
