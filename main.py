import pygame
import sys
import neunet

import utils
import numpy as np

# Constants
IMAGES_FILE = "train-images.idx3-ubyte"
PIXEL_SIZE = 10
NUM_OF_IMAGES=60000
WIDTH=28*PIXEL_SIZE
HEIGHT=28*PIXEL_SIZE

if __name__ == "__main__":
    pygame.init()

    window_size = (WIDTH, HEIGHT)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Neural Network')

    window.fill((200, 200, 200))

    pygame.display.update()

    images = utils.parse_mnist(5)

    # set_virtual_pixel(0, 0, 0)
    # # set_virtual_pixel(27*PIXEL_SIZE, 27*PIXEL_SIZE, 0)
    # set_virtual_pixel(27, 27, 0)

    # # Draw mnist digit
    # for row_idx, row in enumerate(images[4]):
    #     for col_idx, grayscale in enumerate(row):
    #         # window.set_at((col_idx, row_idx), (grayscale, grayscale, grayscale))
    #         utils.set_virtual_pixel(window, col_idx, row_idx, grayscale)
    #         # img.put(f"#{grayscale:02x}{grayscale:02x}{grayscale:02x}", (col_idx, row_idx))

    
        
    # nn = neunet.NeuralNetwork.init_layered_network([28*28, 256, 128, 10])
    # nn = neunet.NeuralNetwork.init_layered_network([3, 6, 2])

    # utils.draw_neural_network(nn)

    # nn2 = neunet.NeuralNetwork([
    #     neunet.DenseLayer(1, 1),
    #     neunet.DenseLayer(1, 1),
    # ])
    # nn2.predict(np.array([2]))

    nn = neunet.NeuralNetwork([
        neunet.DenseLayer(20, 28*28),
        neunet.DenseLayer(10, 20)
    ])

    pygame.display.update()

    drawn_image = [[0 for j in range(28)] for i in range(28)]
    # drawn_image[1][20] = 255

    # Main Window Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    drawn_image = [[0 for j in range(28)] for i in range(28)]
                if event.key == pygame.K_p:
                    print("Making prediction...")
                    y_hat = nn.predict(utils.image_to_input_array(drawn_image))
                    print(f"Predicted: {y_hat}")
            if event.type == pygame.QUIT:
                running = False
            

        if pygame.mouse.get_pressed()[0]:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            drawn_image[mouse_y // PIXEL_SIZE][mouse_x // PIXEL_SIZE] = 255

        
        
        utils.draw_image(drawn_image, window)
        pygame.display.update()

    # # Quit Pygame
    # pygame.quit()
    # sys.exit()
