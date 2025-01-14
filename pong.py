import pygame , sys

pygame.init()

screen_width = 1280
screen_height= 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pong Game!")

clock = pygame.time.Clock()

while True:
    #check the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #update the display
    pygame.display.update()
    clock.tick(60)       