import pygame, os

pygame.init()

from Funcoes.funcoes_jogo import escreveTela

largura_tela = 1200
altura_tela = 600
tamanho = (largura_tela, altura_tela)

pygame_display = pygame.display

gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()

def telaMenu(pontos):
    escolhendo = pygame.mixer.Sound("Sons/som escolha.mp3")
    escolhendo.set_volume(0.5)

    corOp1 = (0, 228, 251)
    corOp2 = (255, 255, 255)
    corOp3 = (255, 255, 255)
    corBorda = (0, 228, 251)
    selecionado = 170
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(escolhendo)
                if event.key == pygame.K_UP:
                    if selecionado == 170:
                        selecionado = 410
                    else:
                        selecionado -= 120

                elif event.key == pygame.K_DOWN:
                    if selecionado == 410:
                        selecionado = 170
                    else:
                        selecionado += 120

                elif event.key == pygame.K_RETURN:
                    if selecionado == 170:
                        return "Jogo"

                    elif selecionado == 290:
                        return "Loja"

                    elif selecionado == 410:
                        return "Como jogar"
                        
        if selecionado == 170:
            corOp1 = (0, 228, 251)
            corOp2 = (255, 255, 255)
            corOp3 = (255, 255, 255)

        elif selecionado == 290:
            corOp1 = (255, 255, 255)
            corOp2 = (0, 228, 251)
            corOp3 = (255, 255, 255)

        elif selecionado == 410:
            corOp1 = (255, 255, 255)
            corOp2 = (255, 255, 255)
            corOp3 = (0, 228, 251)

        gameDisplay.fill((65, 81, 106))
        
        gameDisplay.blit(escreveTela("Pontos: %d"%int(pontos), (255, 255, 255), 25), (100, 100))

        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(300, 170, 500, 90))
        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(300, 290, 500, 90))
        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(300, 410, 500, 90))
        pygame.draw.rect(gameDisplay, corBorda, pygame.Rect(300, selecionado, 500, 90), 2)

        gameDisplay.blit(escreveTela("Jogo", corOp1, 50), (480, 190))
        gameDisplay.blit(escreveTela("Loja", corOp2, 50), (480, 310))
        gameDisplay.blit(escreveTela("Como jogar", corOp3, 50), (430, 430))

        pygame_display.update()
        clock.tick(60)

def telaLoja(dinheiro):
    escolhendo = pygame.mixer.Sound("Sons/som escolha.mp3")
    escolhendo.set_volume(0.5)

    selecionado = 1
    corBorda = (0, 228, 251)
    cadiado = "cadiado"
    nomesPersonagens = ["insectoide","angry birds", "Lanterna Verde", "super choque", "homem de ferro"]
    posicoes = [200, 350, 500, 650, 800]
    liberados = 1
    personagensLiberados = []
    minimo = 1

    while minimo < dinheiro:
        if liberados >= len(nomesPersonagens):
            break
        else:
            minimo += 10
            liberados += 1
        os.system("cls")
        print(minimo)
        print(liberados)
    
    for posicaoNomes in range(0, liberados):
        personagensLiberados.append(nomesPersonagens[posicaoNomes])
    
    while len(personagensLiberados) < len(nomesPersonagens):
        personagensLiberados.append(cadiado)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(escolhendo)
                if event.key == pygame.K_LEFT:
                    if selecionado == 1:
                        selecionado = len(personagensLiberados)
                    else:
                        selecionado -= 1
                
                elif event.key == pygame.K_RIGHT:
                    if selecionado == len(personagensLiberados):
                        selecionado = 1
                    else:
                        selecionado += 1

                elif event.key == pygame.K_RETURN:
                    personagemEscolhido = personagensLiberados[selecionado-1]
                    if personagemEscolhido != cadiado:
                        return ["Menu", personagemEscolhido]

        gameDisplay.fill((65, 81, 106))

        for posicao, personagem in enumerate(personagensLiberados):
            imagemPersonagem = pygame.image.load("Imagens/Personagens/" + personagem + ".png")
            gameDisplay.blit(imagemPersonagem, (posicoes[posicao], 200))

        gameDisplay.blit(escreveTela("Use as setas e clique Enter para selecionar", (255, 255, 255), 30), (25, 120))
        pygame.draw.rect(gameDisplay, corBorda, pygame.Rect(posicoes[selecionado - 1] - 13, 200-3, 125, 143), 2)

        pygame_display.update()
        clock.tick(60)
    
def telaComoJogar():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return "Menu"

        gameDisplay.fill((65, 81, 106))
        gameDisplay.blit(escreveTela("- Use as setas do teclado para movimentar o personagem", (255, 255, 255), 30), (25, 150))
        gameDisplay.blit(escreveTela("- Precione [A] para lançar poder e destruir a nave", (255, 255, 255), 30), (25, 255))
        gameDisplay.blit(escreveTela("- Destrua o máximo de robos para ganhar pontos e liberar personagens", (255, 255, 255), 30), (25, 350))
        gameDisplay.blit(escreveTela("Precione [X] para Sair", (0,0,0), 30), (30, 500))
        pygame_display.update()
        clock.tick(60)

def morreu(pontos):
    fundo_perdeu = pygame.image.load("Imagens/Fim de jogo.jpg")
    omnitrixDescarregando = pygame.mixer.Sound("Sons/Omnitrix Descarregando.mp3")
    omnitrixDescarregando.set_volume(0.1)
    corPreta = (0, 0, 0)
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(omnitrixDescarregando)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "Jogo"

                elif event.key == pygame.K_x:
                    return "Menu"

        gameDisplay.blit(fundo_perdeu, (0, 0))
        gameDisplay.blit(escreveTela("Você morreu com " + str(pontos) + " pontos", (255, 255, 255 ), 40), (20, 20))
        gameDisplay.blit(escreveTela("Precione Enter para recomessar", (255, 255, 255 ), 30), (700, 560))
        gameDisplay.blit(escreveTela("Precione [X] para Sair", corPreta, 30), (25, 560))
        pygame_display.update()
