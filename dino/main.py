import pgzrun
import random

from pgzero.actor import Actor

clouds = [Actor('cloud1', (200, 200)),
          Actor('cloud2', (400, 300)),
          Actor('cloud3', (600, 200)),
          Actor('cloud1', (800, 300))]

obstacles = [Actor('cactus', (random.randint(900, 1000), 495)),
             Actor('cactus', (random.randint(1200, 1500), 495)),
             Actor('cactus', (random.randint(1500, 2000), 495))]


def draw():
    for cloud in clouds:
        cloud.draw()


pgzrun.go()

