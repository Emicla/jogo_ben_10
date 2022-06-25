import pygame, random, os

pygame.init()

from Funcoes.funcoes_jogo import escreveTela

largura_tela = 1200
altura_tela = 600
tamanho = (largura_tela, altura_tela)

pygame_display = pygame.display

gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()

def telaMenu(pontos):
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
                if event.key == pygame.K_UP:
                    if selecionado == 170:
                        selecionado = 410
                        corOp1 = (255, 255, 255)
                        corOp2 = (0, 228, 251)
                    else:
                        selecionado -= 120
                        corOp1 = (0, 228, 251)
                        corOp2 = (255, 255, 255)

                elif event.key == pygame.K_DOWN:
                    if selecionado == 410:
                        selecionado = 170
                        corOp1 = (0, 228, 251)
                        corOp2 = (255, 255, 255)
                    else:
                        selecionado += 120
                        corOp1 = (255, 255, 255)
                        corOp2 = (0, 228, 251)

                elif event.key == pygame.K_RETURN:
                    if selecionado == 170:
                        return "Jogo"

                    elif selecionado == 290:
                        return "Loja"

                    elif selecionado == 410:
                        return "Como jogar"

        gameDisplay.fill((65, 81, 106))
        
        gameDisplay.blit(escreveTela("Pontos: %d"%int(pontos), (255, 255, 255), 25), (100, 100))
        corBorda = (255, 255, 255)

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
    selecionado = 1
    corOp1 = (0, 228, 251)
    corOp2 = (255, 255, 255)
    corBorda = (0, 228, 251)
    cadiado = "Imagens/cadiado.png"
    nomesPersonagens = ["Imagens/insectoide.png","Imagens/angry birds.png", "Imagens/Lanterna Verde.png", "Imagens/super choque.png"]
    posicoes = [200, 350, 500, 650]
    liberados = 1
    personagensLiberados = []
    minimo = 1

    while minimo < dinheiro:
        if liberados >= len(nomesPersonagens):
            break
        else:
            minimo += 5
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
                if event.key == pygame.K_LEFT:
                    if selecionado == 1:
                        selecionado = len(personagensLiberados)
                    else:
                        selecionado -= 1

                elif event.key == pygame.K_RETURN:
                    personagemEscolhido = personagensLiberados[selecionado-1]
                    if personagemEscolhido != cadiado:
                        return ["Menu", personagemEscolhido]

        gameDisplay.fill((65, 81, 106))

        for posicao, personagem in enumerate(personagensLiberados):
            imagemPersonagem = pygame.image.load(personagem)
            gameDisplay.blit(imagemPersonagem, (posicoes[posicao], 200))

        # pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(216, 200, 500, 90))
        # pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(216, 200, 500, 90))
        pygame.draw.rect(gameDisplay, corBorda, pygame.Rect(posicoes[selecionado - 1] - 13, 200-3, 125, 143), 2)

        # gameDisplay.blit(escreveTela(opcao1, corOp1, 50), (375, 215))
        # gameDisplay.blit(escreveTela(opcao2, corOp2, 50), (375, 343))

        pygame_display.update()
        clock.tick(60)
    
def telaComoJogar():
    gameDisplay.blit(escreveTela("- Use as setas do teclado para movimentar o personagem", (0,0,0), 50), (25, 220))
    gameDisplay.blit(escreveTela("- Precione [A] para lançar poder para destruir a nave", (0,0,0), 30), (25, 300))
    gameDisplay.blit(escreveTela("Precione [X] para Sair", (0,0,0), 30), (25, 400))
    pygame_display.update()

def morreu(pontos):
    fundo_perdeu = pygame.image.load("Imagens/fundo_perdeu.jpg")
    omnitrixDescarregando = pygame.mixer.Sound("Sons/Omnitrix Descarregando.mp3")
    omnitrixDescarregando.set_volume(0.1)
    corPreta = (0, 0, 0)
    corVermelha = (255, 0, 0)
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
        gameDisplay.blit(escreveTela("Você morreu com " + str(pontos) + " pontos", corVermelha, 50), (25, 220))
        gameDisplay.blit(escreveTela("Precione Enter para recomessar", corPreta, 30), (25, 300))
        gameDisplay.blit(escreveTela("Precione [X] para Sair", corPreta, 30), (25, 400))
        pygame_display.update()
