import pygame

from code.Entity import Entity
from code.const import WIN_HEIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
    def update(self):
        pass

    def move(self, obstacles=[], game_over_callback=None):
        keys = pygame.key.get_pressed()

        # Movimento para direita e esquerda
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.centerx += 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.centerx -= 5

        # Inicializa variáveis de pulo e gravidade, se não existirem
        if not hasattr(self, 'vel_y'):
            self.vel_y = 0
            self.gravidade = 0.5
            self.no_chao = True

        # Pulo apenas se estiver no chão
        if (keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.no_chao:
            self.vel_y = -15
            self.no_chao = False

        # Aplica gravidade se estiver no ar
        if not self.no_chao:
            self.vel_y += self.gravidade
            self.rect.centery += self.vel_y

            # Verifica colisão com o "chão"
            if self.rect.bottom >= 280:
                self.rect.bottom = 280
                self.vel_y = 0
                self.no_chao = True

        # Verificação de colisão com obstáculos (inimigos ou plataformas)
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                print("Colisão detectada com obstáculo!")
                # Aciona a função de fim de jogo
                if game_over_callback:
                    game_over_callback()  # Chamando a função de fim de jogo
                return  # Sai do método move para não continuar a execução



