import pygame

pygame.init()
window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()
background_img = pygame.image.load("")


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    window.fill([23,78,230])
    pygame.display.flip()
    clock.tick(60)