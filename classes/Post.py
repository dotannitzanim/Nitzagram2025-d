import pygame

from constants import *
from classes.Comment import Comment
from helpers import screen
from helpers import text_display

# from classes import Comment

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,user_name,location,description,likes_counter,comments): #TODO: add parameters
        #TODO: write me!
        self.comments_display_index = 0
        self.comments = comments
        self.likes_counter = likes_counter
        self.description = description
        self.location = location
        self.user_name = user_name

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self,text):
        self.comments.append(Comment(text))

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_description()
        self.display_likes()
        self.display_location()
        self.display_user_name()
        self.display_comments()

    def display_likes(self):
        text_display(str(self.likes_counter),UI_FONT_SIZE,(LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS))
    def display_location(self):
        text_display(self.location,UI_FONT_SIZE,(LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS))

    def display_description(self):
        text_display(self.description,UI_FONT_SIZE,(DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS))

    def display_user_name(self):
        text_display(self.user_name,UI_FONT_SIZE,(USER_NAME_X_POS,USER_NAME_Y_POS))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



