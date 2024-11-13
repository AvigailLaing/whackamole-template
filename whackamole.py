import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        #Defines the size of the window
        clock = pygame.time.Clock()
        running = True

        mole_position = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #If you click the X at the top of the screen
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos #Where they click
                    #Find current position of the mole and see if it matches the mouse click
                    mole_rect = mole_image.get_rect(topleft=mole_position)
                    #Have to use collidepoint to see if it matches the rectangle where the mole is?
                    if mole_rect.collidepoint(x, y):
                        mole_position = (random.randint(0, 19) * 32, random.randint(0, 15) * 32)
                        #X can range in the 20 vertical lines, Y can range in the 16 horizontal lines
            screen.fill("light green")

            # 20x16 grid of 32x32 squares
            # This means 20 horizontal lines and 16 vertical lines
            # Line 1 (0,32) -> (640, 32) for horizontal
            # Line 1 (32,0) -> (32, 512) for vertical
            for i in range(1, 17):  # To draw 16 horizontal lines
                pygame.draw.line(screen, "dark green", (0, 32 * i), (640, 32 * i), 4)
            for i in range(1, 21):  # To draw 20 vertical lines
                pygame.draw.line(screen, "dark green", (32 * i,0), (32 * i,512), 4)


            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position)) #Have to initially draw it with the dynamic variable mole_position and not (0,0) or else it won't ever move
            pygame.display.flip()
            #Updates the screen
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
