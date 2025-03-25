import pygame
import time

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.const import WIN_WEIGHT, WIN_HEIGHT


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.extend(EntityFactory.get_entity('Player'))
        self.entity_list.extend(EntityFactory.get_entity('enemy'))
        self.clock = pygame.time.Clock()
        self.game_over_time = None
        self.score = 0  # Variável para armazenar a pontuação
        self.start_time = pygame.time.get_ticks()  # Marca o tempo de início do jogo
        self.last_score_update_time = self.start_time  # Inicializa o tempo da última atualização do score

    def run(self):
        running = True
        player = None
        enemies = []

        for ent in self.entity_list:
            if isinstance(ent, Player):
                player = ent
            if isinstance(ent, Enemy):
                enemies.append(ent)

        def game_over():
            self.fade_out()  # Fazendo o fade antes de exibir a tela de Game Over
            self.game_over_displayed = True  # Marcar que o game over foi exibido
            print("Fim de jogo!")
            pygame.display.flip()  # Força a atualização da tela
            self.show_game_over_screen()  # Exibe a tela de game over
            pygame.time.delay(2000)  # Espera 2 segundos para exibir o game over antes de encerrar o jogo

            nonlocal running
            running = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)

                if isinstance(ent, Player):
                    ent.move(enemies, game_over)
                else:
                    ent.move()

                # Se o inimigo for destruído, aumenta a pontuação
                if isinstance(ent, Enemy) and ent.is_destroyed:
                    self.update_score(10)  # Aumenta a pontuação em 10
                    self.entity_list.remove(ent)

            # Atualiza a pontuação com base no tempo
            self.update_score_over_time()

            # Exibe o score na tela
            self.display_score()

            # Verifica se o tempo de game over já passou
            if self.game_over_time and pygame.time.get_ticks() - self.game_over_time > 2000:
                self.show_game_over_screen()

            pygame.display.flip()  # Atualiza a tela
            self.clock.tick(30)  # Limita o FPS
        pygame.quit()  # Fecha o pygame quando o jogo acaba

    def update_score(self, points):
        """Função para atualizar a pontuação."""
        self.score += points

    def update_score_over_time(self):
        """Função para aumentar a pontuação com o passar do tempo."""
        current_time = pygame.time.get_ticks()  # Tempo em milissegundos desde o início do jogo

        # Se passou mais de um segundo desde a última atualização do score, aumenta o score
        if current_time - self.last_score_update_time >= 1000:  # Verifica se 1 segundo se passou
            self.score += 1  # Aumenta a pontuação em 1 a cada segundo
            self.last_score_update_time = current_time  # Atualiza o tempo da última atualização

    def display_score(self):
        """Função para exibir o score na tela."""
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))  # Texto branco

        # Exibe o texto no canto superior esquerdo da tela
        self.window.blit(score_text, (10, 10))

    def fade_out(self):
        # Função para fazer o fade (transição suave)
        fade_surface = pygame.Surface((WIN_HEIGHT, WIN_WEIGHT))  # Tela preta para o fade
        fade_surface.fill((0, 0, 0))  # Cor preta
        alpha = 0
        fade_surface.set_alpha(alpha)

        # Fade in (escurecendo a tela)
        for alpha in range(0, 255, 5):  # Aumenta a opacidade até 255
            fade_surface.set_alpha(alpha)
            self.window.blit(fade_surface, (0, 0))  # Aplica a tela preta cobrindo toda a tela
            pygame.display.flip()
            pygame.time.delay(10)  # Atraso para uma transição suave

    def show_game_over_screen(self):
        # Exibe a tela de Game Over
        font = pygame.font.SysFont('Arial', 50)
        game_over_text = font.render('GAME OVER', True, (255, 0, 0))  # Texto vermelho

        # Calcula a posição para centralizar o texto
        text_rect = game_over_text.get_rect(center=(WIN_HEIGHT // 2, WIN_WEIGHT // 2))

        # Exibe o texto centralizado na tela
        self.window.blit(game_over_text, text_rect)
        pygame.display.flip()
