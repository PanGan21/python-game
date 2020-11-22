import pygame
from player import Human
from screen import Screen
from game import HardGame
from main import play_game

if __name__ == "__main__":
    pygame.init()

    screen = Screen()
    player = Human(screen.width/2, screen.height-100)
    game = HardGame()

    play_game(screen, player, game)