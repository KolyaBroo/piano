from pygame import *
from settings import *
from sounds import load_sounds
from buttons import PianoButton
from effects import press_effect, release_effect

init()

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sounds = load_sounds(KEY)

pressed_keys = set()
keys_list = list(KEY.keys())


button_image = image.load(
    "assets/images/Button.png"
).convert_alpha()

button_width = SCREEN_WIDTH // len(keys_list)
button_height = SCREEN_HEIGHT
buttons = []

for i, key_name in enumerate(keys_list):
    x = i * button_width
    button = PianoButton(
        button_image,
        x,
        0,
        button_width,
        button_height,
        key_name
    )

    buttons.append(button)

running = True
while running:
    screen.fill(WHITE)
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                pressed_keys.add(idx)
                press_effect(buttons[idx])

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in sounds:
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)
                    release_effect(buttons[idx])

    for button in buttons:
        button.draw(screen)

    display.flip()
    time.delay(50)
    
quit()