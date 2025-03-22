import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import Rect

from code.const import COLOR_TEXT_RED, MENU_OPTION, COLOR_TEXT_WHITE


class Menu:
    def __init__(self, menu):
        self.running = True
        self.menu = menu
        self.surf = pygame.image.load('./graphics/wivern.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        try:
            pygame.mixer.music.load('./sounds/ni_idea.wav')  # Carrega o áudio
            pygame.mixer.music.play(-1)  # Reproduz em loop infinito
        except pygame.error as e:
            print(f"Erro ao carregar o áudio: {e}")  # Trata erros de carregamento

        while self.running:  # Usa uma variável para controle do loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Sai do loop quando a janela for fechada
                    quit()

            self.menu.blit(source=self.surf, dest=self.rect)  # Desenha a imagem na tela
            self.menu_text(50, "Running", COLOR_TEXT_RED, (360, 75))
            self.menu_text(50, "Mage", COLOR_TEXT_RED, (360, 105))

            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], COLOR_TEXT_WHITE , (360, 180 + 40* i))


            pygame.display.flip()  # Atualiza a tela

        pygame.mixer.music.stop()  # Para o áudio antes de sair

    def  menu_text(self, text_size, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(None, size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.menu.blit(source=text_surf, dest=text_rect)

