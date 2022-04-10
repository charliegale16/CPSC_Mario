import pygame


class Event():
    def __init__(self):
        pygame.key.set_repeat(1,1)

    def check_event(self, player, bkgd):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.on_ground = False
                    player.show(0, player.rotated, jump=player.on_ground)



        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if bkgd.x < bkgd.left_limit:
                bkgd.x += bkgd.speed
                player.rotated = True
                player.show(player.frame % 2, player.rotated, jump=player.on_ground)

        elif pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if bkgd.x > bkgd.right_limit:
                bkgd.x -= bkgd.speed
                player.rotated = False
                player.show(player.frame % 2, player.rotated, jump=player.on_ground)
        else:
            player.show(0, player.rotated, jump=player.on_ground)

        player.frame += player.speed_animation


        if player.on_ground == False:
            player.jump()
