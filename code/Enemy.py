from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.is_destroyed = False
    def move(self):
        self.rect.centerx -= 5
        if self.rect.right < 0:
            self.rect.right = 640
