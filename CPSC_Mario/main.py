import pygame
import player, event, display    # import files

pygame.font.init()                          # initializes internal fonts


event = event.Event()
play = player.Player()
background = display.Canvas(play)


# game loop
while True:
    background.show(play)
    event.check_event(play, background)
    play.end(background)


    background.time.tick(background.fps)
    pygame.display.update()
