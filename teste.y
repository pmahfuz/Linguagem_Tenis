%start player

%%
player:
    VARIAVEL SPACE WORD BREAKLINE secondplayer BREAKLINE game
    ;

secondplayer:
    VARIAVEL SPACE WORD BREAKLINE
    ;

game:
    point BREAKLINE 
    ;

point:
    header BREAKLINE dispute BREAKLINE point
    | ACAO SPACE FINALIZAR
    ;

header:
    TITULO SPACE title_line
    ;

title_line:
    title
    | title_line SPACE title
    ;

title:
    WORD
    ;

dispute:
    ACAO SPACE action  
    ;

action:
    SAQUE LEFT_PARENTHESIS TIPO COMMA FORCA RIGHT_PARENTHESIS BREAKLINE dispute
    | REBATER LEFT_PARENTHESIS DIRECAO COMMA FORCA RIGHT_PARENTHESIS BREAKLINE dispute
    | CORRER LEFT_PARENTHESIS DIRECAO RIGHT_PARENTHESIS BREAKLINE dispute
    | MARCAR_PONTO BREAKLINE
    ;

%%