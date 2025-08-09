import pygame

class DestructionAnimation(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.frames = 15  # Number of frames for the animation
        self.current_frame = 0
        self.position = pygame.Vector2(position)
        self.radius = 5
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        self.current_frame += 1
        self.radius += 2  # Expand effect
        self.image.fill((0, 0, 0, 0))  # Clear
        pygame.draw.circle(self.image, (255, 255, 0, max(0, 255 - self.current_frame * 16)), (15, 15), self.radius)
        if self.current_frame > self.frames:
            self.kill()