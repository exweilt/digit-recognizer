import pygame
from typing import *
import numpy as np

import neunet
from constants import *

# Returns list of all images. Each image is stored as a 2 dimensional list:
# 1st dim -> Pixel row position
# 2nd dim -> Pixel column position
def parse_mnist(load_num) -> list[ list[list[int]] ]:
    images = []
    with open(IMAGES_FILE, "rb") as file:
        file.read(16) # Skip magic

        assert load_num <= 60000
        for image_idx in range(load_num):
            image = []
            for row_idx in range(28):
                row = []
                for col_idx in range(28):
                    row.append(int.from_bytes(file.read(1), "big"))
                image.append(row)
            images.append(image)

    return images

# Puts given pixel of digit's picture
def set_virtual_pixel(wnd: pygame.Surface, x, y, value):
    pygame.draw.rect(wnd, (value, value, value), (x*PIXEL_SIZE, y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    # pygame.draw.rect(window, (value, value, value), pygame.Rect(x, y, x+PIXEL_SIZE, y+PIXEL_SIZE))
    # img.put(f"#{grayscale:02x}{grayscale:02x}{grayscale:02x}", (col_idx, row_idx))
    # canvas.create_rectangle(x*PIXEL_SIZE, y*PIXEL_SIZE, x*PIXEL_SIZE + PIXEL_SIZE, y*PIXEL_SIZE + PIXEL_SIZE, fill=f"#{grayscale:02x}{grayscale:02x}{grayscale:02x}", width=0)

def draw_image(img: list[list[int]], window):
    for row_idx, row in enumerate(img):
        for col_idx, grayscale in enumerate(row):
            # window.set_at((col_idx, row_idx), (grayscale, grayscale, grayscale))
            set_virtual_pixel(window, col_idx, row_idx, grayscale)
            # img.put(f"#{grayscale:02x}{grayscale:02x}{grayscale:02x}", (col_idx, row_idx))

def draw_neural_network(network: neunet.NeuralNetwork):
    pass

def image_to_input_array(img: list[list[int]]) -> np.ndarray:
    return np.array( [num for row in img for num in row] )