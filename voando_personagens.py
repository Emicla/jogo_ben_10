import pygame, random, os

os.system("cls")

nome = input("Informe seu nome: ")
email = input("Informe seu email: ")

pygame.init()

largura_tela = 1200
altura_tela = 600
tamanho = (largura_tela, altura_tela)

pygame_display = pygame.display
pygame_display.set_caption("Voando com personagens")

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

def escreveTela(texto, cor, tamanho):
    fonte = pygame.font.Font("freesansbold.ttf", tamanho)
    frase = fonte.render(texto, True, cor)
    return frase

def telaMenu(telaAtual, nivel):
    imagemMenu = pygame.image.load("Imagens/Imagem menu.jpg")
    corOp1 = (0, 228, 251)
    corOp2 = (255, 255, 255)
    corBorda = (0, 228, 251)
    selecionado = 190
    opcao1 = "Jogo"
    opcao2 = "Como jogar"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selecionado == 190:
                        selecionado += 130
                        corOp1 = (255, 255, 255)
                        corOp2 = (0, 228, 251)
                    else:
                        selecionado -= 130
                        corOp1 = (0, 228, 251)
                        corOp2 = (255, 255, 255)

                elif event.key == pygame.K_DOWN:
                    if selecionado == 320:
                        selecionado -= 130
                        corOp1 = (0, 228, 251)
                        corOp2 = (255, 255, 255)
                    else:
                        selecionado += 130
                        corOp1 = (255, 255, 255)
                        corOp2 = (0, 228, 251)

                elif event.key == pygame.K_RETURN:
                    if selecionado == 190:
                        return opcao1

                    elif selecionado == 320:
                        return opcao2

        if telaAtual == "Menu":
            gameDisplay.blit(imagemMenu, (0, 0))
            opcao1 = "Jogo"
            opcao2 = "Como jogar"

        elif telaAtual == "Jogo":
            opcao1 = "Jogo"
            opcao2 = "Loja"
            gameDisplay.fill((65, 81, 106))
            gameDisplay.blit(escreveTela("Nível: %d"%int(nivel), (255, 255, 255), 25), (100, 100))
            corBorda = (255, 255, 255)

        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(216, 190, 500, 90))
        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(216, 320, 500, 90))
        pygame.draw.rect(gameDisplay, corBorda, pygame.Rect(216, selecionado, 500, 90), 2)

        gameDisplay.blit(escreveTela(opcao1, corOp1, 50), (375, 215))
        gameDisplay.blit(escreveTela(opcao2, corOp2, 50), (375, 343))

        pygame_display.update()
        clock.tick(60)

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
    missilPosX = 0
    missilPosY = 0
    movimentoXMissil = -5
    missilLargura = 150
    missilAltura = 40

    robo = pygame.image.load("Imagens/robo vilgax.png")
    roboAltura = 217
    roboLargura = 198
    roboPosX = 20
    roboPosY = 100
    movimentoXRobo = 5

    missilLiberado = False
    viraMissil = False
    velocidadeIncremento = 1

    pygame.mixer.music.load("Sons/Ben 10 abertura.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    virou = False

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
                    if missilLiberado == False:
                        viraMissil = False
                        movimentoXMissil = -5
                    movimentoXPersonagem = - velocidade

                elif event.key == pygame.K_RIGHT:
                    if virou == False:
                        insectoide = pygame.transform.flip(insectoide, True, False)
                        virou = True
                    if missilLiberado == False:
                        viraMissil = True
                        movimentoXMissil = 5
                    movimentoXPersonagem = velocidade
                
                elif event.key == pygame.K_UP:
                    movimentoYPersonagem = -velocidade

                elif event.key == pygame.K_DOWN:
                    movimentoYPersonagem = velocidade
                
                elif event.key == pygame.K_a and missilLiberado == False:
                    missilLiberado = True
                    missilPosX = insectoidePosX
                    missilPosY = insectoidePosY

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

        pixelsXRobo = list(range(roboPosX, roboPosX + roboLargura + 1))
        pixelsYRobo = list(range(roboPosY, roboPosY + roboAltura + 1))

        pixelsXMissel = list(range(missilPosX, missilPosX + missilLargura + 1))
        pixelsYMissel = list(range(missilPosY, missilPosY + missilAltura + 1))

        if len(list(set(pixelsYRobo) & set(pixelsYInsectoide))) > 60:
            if len(list(set(pixelsXRobo) & set(pixelsXInsectoide))) > 65:
                print(len(list(set(pixelsXRobo) & set(pixelsXInsectoide))))
                print(len(list(set(pixelsYRobo) & set(pixelsYInsectoide))))
                print("Morreu")
                return ["Morreu", pontos]
        
        if len(list(set(pixelsYRobo) & set(pixelsYMissel))) > 25:
            if len(list(set(pixelsXRobo) & set(pixelsXMissel))) > 25:
                print("Acertou")
                missilLiberado = False
                missilPosX = 0
                missilPosY = 0
                pontos = pontos + 1
                roboPosY = random.randrange(0, altura_tela - roboAltura)
                numeroAleatorio = random.randrange(1, 3)
                movimentoXRobo = movimentoXRobo + velocidadeIncremento
                if numeroAleatorio == 1:
                    roboPosX = 0 - roboLargura
                    if movimentoXRobo < 0:
                        movimentoXRobo = -(movimentoXRobo)
                else:
                    roboPosX = largura_tela
                    if movimentoXRobo > 0:
                        movimentoXRobo = -(movimentoXRobo)
                    
                    
        elif roboPosX > largura_tela or roboPosX < 0 - roboLargura:
            movimentoXRobo = -movimentoXRobo
            velocidadeIncremento = -velocidadeIncremento
            roboPosY = random.randrange(0, altura_tela - roboAltura)
            robo = pygame.transform.flip(robo, True, False)
            print(roboPosX)

        roboPosX = roboPosX + movimentoXRobo

        # Desenhando na tela as imagens
        gameDisplay.fill((195, 100, 30)) #Mudando a cor do fundo
        gameDisplay.blit(robo, (roboPosX, roboPosY))
        gameDisplay.blit(insectoide, (insectoidePosX, insectoidePosY))

        # Escrevendo na tela
        fonte = pygame.font.Font("freesansbold.ttf", 20)
        texto = fonte.render("Pontos: " + str(pontos),True, corLetra)
        gameDisplay.blit(texto, (20, 20))

        if missilLiberado == True and missilPosX > 0 and missilPosX + missilLargura < largura_tela:
            gameDisplay.blit(missil, (missilPosX, missilPosY))

            if viraMissil == True:
                missil = pygame.transform.flip(missil, True, False)
                viraMissil = False
            
            missilPosX += movimentoXMissil
        else:
            missilLiberado = False


        pygame_display.update()
        clock.tick(60)

telaAtual = "Jogar"

while True:
    if telaAtual == "Jogar":
        lista = jogo(pontos)
        telaAtual = lista[0]
        pontos = lista[1]

    elif telaAtual == "Morreu":
        telaAtual = morreu(pontos)
        pontos = 0