import pygame.image
from constants import *
from classes.Post import Post
from helpers import screen


class ImagePost(Post):
    def __init__(self, user_name, location, description, likes_counter, comments,image):
        super().__init__(user_name, location, description, likes_counter, comments)
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image,(POST_WIDTH,POST_HEIGHT))

    def display(self):
        super().display()
        screen.blit(self.image,(POST_X_POS,POST_Y_POS))