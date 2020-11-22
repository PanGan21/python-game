import pygame
from player import Human
from screen import Screen
from game import BossGame
from main import play_game

if __name__ == "__main__":
    pygame.init()

    screen = Screen()
    player = Human(screen.width/2, screen.height-100)
    game = BossGame()

    play_game(screen, player, game)