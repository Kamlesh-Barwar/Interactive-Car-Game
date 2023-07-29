import pygame
from pygame.locals import *
import random
import math
pygame.init()

# FPS
fps = 60
clock = pygame.time.Clock()

# Screen size
screen = pygame.display.set_mode((900, 768))

# Title and Icon
pygame.display.set_caption('Car Game')
icon = pygame.image.load('data/icon.ico')
pygame.display.set_icon(icon)

# Main menu
main = pygame.image.load('data/Main_menu.jpg')
play = pygame.image.load('data/play.png')
control = pygame.image.load('data/controls.png')
quit_game = pygame.image.load('data/quit.png')
menu = pygame.image.load('data/control_menu.jpg')


# Player
playerImg = pygame.image.load('data/player.png')
lightplayerImg = pygame.image.load('data/light_player.png')
enemyImg = [pygame.image.load('data/green_car.png'), pygame.image.load('data/blue_car.png'), pygame.image.load('data/purple_car.png')]
sideImg = pygame.image.load('data/side.png')
expImg = pygame.image.load('data/explosion.png')
powerup = [pygame.image.load('data/red_bullet.png'), pygame.image.load('data/blue_bullet.png')]
powerup1 = [pygame.image.load('data/red.png'), pygame.image.load('data/blue.png'), pygame.image.load('data/light.png')]
gameover_logo = pygame.image.load('data/game-over.png')
pointerImg = pygame.image.load('data/pointer.png')

# Intializing all values
place = [40, 180, 330, 470]
place1 = [-300, -500, -700, -600]
playerX = 320
playerY = 570
enemyX = [random.choice(place), random.choice(place), random.choice(place)]
enemyY = [random.choice(place1), random.choice(place1), random.choice(place1)]
score = 0
bulletX = [0, 0, 0, 0, 0]
bulletY = [0, 0, 0, 0, 0]
fire = [False, False, False, False, False]
bchangeY = 5
pchangeX = 0
pchangeY = 0
echangeY = 7
ammo = [5, 3, 0]
ptype = [0, 0, 0, 0, 0]
gameover = False
main_menu = True
power = 0
powerupX = [120, 265, 410]
new_powerX = [random.choice(powerupX), random.choice(powerupX), random.choice(powerupX)]
new_powerY = [random.choice(place1), random.choice(place1), random.choice(place1)]
prange = [random.choice(range(0, 1200)), random.choice((range(0, 1200))), random.choice((range(0, 1200)))]
time = 0
powerupbool = [False, False, False]
lighttime = 0

# Background
backImg = pygame.image.load('data/road_full.png')
backY = -1500


def player(x, y, a):
    if a == 0:
        screen.blit(playerImg, (x, y))
    else:
        screen.blit(lightplayerImg, (x, y))


def enemy(x, y, num):
    screen.blit(enemyImg[num], (x, y))


def bullet(x, y, p):
    if p == 0:
        screen.blit(powerup[0], (x, y))
    else:
        screen.blit(powerup[1], (x, y))

def Collision(ex, ey, x, y):
    distx = abs(ex - x)
    disty = abs(ey - y)
    if distx <= 76 and disty <= 186:
        return True


def explosion(x, y):
    screen.blit(expImg, (x, y))


def blast(bx, by, ex, ey):
    distx = bx - ex
    disty = abs(by - ey)
    if 0 <= distx <= 65 and disty <= 120:
        for i in range(15):
            explosion(ex, ey)
        return True


def taking(bx, by, x, y):
    distx = bx - x
    disty = abs(by - y)
    if 0 <= distx <= 60 and disty <= 100:
        return True
    if 0 <= distx <= 187 and disty <= 100:
        return True


controls_menu = False

while True:
    # Mainmenu
    if main_menu:
        if controls_menu:
            screen.blit(menu, (0, 0))
        else:
            screen.blit(main, (0, 0))
            screen.blit(play, (585, 220))
            screen.blit(control, (538, 327))
            screen.blit(quit_game, (490, 434))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if controls_menu:
                    controls_menu = False
                else:
                    x, y = pygame.mouse.get_pos()
                    if 585 <= x <= 810 and 220 <= y <= 300:
                        main_menu = False
                        gameover = False
                        place = [40, 180, 330, 470]
                        place1 = [-300, -500, -700, -600]
                        playerX = 320
                        playerY = 570
                        enemyX = [random.choice(place), random.choice(place), random.choice(place)]
                        enemyY = [random.choice(place1), random.choice(place1), random.choice(place1)]
                        score = 0
                        bulletX = [0, 0, 0, 0, 0]
                        bulletY = [0, 0, 0, 0, 0]
                        fire = [False, False, False, False, False]
                        bchangeY = 5
                        pchangeX = 0
                        pchangeY = 0
                        echangeY = 7
                        ammo = [5, 3, 0]
                        ptype = [0, 0, 0, 0, 0]
                        power = 0
                        powerupX = [120, 265, 410]
                        new_powerX = [random.choice(powerupX), random.choice(powerupX), random.choice(powerupX)]
                        new_powerY = [random.choice(place1), random.choice(place1), random.choice(place1)]
                        prange = [random.choice(range(0, 1200)), random.choice((range(0, 1200))),
                                  random.choice((range(0, 1200)))]
                        time = 0
                        lighttime = 0
                        powerupbool = [False, False, False]

                        # Background
                        backImg = pygame.image.load('data/road_full.png')
                        backY = -1500
                    if 538 <= x <= 763 and 327 <= y <= 407:
                        controls_menu = True
                    if 490 <= x <= 715 and 434 <= y <= 514:
                        pygame.quit()
                        quit()
        pygame.display.update()
        clock.tick(15)

    # Gameover
    elif gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu = True
        gameover_font = pygame.font.Font('freesansbold.ttf', 48)
        next_page = pygame.font.Font('freesansbold.ttf', 48)
        output = "Your Score : {} ".format(score)
        text1 = gameover_font.render(output, True, [0, 0, 0])
        text2 = next_page.render("Press click to continue..", True, [0, 0, 0])
        next_page_rect = text2.get_rect()
        next_page_rect.center = (450, 420)
        gameover_font_rect = text1.get_rect()
        gameover_font_rect.center = (450, 380)
        screen.blit(gameover_logo, (200, 230))
        screen.blit(text1, gameover_font_rect)
        screen.blit(text2, next_page_rect)
        pygame.display.update()
        clock.tick(15)

    # While Playing
    else:
        backY += 5
        if backY >= 45:
            backY = -1500
        screen.blit(backImg, (0, backY))
        screen.blit(sideImg, (600, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pchangeX = -4
                if event.key == pygame.K_RIGHT:
                    pchangeX = 4
                if event.key == pygame.K_UP:
                    pchangeY = -4
                if event.key == pygame.K_DOWN:
                    pchangeY = 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pchangeX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pchangeY = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    power = (power + 1) % 2
                if event.key == pygame.K_z:
                    if ammo[power] > 0:
                        for i in range(5):
                            if not fire[i]:
                                fire[i] = True
                                ptype[i] = power
                                bulletX[i] = playerX + 35
                                bulletY[i] = playerY
                                break
                        ammo[power] -= 1
        playerX += pchangeX
        playerY += pchangeY
        if playerX < 0 or playerX > 519:
            playerX -= pchangeX
        if playerY > 581 or playerY < 0:
            playerY -= pchangeY

        time = (time + 1) % 1001
        if ammo[2] > 0:
            lighttime += 1
            if lighttime == 230:
                lighttime = 0
                ammo[2] -= 1

        for t in range(3):
            if time == prange[t]:
                powerupbool[t] = True
                prange[t] = random.choice(range(0, 1200))

        for i in range(3):
            if powerupbool[i]:
                new_powerY[i] += 5
                screen.blit(powerup1[i], (new_powerX[i], new_powerY[i]))
                if taking(new_powerX[i], new_powerY[i], playerX, playerY):
                    if i == 0:
                        ammo[i] += 5
                    if i == 1:
                        ammo[i] += 2
                    if i == 2:
                        ammo[i] += 1
                    powerupbool[i] = False
                    new_powerY[i] = random.choice(place1)
                    new_powerX[i] = random.choice(powerupX)
                if new_powerY[i] >= 700:
                    powerupbool[i] = False
                    new_powerY[i] = random.choice(place1)
                    new_powerX[i] = random.choice(powerupX)

        for i in range(5):
            if fire[i]:
                bulletY[i] -= bchangeY
                bullet(bulletX[i], bulletY[i], ptype[i])
                if bulletY[i] < 0:
                    fire[i] = False

        player(playerX, playerY, ammo[2])
        for i in range(3):
            enemyY[i] += echangeY
            if enemyY[i] >= 700:
                enemyX[i] = random.choice(place)
                enemyY[i] = random.choice(place1)
                score += 1
            enemy(enemyX[i], enemyY[i], i)

        for i in range(5):
            if fire[i]:
                for j in range(3):
                    if blast(bulletX[i], bulletY[i], enemyX[j], enemyY[j]):
                        enemyY[j] = random.choice(place1)
                        enemyX[j] = random.choice(place)
                        score += 3
                        if ptype[i] == 0:
                            fire[i] = False

        for i in range(3):
            if Collision(enemyX[i], enemyY[i], playerX, playerY):
                if ammo[2] > 0:
                    if blast(enemyX[i], enemyY[i], enemyX[i], enemyY[i]):
                        enemyY[i] = random.choice(place1)
                        enemyX[i] = random.choice(place)
                        score += 3
                else:
                    gameover = True

        score_font = pygame.font.Font('freesansbold.ttf', 32)
        ammo0_font = pygame.font.Font('freesansbold.ttf', 32)
        ammo1_font = pygame.font.Font('freesansbold.ttf', 32)

        text = [score_font.render(str(score), True, [0, 0, 0]), ammo0_font.render('x' + str(ammo[0]), True, [0, 0, 0]), ammo1_font.render('x' + str(ammo[1]), True, [0, 0, 0])]
        score_font_rect = text[0].get_rect()
        ammo0_font_rect = text[1].get_rect()
        ammo1_font_rect = text[2].get_rect()

        score_font_rect.center = (770, 282)
        ammo0_font_rect.center = (690, 660)
        ammo1_font_rect.center = (810, 660)

        screen.blit(text[0], score_font_rect)
        screen.blit(text[1], ammo0_font_rect)
        screen.blit(text[2], ammo1_font_rect)
        if power == 0:
            screen.blit(pointerImg, (613, 500))
        else:
            screen.blit(pointerImg, (735, 500))
        pygame.display.update()
        clock.tick(fps)