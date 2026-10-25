import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(75, 150, 100, 100))

    pygame.display.flip()

    GREEN = (0, 255, 0)
    
    pygame.draw.circle(screen, GREEN, (50, 50), 50)
    pygame.draw.circle(screen, GREEN, (200, 100), 50, 3)

    pygame.display.update

pygame.quit()