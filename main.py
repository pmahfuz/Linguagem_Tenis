from abc import abstractmethod
import random
import sys
import time

global Player1SET
global Player2SET
global Player1Score
global Player2Score

def soma_ponto(id):
    global Player1Score, Player2Score
    if id == "1":
        if Player1Score == 30:
            Player1Score = 40
        else:
            Player1Score += 15
    elif id == "2":
        if Player2Score == 30:
            Player2Score = 40
        else:
            Player2Score += 15

class Symbol_Table():
    
    symbol_table = {}

    def getter(self, identifier):
        if identifier in self.symbol_table:
            return self.symbol_table[identifier]
        else:
            raise TypeError("Error, variavel não declarada")
        
    def setter(self, identifier, value):
        if identifier not in self.symbol_table:
            self.symbol_table[identifier] = value
        else:
            raise TypeError("Error, variavel já declarada")


class PrePro():
    def filter(code):
        code = code.split("\n")
        for i in range(len(code)):
            if "//" in code[i]:
                code[i] = code[i].split("//")[0]
        code = "\n".join(code)
        return code


class Node():
    def __init__(self, value, children):
        self.value = value
        self.children = children

    @abstractmethod
    def evaluate(self, st):
        pass

class Jogar(Node):
    def evaluate(self, st):
        for child in self.children:
            if child == None:
                continue
            child.evaluate(st)

class InicioGame(Node):
    def evaluate(self, st):
        print("---------------------------------")  
        print("MOMENTO RESERVADO PARA PROPAGANDAS")
        print("---------------------------------")
        time.sleep(3)
        propagandas = ["ROLEX", "FERRARI", "POLO", "TOMMY HILFIGER", "BUDWEISER", "NIKE", "ADIDAS", "PUMA", "LACOSTE", "GUCCI", "PRADA", "VERSACE", "LOUIS VUITTON", "APPLE", "SAMSUNG", "SONY", "BOSE", "RED BULL", "COCA-COLA", "PEPSI"]
        randomNumber = random.randint(0,19)
        print(f"{propagandas[randomNumber]} é muito bom!")
        print("---------------------------------")
        time.sleep(2)
        input("Pressione ENTER para continuar")
        print("Vamos começar o game!")

class FimGame(Node):
    def evaluate(self, st):
        pass

class Player(Node):
    def evaluate(self, st):
        nome = self.value
        numero = self.children[0]
        print(f"Jogador {numero} {nome}")
        return st.setter(numero, nome)

class Number(Node):
    def evaluate(self, st):
        return self.value

class Detalhes(Node):
    def evaluate(self, st):
        return self.value

class Correr(Node):
    def evaluate(self, st):
        direcao = self.children[0].evaluate(st)
        print(f"Jogador correu para {direcao}")

class Saque(Node):
    def evaluate(self, st):
        tipo = self.children[0].evaluate(st)
        forca = self.children[1].evaluate(st)
        if tipo == 'corpo':
            print(f"Saque {forca} no {tipo}")
        else:
            print(f"Saque {forca} {tipo}")
    
class Rebater(Node):
    def evaluate(self, st):
        lugar = self.children[0].evaluate(st)
        forca = self.children[1].evaluate(st)
        print(f"Rebateu {forca} na {lugar}")

class Ponto(Node):
    def evaluate(self, st):
        global Player1SET, Player2SET, Player1Score, Player2Score
        id = self.children[0].evaluate(st)
        soma_ponto(id)
        print(f"Ponto do jogador {id}")
        if Player1Score < 41 and Player2Score < 41:
            print(f"Placar do game: {Player1Score} X {Player2Score}")
            print("---------------------------------")
            time.sleep(1)
        else:
            Player1Score = 0
            Player2Score = 0
            print("---------------------------------")
            vencedor = st.getter(id)
            if id == "1":
                Player1SET += 1
            elif id == "2":
                Player2SET += 1
            print(f"Jogador {vencedor} venceu o game")
            print("---------------------------------")


class Finalizar(Node):
    def evaluate(self, st):
        global Player1SET, Player2SET
        player1 = st.getter("1")
        player2 = st.getter("2")
        print("O set foi finalizado com o resultado final de:")
        print(f"{player1} {Player1SET} X {Player2SET} {player2}")
    
class NoOp(Node):
    def evaluate(self, st):
        pass

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:

    # Palavras reservadas
    Reservadas = ["aberto", "fechado", "corpo", "esquerda", "direita", "frente", "forte", "medio", "fraco", "Inicio_game", "Fim_game"]
    Acoes = ["CORRER", "SAQUE", "REBATER", "MARCAR_PONTO", "FINALIZAR"]
    
    def __init__(self, source : str):
        self.source = source
        self.position = 0
        self.next = None
    
    def select_next(self):

            if self.position == len(self.source):
                self.next = Token("EOF", "")

            elif self.source[self.position].isdigit():
                numero = ""
                while  self.position < len(self.source) and self.source[self.position].isdigit() or self.source[self.position] == "/":
                    numero += self.source[self.position]
                    self.position += 1

                self.next = Token("INT", numero)

            elif self.source[self.position] == "(":
                self.next = Token("OPEN", self.source[self.position])
                self.position += 1
            
            elif self.source[self.position] == ")":
                self.next = Token("CLOSE", self.source[self.position])
                self.position += 1

            elif self.source[self.position] == "&":
                self.next = Token("JOGADOR", self.source[self.position])
                self.position += 1
            
            elif self.source[self.position] == "%":
                self.next = Token("ACAO", self.source[self.position])
                self.position += 1
            
            elif self.source[self.position] == "\n":
                self.next = Token("BREAK", self.source[self.position])
                self.position += 1
            
            elif self.source[self.position] == ",":
                self.next = Token("COMMA", self.source[self.position])
                self.position += 1

            elif self.source[self.position].isalpha():
                identificador = ""
                while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] in ["_", "-"]):
                    identificador += self.source[self.position]
                    self.position += 1
                
                if identificador in Tokenizer.Reservadas:
                    if(identificador == "aberto" ):
                        self.next = Token("TIPO_SAQUE", identificador)
                    elif(identificador == "fechado"):
                        self.next = Token("TIPO_SAQUE", identificador)
                    elif(identificador == "corpo"):
                        self.next = Token("TIPO_SAQUE", identificador)
                    elif(identificador == "esquerda"):
                        self.next = Token("DIRECAO", identificador)
                    elif(identificador == "direita"):
                        self.next = Token("DIRECAO", identificador)
                    elif(identificador == "frente"):
                        self.next = Token("DIRECAO", identificador)
                    elif(identificador == "forte"):
                        self.next = Token("FORCA", identificador)
                    elif(identificador == "medio"):
                        self.next = Token("FORCA", identificador)
                    elif(identificador == "fraco"):
                        self.next = Token("FORCA", identificador)
                    elif(identificador == "Inicio_game"):
                        self.next = Token("INICIO", identificador)
                    elif(identificador == "Fim_game"):
                        self.next = Token("FIM", identificador)
                elif identificador in Tokenizer.Acoes:
                    if(identificador == "CORRER"):
                        self.next = Token("ACOES", identificador)
                    elif(identificador == "SAQUE"):
                        self.next = Token("ACOES", identificador)
                    elif(identificador == "REBATER"):
                        self.next = Token("ACOES", identificador)
                    elif(identificador == "MARCAR_PONTO"):
                        self.next = Token("ACOES", identificador)
                    elif(identificador == "FINALIZAR"):
                        self.next = Token("ACOES", identificador)
                else:
                    self.next = Token("PALAVRA", identificador)

            elif self.source[self.position].isspace():
                self.position += 1
                self.select_next()
            
            else:
                raise ValueError(f"Error, caractere {self.source[self.position]} não reconhecido na posição {self.position}")

    
class Parser:
    

    def parse_set():
        resultado = Jogar("Jogar", [])
        while Parser.tokenizer.next.type != "EOF":
            resultado.children.append(Parser.parse_games())
        return resultado
    
    def parse_games():

        resultado = None

        if Parser.tokenizer.next.type == "BREAK":
            Parser.tokenizer.select_next()
            return NoOp("NoOp", [])
        
        elif Parser.tokenizer.next.type == "JOGADOR":
            Parser.tokenizer.select_next()
            player = ""
            
            while Parser.tokenizer.next.type != "BREAK" and Parser.tokenizer.next.value.isalpha():
                player += Parser.tokenizer.next.value
                Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "INT":

                number = Parser.tokenizer.next.value 
                Parser.tokenizer.select_next()
                resultado = Player(player, [])
                resultado.children.append(number)
                return resultado
        elif Parser.tokenizer.next.type == "INICIO":
            iniciar = InicioGame(Parser.tokenizer.next.value, [])
            Parser.tokenizer.select_next()
            return iniciar
        elif Parser.tokenizer.next.type == "FIM":
            fim = FimGame(Parser.tokenizer.next.value, [])
            Parser.tokenizer.select_next()
            return fim
        elif Parser.tokenizer.next.type == "ACAO":
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == "ACOES":
                acao = Parser.tokenizer.next.value
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type == "OPEN":
                    Parser.tokenizer.select_next()
                    detalhes = []
                    while Parser.tokenizer.next.type != "CLOSE":
                        detalhes.append(Parser.tokenizer.next.value)
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "COMMA":
                            Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "CLOSE":
                        Parser.tokenizer.select_next()
                        if Parser.tokenizer.next.type == "BREAK":
                            Parser.tokenizer.select_next()
                            if acao == "CORRER":
                                resultado = Correr(acao, [])
                                resultado.children.append(Detalhes(detalhes[0], []))
                                return resultado
                            elif acao == "SAQUE":
                                resultado = Saque(acao, [])
                                resultado.children.append(Detalhes(detalhes[0], []))
                                resultado.children.append(Detalhes(detalhes[1], []))
                                return resultado
                            elif acao == "REBATER":
                                resultado = Rebater(acao, [])
                                resultado.children.append(Detalhes(detalhes[0], []))
                                resultado.children.append(Detalhes(detalhes[1], []))
                                return resultado
                            elif acao == "MARCAR_PONTO":
                                resultado = Ponto(acao, [])
                                resultado.children.append(Number(detalhes[0], []))
                                return resultado
                            
                        else:
                            raise TypeError("Error, não tem quebra de linha")

                elif acao == "FINALIZAR":
                                resultado = Finalizar(acao, [])
                                return resultado
                else:
                    raise TypeError("Error, não tem (")
            else:
                raise TypeError("Error, não tem função")

        else:
            raise TypeError("Error")
        
            
    def run(code):

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()

        resultado = Parser.parse_set()

        if Parser.tokenizer.next.type == "EOF":
            return resultado
        else:
            raise TypeError("Error")

          

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        code = file.read() + '\n'
        code = PrePro.filter(code)



    st = Symbol_Table()
    Player1Score = 0
    Player2Score = 0
    Player1SET = 0
    Player2SET = 0
    root = Parser.run(code)
    root.evaluate(st)