from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WEIGHT, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                # Adicionando os objetos de fundo com a posição ajustada
                for i in range(8):
                    # Criando os objetos de fundo, com o nome de acordo com o arquivo de imagem
                    list_bg.append(Background(f'level1bg{i}.png', (0, 0)))  # Primeira posição
                    list_bg.append(Background(f'level1bg{i}.png', (WIN_HEIGHT, 0)))  # Segunda posição
                return list_bg
            case 'Player':
                list_pl = []
                for i in range(8):
                    list_pl.append(Player(f'Player{i}.png', (0, 174)))
                return list_pl
            case 'enemy':
                list_en = []
                for i in range(8):
                    list_en.append(Enemy(f'enemy{0}.png', (576, 224)))
                return  list_en



