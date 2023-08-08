import pygame
import time
import random
pygame.font.init()

#display
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fighter")

#set background
BG = pygame.transform.scale(pygame.image.load("space.jpeg"), (WIDTH, HEIGHT))

#set player spec
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

#set projectile spec
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

#text font
FONT = pygame.font.SysFont("Comic Sans", 30)

#func to create player, text, and projectile
def draw(player, elapsed_time, stars):
    WIN.blit(BG,(0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1 , "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    #control movement speed
    clock = pygame.time.Clock()

    #timer
    start_time = time.time()
    elapsed_time = 0

    #projectile
    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False

    #start game
    while run:
        #set clock speed
        star_count += clock.tick(60)

        #runtime
        elapsed_time = time.time() - start_time

        #generate projectile
        if star_count > star_add_increment:
            for i in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment -50)
            star_count = 0

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()

        #move player
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        #show projectile
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        #player lose
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()




if __name__ == "__main__":
    main()
    