import pygame as py


class PianoButton:
    def __init__(self, image, x, y, width, height, key_name):
        self.key_name = key_name
        self.image = py.transform.scale(image, (width, height))
        self.normal_image = self.image.copy()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pressed = False

    def set_pressed(self, pressed):
        self.pressed = pressed

    def draw(self, screen):
        screen.blit(self.image, self.rect)