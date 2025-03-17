import pygame
import sys
import random

# Pygame initialization
pygame.init()  # אתחול של pygame

# Constants
width, height = 400, 300  # קביעת קבועים לגודל החלון
ball_radius = 20  # רדיוס הכדור
ball_color = (0, 0, 255)  # צבע הכדור
background_color = (255, 255, 255)  # צבע הרקע
fps = 60  # מספר הפריימים בשנייה(מהירות הכדורים)

# Ball properties
num_balls = 2  # מספר הכדורים
balls = [{'x': random.randint(ball_radius, width - ball_radius),
          'y': random.randint(ball_radius, height - ball_radius),
          'vx': random.uniform(-2, 2),
          'vy': random.uniform(-2, 2)} for _ in range(num_balls)]  # יצירת רשימה של כדורים

# Set the second ball (index 1) to have random initial velocity
balls[1]['vx'] = random.uniform(-2, 2)
balls[1]['vy'] = random.uniform(-2, 2)

# Increase the speed of both balls (multiply by a constant factor)
for ball in balls:
    ball['vx'] *= 2
    ball['vy'] *= 2  # כפל מהירות הכדורים בקבוע

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Elastic Collision Simulation')
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # יציאה מהתוכנית כאשר המשתמש סוגר את החלון

    # Update ball positions
    for ball in balls:
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']

        # Check for collisions with walls
        if ball['x'] - ball_radius <= 0 or ball['x'] + ball_radius >= width:
            ball['vx'] *= -1  # Reflect x velocity
            # התגובה להתנגשות עם הקיר: שינוי כיוון המהירות בציר x
        if ball['y'] - ball_radius <= 0 or ball['y'] + ball_radius >= height:
            ball['vy'] *= -1  # Reflect y velocity
            # התגובה להתנגשות עם הקיר: שינוי כיוון המהירות בציר y

    # Check for collisions between balls
    for i in range(num_balls):
        for j in range(i+1, num_balls):
            dx = balls[i]['x'] - balls[j]['x']
            dy = balls[i]['y'] - balls[j]['y']
            distance = pygame.math.Vector2(dx, dy).length()

            if distance <= 2 * ball_radius:
                # Elastic collision formula for 2D
                angle = pygame.math.Vector2(dx, dy).angle_to((1, 0))
                v1 = pygame.math.Vector2(balls[i]['vx'], balls[i]['vy']).rotate(-angle)
                v2 = pygame.math.Vector2(balls[j]['vx'], balls[j]['vy']).rotate(-angle)

                v1, v2 = v2, v1
                # החלפת מהירויות

                balls[i]['vx'], balls[i]['vy'] = v1.rotate(angle)
                balls[j]['vx'], balls[j]['vy'] = v2.rotate(angle)
                # החלפת המהירויות חזרה למערכת המקורית

    # Draw background
    screen.fill(background_color)  # צביעת הרקע

    # Draw balls
    for ball in balls:
        pygame.draw.circle(screen, ball_color, (int(ball['x']), int(ball['y'])), ball_radius)
        # ציור הכדורים על המסך

    pygame.display.flip()
    clock.tick(fps)  # המתנה קצרה שמתחילה את הלולאה הבאה לאחר זמן קבוע (כדי לשמור על מספר הפריימים בשנייה)
