import os

def registrar(arquivo, informacoes):
    arquivo = open(arquivo, "w")
    arquivo.write(informacoes)
    arquivo.close()

def ler_registro(arquivo):
    try:
        arquivo = open(arquivo, "r")
        conteudo = arquivo.readlines()
        arquivo.close()
        return conteudo
        
    except:
        return []

def armazenar(informacao, arquivo):
    conteudo = ler_registro(arquivo)
    
    conteudo.append("%s\n"%informacao)

    registrar(arquivo, ''.join(conteudo))

def verificaInf(frase):
    while True:
        resposta = input(frase)
        os.system("cls")
        try:
            resposta = int(resposta)
            print("Não pode ser só números")

        except:
            if len(resposta) < 2:
                print("Deve conter mais de 2 letras")
            elif resposta[0] == " ":
                print("Por favor, sem espaços em branco no ínicio")
            else:
                return resposta