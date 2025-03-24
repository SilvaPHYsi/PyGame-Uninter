import pygame

from code.Level import Level
from code.Menu import Menu
from code.const import WIN_HEIGHT, WIN_WEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.menu = pygame.display.set_mode((WIN_HEIGHT, WIN_WEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Finaliza o loop ao receber o evento de saída

            menu = Menu(self.menu)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.menu, 'level1', menu_return)
                level.run()
            elif menu_return == MENU_OPTION[2]:
                self.running = False  # Alterando para finalizar o jogo ao escolher sair do menu
        pygame.quit()  # Finaliza o Pygame de forma segura após sair do loop principal





