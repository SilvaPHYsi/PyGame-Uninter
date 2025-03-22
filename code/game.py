import pygame
from code.Menu import Menu
from code.const import WIN_HEIGHT, WIN_WEIGHT


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.menu = pygame.display.set_mode((WIN_HEIGHT, WIN_WEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            menu = Menu(self.menu)
            menu.run()
            pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()

        # self.screen.fill("purple")
        # pygame.display.flip()  # Atualiza a tela
        # self.clock.tick(60)


        pygame.mixer.music.stop()  # Para o áudio ao sair do loop
        pygame.quit()
