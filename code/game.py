import pygame
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.menu = pygame.display.set_mode((800, 400))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            menu = Menu(self.menu)
            menu.showMenu()
            pass

            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #       self.running = False

           # self.screen.fill("purple")
           # pygame.display.flip()  # Atualiza a tela
           # self.clock.tick(60)

        pygame.quit()


