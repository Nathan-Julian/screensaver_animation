# import packages
import pygame
import random
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (int (screen_info.current_w), int (screen_info.current_h))
screen = pygame.display.set_mode(size)
background_color = (120, 255, 172)


#clock
clock = pygame.time.Clock()

#sprite
sprite_image = pygame.image.load("replit.png")
sprite_rect = sprite_image.get_rect()
sprite_image = pygame.transform.scale(sprite_image, (int(0.1*sprite_rect.width), int (0.1*sprite_rect.height)))
sprite_rect = sprite_image.get_rect()
sprite_rect.center = (width // 2, height // 2)

speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)


def main():
	while True:
		clock.tick(60)
		sprite_rect.move_ip(speed)
		screen.fill(background_color)
		screen.blit(sprite_image, sprite_rect)
		pygame.display.flip()

main()