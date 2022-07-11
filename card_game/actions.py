import sys

import pygame

from classes.button import Button
from phases import Phases


def _brawl_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        screen.draw()
    return ret_enum


def _confirm_map_menu_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        screen.draw()
    return ret_enum


def _macro_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        screen.draw()
    return ret_enum


def _main_menu_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        screen.draw()
    return ret_enum


def _map_choice_logic(**kwargs):
    player = kwargs["player"]
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

            if event.key == pygame.K_LEFT:
                player.board.move_selection("left")
            if event.key == pygame.K_RIGHT:
                player.board.move_selection("right")
            if event.key == pygame.K_UP:
                player.board.move_selection("up")
            if event.key == pygame.K_DOWN:
                player.board.move_selection("down")


            if event.key == pygame.K_RETURN:
                #ret_enum = Phases.CONFIRM_MAP_MENU

                ret_enum = Phases.MACRO

        screen.draw()
    return ret_enum


def _menu_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        screen.draw()
    return ret_enum


def _shop_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        screen.draw()
    return ret_enum


def _title_logic(**kwargs):
    screen = kwargs["screen"]
    ret_enum = None

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_RETURN:
                ret_enum = Phases.MAP_CHOICE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen.title.start_button.check_for_input(screen.title.check_mouse()):
                ret_enum = Phases.MAP_CHOICE
            if screen.title.quit_button.check_for_input(screen.title.check_mouse()):
                sys.exit()
        screen.draw()
    return ret_enum