import pygame
import sys

# קביעת גודל החלון
width, height = 800, 600

# קביעת מאפייני הכדורים
radius = 30
mass = 1

# קביעת המיקום ההתחלתי של הכדורים
x1, y1 = 200, 300
x2, y2 = 600, 300

# קביעת מהירויות הכדורים
speed1 = [2, 0]
speed2 = [0, 0]

# התחברות לחלון pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elastic Collision Simulation")

# לולאת התמרור
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # התנגשות אלסטית בין הכדורים
    if pygame.Rect(x1-radius, y1-radius, 2*radius, 2*radius).colliderect(pygame.Rect(x2-radius, y2-radius, 2*radius, 2*radius)):
        speed1[0], speed2[0] = speed2[0], speed1[0]
        speed1[1], speed2[1] = speed2[1], speed1[1]

    # עדכון מיקום הכדורים
    x1 += speed1[0]
    y1 += speed1[1]
    x2 += speed2[0]
    y2 += speed2[1]

    # בדיקה שהכדורים לא חורגים ממסגרת החלון
    if x1 <= radius or x1 >= width - radius:
        speed1[0] *= -1
    if y1 <= radius or y1 >= height - radius:
        speed1[1] *= -1
    if x2 <= radius or x2 >= width - radius:
        speed2[0] *= -1
    if y2 <= radius or y2 >= height - radius:
        speed2[1] *= -1

    # ציור הכדורים והצגה בחלון
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(x1), int(y1)), radius)
    pygame.draw.circle(screen, (0, 0, 255), (int(x2), int(y2)), radius)
    pygame.display.flip()

    # קביעת מהירות התמרור
    pygame.time.Clock().tick(60)
