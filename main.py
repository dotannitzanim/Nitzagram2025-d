import pygame

import buttons
from classes.Comment import Comment
from classes.ImagePost import ImagePost
import helpers
from classes.TextPost import TextPost
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    p1 = ImagePost("dotan","madrid","yokokdokodkodkd",0,[],"Images/ronaldo.jpg")
    p2 = TextPost("roni","Israel","nonononono",1,[Comment("kmdkd"),Comment("jnjndjnd")],"Images/noa_kirel.jpg")
    posts = [p1,p2]
    index = 0
    running = True
    while running:
        curr = posts[index]
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                print(buttons.like_button.get_rect())
                if buttons.like_button.get_rect().collidepoint(pos):
                    print("buttons.like_button.get_rect")
                    curr.likes_counter += 1
                if buttons.comment_button.get_rect().collidepoint(pos):
                    helpers.draw_comment_text_box()
                    print("buttons.comment_button.get_rect()")
                    t = helpers.read_comment_from_user()
                    curr.add_comment(t)
                if buttons.click_post_button.get_rect().collidepoint(pos):
                    index = (index + 1) % len(posts)
                    print("buttons.click_post_button.get_rect().collidepoint")
        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        curr.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
