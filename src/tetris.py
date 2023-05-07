# Author  : Chirath Nissanka
# Project : Tetris
# Date    : 2023
import pygame
import random
from src.constants import *


def get_next_block():
    return random.choice(TETRIS_BLOCKS)


def construct_block(block=TETRIS_I_BLOCK):
    pass


class Block:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        self.running = True

    def draw(self, screen):
        print("hello")

    def draw_border(self):
        pass

    def draw_next_block_container(self):
        pass

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, is_running):
        self._running = is_running


def main(game):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while game.running:
        game.handle_event(pygame.event.get())
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    game = Game()
    main(game)
