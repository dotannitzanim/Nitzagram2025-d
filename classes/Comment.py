import pygame
from constants import *
from helpers import *
class Comment:
    def __init__(self,text):
        self.text = text

    def display(self,index):
        text_display(self.text,COMMENT_TEXT_SIZE,(FIRST_COMMENT_X_POS,FIRST_COMMENT_Y_POS+ COMMENT_TEXT_SIZE*index + 1))