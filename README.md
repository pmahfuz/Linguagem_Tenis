# AceCode

### Descrição
Bem-vindo ao AceCode, uma linguagem de programação inovadora projetada para a simulação interativa de partidas de tênis. Com AceCode, os usuários podem inserir descrições detalhadas de cada ponto em uma partida de tênis, recebendo feedback em tempo real e o placar atualizado após cada jogada.

### Exemplo de programa:
```
& PEDRO 1
& FELIPE 2

Inicio_game

% SAQUE(aberto,medio)
% MARCAR_PONTO(1)

% SAQUE(aberto,medio)
% MARCAR_PONTO(1)

% SAQUE(corpo,forte)
% CORRER(direita)
% REBATER(esquerda,forte)
% MARCAR_PONTO(1)

% SAQUE(aberto,medio)
% CORRER(direita)
% REBATER(esquerda,fraco)
% CORRER(esquerda)
% MARCAR_PONTO(2)

% SAQUE(aberto,medio)
% MARCAR_PONTO(1)

Fim_game

% FINALIZAR

```

### Flex e Bison
A análise léxica e sintática da linguagem foi realizada utilizando o Flex e o Bison. Para compilar o programa, é essencial ter essas ferramentas instaladas. Para executar as análises, simplesmente execute os comandos apropriados no terminal.
```
flex -l jogar.l
bison -dv parser.y
gcc -o analyzer parser.tab.c lex.yy.c -lfl
./analyzer < ../jogada.txt
```

### Compilador
O compilador da AceCode é baseado no compilador criado para a linguagem GO durante a disciplina. Ele realiza todas as fases de análise - léxica, sintática e semântica - e simula a execução da receita no terminal.

Para compilar o programa de testes, é preciso ter o Python instalado. Para executá-lo, digite o seguinte comando no terminal:
```
python main.py jogada.txt
```


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

### Apresentação
A apresentação pode ser encontrada no arquivo AceCodePPT.pdf
