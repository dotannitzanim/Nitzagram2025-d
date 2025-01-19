import pygame

from classes.Post import Post
from helpers import *
from constants import *


class TextPost(Post):
    def __init__(self, user_name, location, description, likes_counter, comments,text,text_color=(0,0,0),background_color=(0,0,255)):
        super().__init__(user_name, location, description, likes_counter, comments)
        self.background_color = background_color
        self.text_color = text_color
        self.text_arr = from_text_to_array(text)

    def display(self):
        super().display()
        pygame.draw.rect(screen,self.background_color,pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT))
        n = len(self.text_arr)
        for i in range(n):
            font = pygame.font.SysFont('chalkduster.ttf', (TEXT_POST_FONT_SIZE))
            text = font.render(self.text_arr[i], True, self.text_color)
            pos = center_text(n,text,i)
            screen.blit(text, pos)
