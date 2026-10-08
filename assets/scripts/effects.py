import pygame as py

def darken_image(image, amount=45):
    result = image.copy()
    dark_layer = py.Surface(result.get_size(), py.SRCALPHA)
    dark_layer.fill((0, 0, 0, amount))
    result.blit(dark_layer, (0, 0))
    return result

def press_effect(button):
    button.image = darken_image(button.normal_image)

def release_effect(button):
    button.image = button.normal_image.copy()