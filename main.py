import pygame
import sys
import neunet

import utils

# Constants
IMAGES_FILE = "train-images.idx3-ubyte"
PIXEL_SIZE = 10
NUM_OF_IMAGES=60000
WIDTH=28*PIXEL_SIZE
HEIGHT=28*PIXEL_SIZE

if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Set up the display window
    window_size = (WIDTH*2, HEIGHT*2)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Neural Network')

    # Fill the window with a white background
    window.fill((200, 200, 200))

    # Update the display
    pygame.display.update()

    images = utils.parse_mnist(5)

    # set_virtual_pixel(0, 0, 0)
    # # set_virtual_pixel(27*PIXEL_SIZE, 27*PIXEL_SIZE, 0)
    # set_virtual_pixel(27, 27, 0)

    for row_idx, row in enumerate(images[4]):
        for col_idx, grayscale in enumerate(row):
            # window.set_at((col_idx, row_idx), (grayscale, grayscale, grayscale))
            utils.set_virtual_pixel(window, col_idx, row_idx, grayscale)
            # img.put(f"#{grayscale:02x}{grayscale:02x}{grayscale:02x}", (col_idx, row_idx))

    
        

    # nn = neunet.NeuralNetwork.init_layered_network([28*28, 256, 128, 10])

    # draw_neural_network(nn)

    pygame.display.update()


    # Main Window Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # # Quit Pygame
    # pygame.quit()
    # sys.exit()
