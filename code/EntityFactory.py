from code.Background import Background
from code.const import WIN_WEIGHT

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                # Adicionando os objetos de fundo com a posição ajustada
                for i in range(7):
                    # Criando os objetos de fundo, com o nome de acordo com o arquivo de imagem
                    list_bg.append(Background(f'level1bg{i}.png', (0, 0)))  # Primeira posição
                    list_bg.append(Background(f'level1bg{i}.png', (WIN_WEIGHT, 0)))  # Segunda posição
                return list_bg
            case _:
                return []  # Caso não encontre o nome, retorna uma lista vazia

