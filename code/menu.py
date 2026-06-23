#!/usr/bin/python
# -*- coding: utf-8 -*-
from idlelib.configdialog import font_sample_text

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font_title = pygame.font.Font('./asset/lucida.ttf', 50)
        self.font_menu = pygame.font.Font('./asset/lucida.ttf', 20)

    def run(self, ):
        pygame.mixer_music.load('./asset/fase1.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(font=self.font_title, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(font=self.font_title, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(font=self.font_menu, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame

    def menu_text(self, font: pygame.font.Font, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
