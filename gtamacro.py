import pygame
import sys
from ahk import AHK
from time import sleep

ahk = AHK()
# ahk.type('hello, world!')
# ahk.send_input('Hello, {U+1F30E}{!}')
# {Esc}
# {Enter}


def buyBST():
    # send BST keystrokes here
    # m enter down down down down enter down enter
    ahk.type("m")
    ahk.send_input('{Enter}')
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Enter}')
    ahk.send_input('{Down}')
    ahk.send_input('{Enter}')


def callVeh():
    # send vehicle keystrokes here
    # m down down enter enter
    ahk.type("m")
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Enter}')
    ahk.send_input('{Enter}')

def callopp():
    # send keystrokes to call oppressor from terrorbyte
    # M Down Down Enter Down Down Down Enter Down Down Enter
    ahk.type("m")
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Enter}')
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Enter}')
    ahk.send_input('{Down}')
    ahk.send_input('{Down}')
    ahk.send_input('{Enter}')

def newseshon():
    # send keystrokes to join new session
    # esc SLEEP(2s) right enter sleep(500ms) up up up up enter
    ahk.send_input('{Esc}')
    sleep(2)
    ahk.send_input('{Right}')
    ahk.send_input('{Enter}')
    sleep(0.5)
    ahk.send_input('{Up}')
    ahk.send_input('{Up}')
    ahk.send_input('{Up}')
    ahk.send_input('{Up}')
    ahk.send_input('{Enter}')


# Initialize pygame
pygame.init()

# Set up display
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height), pygame.SRCALPHA)  # Enable per-pixel alpha

# Transparent background surface
background = pygame.Surface((window_width, window_height), pygame.SRCALPHA)  # Add alpha channel
background.fill((0, 0, 0, 128))  # Black with 50% transparency (128 alpha)

# Set up font
font = pygame.font.Font(None, 50)
bstkey = "B"
vehkey = ";"
oppkey = "]"
newses = "["
overlay_text = "GTAMACRO\nBuy BST: " + bstkey + "\nCall Vehicle: " + vehkey + "\nCall Oppressor: " + oppkey + "\nJoin new session: " + newses + ""
text_surface = font.render(overlay_text, True, (255, 255, 255))  # White text

# declare hotkeys for AHK
ahk.add_hotkey(bstkey, callback=buyBST)
ahk.add_hotkey(vehkey, callback=callVeh)
ahk.add_hotkey(oppkey, callback=callopp)
ahk.add_hotkey(newses, callback=newseshon)

# start the hotkeys
ahk.start_hotkeys()  # start the hotkey process thread

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw transparent background
    window.blit(background, (0, 0))  # Blit the transparent surface

    # Draw text overlay
    text_position = (50, 50)
    window.blit(text_surface, text_position)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
