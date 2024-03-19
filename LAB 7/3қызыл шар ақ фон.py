
"""
please, download the picture for icon or:
if my code didn't work, please delete the icon_image(line 17 and 18)
"""

import sys, pygame

pygame.init()

s_w = 600
s_h = 600
screen = pygame.display.set_mode((s_w, s_h), pygame.RESIZABLE)
done = False
pygame.display.set_caption("Bounce Tales: Оrigins")

icon_image = pygame.image.load("C:\\Users\\User\\Desktop\\красны.png")
pygame.display.set_icon(icon_image)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x = s_w//2
y = s_h//2

fps = pygame.time.Clock()

def draw_ball(x, y):
    pygame.draw.circle(screen, RED, (x, y), radius)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.VIDEORESIZE:
            s_w = event.w
            s_h = event.h
            screen = pygame.display.set_mode((s_w, s_h), pygame.RESIZABLE)
            
        elif event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20
            if event.key == pygame.K_RIGHT:
                x += 20
            elif event.key == pygame.K_LEFT:
                x -= 20

    x = max(radius, min(x, s_w - radius))
    y = max(radius, min(y, s_h - radius))
            
    screen.fill(WHITE)
    draw_ball(x, y)

    fps.tick(60)
            
    pygame.display.flip()

pygame.quit()


