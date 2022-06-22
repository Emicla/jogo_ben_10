import pygame, random
pygame.init()

largura_tela = 900
altura_tela = 500
tamanho = (largura_tela, altura_tela)

pygame_display = pygame.display
pygame_display.set_caption("Jogo Ben 10")

gameDisplay = pygame.display.set_mode(tamanho) #Tamanho da tela
iconeOminitrix = pygame.image.load("Imagens/icone_omnitrix.png")
pygame_display.set_icon(iconeOminitrix)

clock = pygame.time.Clock() #Armazena em uma variável o metodo de renderizar a tela

corLetra = (255, 255, 255)
corVermelha = (255, 0, 0)
corPreta = (0, 0, 0)
fundo = pygame.image.load("Imagens/fundo.png")
fundo_perdeu = pygame.image.load("Imagens/fundo_perdeu.jpg")

omnitrixDescarregando = pygame.mixer.Sound("Sons/Omnitrix Descarregando.mp3")
omnitrixDescarregando.set_volume(0.1)

pontos = 0

def morreu(pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(omnitrixDescarregando)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "Jogar"

        gameDisplay.blit(fundo_perdeu, (0, 0))
        fonte = pygame.font.Font("freesansbold.ttf", 30)
        fontePerdeu = pygame.font.Font("freesansbold.ttf", 50)
        texto = fontePerdeu.render("Você morreu com " + str(pontos) + " pontos", True, corVermelha)
        textoContinue = fonte.render("Precione Enter para recomessar", True, corPreta)
        gameDisplay.blit(texto, (25, 220))
        gameDisplay.blit(textoContinue, (25, 300))
        pygame_display.update()

def jogo(pontos):

    insectoide = pygame.image.load("Imagens/insectoide.png")
    insectoidePosX = 400
    insectoidePosY = 400
    movimentoXPersonagem = 0
    movimentoYPersonagem = 0
    velocidade = 5
    insectoideLargura =  100
    insectoideAltura = 136

    missil = pygame.image.load("Imagens/missil.png")
    missil = pygame.transform.flip(missil, True, False)
    missilPosX = 20
    missilPosY = 200
    movimentoXMissil = 5
    missilLargura = 150
    missilAltura = 40

    robo = pygame.image.load("Imagens/robo vilgax.png")
    roboAltura = 217
    roboLargura = 198
    roboPosX = 20
    roboPosY = 200 - (roboAltura / 2)

    pygame.mixer.music.load("Sons/Ben 10 abertura.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    virou = False
    direcao = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if virou == True:
                        insectoide = pygame.transform.flip(insectoide, True, False)
                        virou = False
                    movimentoXPersonagem = - velocidade

                elif event.key == pygame.K_RIGHT:
                    if virou == False:
                        insectoide = pygame.transform.flip(insectoide, True, False)
                        virou = True
                    movimentoXPersonagem = velocidade
                
                elif event.key == pygame.K_UP:
                    movimentoYPersonagem = -velocidade

                elif event.key == pygame.K_DOWN:
                    movimentoYPersonagem = velocidade
                
                elif event.key == pygame.K_a:
                    insectoide = pygame.image.load("Imagens/insectoide_tunado.png")
                    velocidade = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXPersonagem = 0
                    movimentoYPersonagem = 0
                    
                elif event.key == pygame.K_a:
                    insectoide = pygame.image.load("Imagens/insectoide.png")
                    velocidade = 5
                    if virou == True:
                        insectoide = pygame.transform.flip(insectoide, True, False)

        insectoidePosX += movimentoXPersonagem
        insectoidePosY += movimentoYPersonagem

        # Colisão com bordas da tela
        if insectoidePosX < 0:
            insectoidePosX = 0

        elif insectoidePosX >= largura_tela - insectoideLargura:
            insectoidePosX = largura_tela - insectoideLargura

        if insectoidePosY < 0:
            insectoidePosY = 0

        elif insectoidePosY >= altura_tela - insectoideAltura:
            insectoidePosY = altura_tela - insectoideAltura
        
        # Colisão com missil
        pixelsXInsectoide = list(range(insectoidePosX, insectoidePosX + insectoideLargura + 1))
        pixelsYInsectoide = list(range(insectoidePosY, insectoidePosY + insectoideAltura + 1))

        pixelsXMissel = list(range(missilPosX, missilPosX + missilLargura + 1))
        pixelsYMissel = list(range(missilPosY, missilPosY + missilAltura + 1))

        if len(list(set(pixelsYMissel) & set(pixelsYInsectoide))) > 25:
            if len(list(set(pixelsXMissel) & set(pixelsXInsectoide))) > 25:
                return ["Morreu", pontos]

        if direcao == True:
            if missilPosX < largura_tela - missilLargura:
                missilPosX = missilPosX + movimentoXMissil
            else:
                direcao = False
                missilPosY = random.randrange(0, altura_tela - missilAltura)
                roboPosY = missilPosY - (roboAltura / 2)
                roboPosX = missilPosX
                movimentoXMissil = movimentoXMissil + 1
                missil = pygame.transform.flip(missil, True, False)
                pontos = pontos + 1
        else:
            if missilPosX >= 0:
                missilPosX = missilPosX - movimentoXMissil
            else:
                direcao = True
                missilPosY = random.randrange(0, altura_tela - missilAltura)
                roboPosY = missilPosY - (roboAltura / 2)
                roboPosX = missilPosX
                movimentoXMissil = movimentoXMissil + 1
                missil = pygame.transform.flip(missil, True, False)
                pontos = pontos + 1

        # Desenhando na tela as imagens
        gameDisplay.fill((195, 100, 30)) #Mudando a cor do fundo
        #gameDisplay.blit(fundo, (0, 0)) # Fundo
        gameDisplay.blit(missil, (missilPosX, missilPosY))
        gameDisplay.blit(robo, (roboPosX, roboPosY))
        gameDisplay.blit(insectoide, (insectoidePosX, insectoidePosY))

        # Escrevendo na tela
        fonte = pygame.font.Font("freesansbold.ttf", 20)
        texto = fonte.render("Pontos: " + str(pontos),True, corLetra)
        gameDisplay.blit(texto, (20, 20))

        pygame_display.update()
        clock.tick(60)

cena = "Jogar"

while True:
    if cena == "Jogar":
        lista = jogo(pontos)
        cena = lista[0]
        pontos = lista[1]

    elif cena == "Morreu":
        cena = morreu(pontos)
        pontos = 0