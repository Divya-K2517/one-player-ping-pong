import pygame
import sys
import random

pygame.init() #starts up pygame
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("One-player Ping Pong")
clock = pygame.time.Clock()
running = True
moving=False
Ball = False #whether there is a ball on the screen or not

paddle_x = 250
paddle_y=400
paddle = pygame.Rect(paddle_x, paddle_y, 100, 20)
ball_radius = 10
#ball = pygame.Rect(random.randint(0,WIDTH), random.randint(0,paddle_y), ball_radius,ball_radius)
og_speed_x = 5
og_speed_y = 5
ball_speed = [og_speed_x, og_speed_y]
ball_pos = [random.randint(0,WIDTH), random.randint(0,paddle_y)]
score = 0
high_score = 0
font = pygame.font.SysFont("Times New Roman", 20)


while running:
    dt = clock.tick(60)/1000  #time passed since last frame
    
    score_text = font.render("score: " + str(score), True, (247,220,255))
    score_rect = score_text.get_rect()
    score_rect.center = (int(WIDTH * 0.1), int(HEIGHT*0.1))

    high_score_text = font.render("high score: " + str(high_score), True, (247,220,255))
    high_score_rect = score_text.get_rect()
    high_score_rect.center = (int(WIDTH * 0.1), int(HEIGHT*0.05))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        #above 5 lines make it so the user has a way to close the screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if paddle.collidepoint(event.pos):
                moving=True
        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEMOTION and moving:
            paddle.move_ip(event.rel[0], 0) #only moves horizontally       
    
    screen.fill((0, 0, 0))
    screen.blit(surface, (0, 0))

    if Ball:
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]
        #making the ball reverse direction if it hits the side of the screen
        if ball_pos[0] <= ball_radius or ball_pos[0] >= WIDTH-ball_radius:
            ball_speed[0] = -ball_speed[0]
            if ball_pos[0] <= ball_radius:
                ball_pos[0] += 1
            if ball_pos[0] >= WIDTH-ball_radius:
                ball_pos[0] -=1
        #making the ball reverse direction if it hits the top of the screen
        if ball_pos[1] <= ball_radius:
            ball_speed[1] = -ball_speed[1]
            ball_pos[0] += 1
        #making the ball reverse direction if it hits the paddle
        if ball_pos[1] + ball_radius >= paddle.top and ball_pos[1] + ball_radius <= paddle.bottom and ball_pos[0] >= paddle.left and ball_pos[0] <= paddle.right:
            ball_speed[1] = -ball_speed[1]         
            ball_speed[0] *= 1.15
            ball_speed[1] *= 1.15
            score += 1
            if score > high_score:
                high_score += 1
        #checking if ball goes below the paddle
        if ball_pos[1] > HEIGHT:
            Ball=False
            score = 0
            ball_speed = [og_speed_x, og_speed_y]



    elif not Ball:
        ball_pos = [random.randint(0, WIDTH), random.randint(0, paddle_y)]
        Ball = True
    
    pygame.draw.rect(screen, (255,255,255), paddle) #draws paddle
    if Ball:
        pygame.draw.circle(screen, (255,255,255), ball_pos, ball_radius) #draws ball
    
    screen.blit(score_text, score_rect)
    screen.blit(high_score_text, high_score_rect)
    pygame.display.flip() #updates display

#quites pygame and closes the window
pygame.quit()
sys.exit()
