import pgzero
import pgzrun
import random

from pgzero.actor import Actor
__all__ = ["pgzrun", "pgzero"]

clouds = [Actor('cloud1', (200, 200)),
          Actor('cloud2', (400, 300)),
          Actor('cloud3', (600, 200)),
          Actor('cloud1', (800, 300))]

obstacles = [Actor('cactus', (random.randint(900, 1000), 495)),
             Actor('cactus', (random.randint(1200, 1500), 495)),
             Actor('cactus', (random.randint(1500, 2000), 495))]

player = Actor('p3_stand', (100, 484))

# 0 - game not started
# 1 - game just stared
# 2 - finished
game = 0
# frame that is currently running
frame = 0
# player movement speed and direction
jump = 0
# 0 - jump is available
# 1 - jump is forbidden
jump_blocked = 0
cloud_speed = 2
game_time = 0
# cactus movement speed
game_speed = 8
# 0 - game running
# 1 - game blocked
jump_unblocked = 0


def draw():
    global game
    screen.clear()
    screen.fill('#cff4f7')
    for i in range((screen.width // 70) + 1):
        screen.blit('grass', (i * 70, screen.height - 70))

    for cloud in clouds:
        cloud.draw()

    for obstacle in obstacles:
        obstacle.draw()

    screen.draw.text(
        align_text_time(game_time),
        midright=(screen.width - 50, 50),
        fontname="roboto_mono_bold",
        color="orange",
        fontsize=45
    )

    player.draw()

    if game == 0:
        screen.draw.text(
            "Wcisnij spacje",
            center=(screen.width / 2, screen.height / 2),
            color="orange",
            fontsize=60
        )

    if game == 2:
        screen.draw.text(
            "Koniec gry",
            center=(screen.width / 2, screen.height / 2),
            color=red,
            fontsize=60
        )
        screen.draw.text(
            "Wcisnij spacje aby zagrac jeszcze raz",
            center=(screen.width / 2, screen.height - 200),
            color=red,
            fontsize=30
        )


def align_text_time(time):
    text = "0" * (5 - len(str(time)))
    text += str(time)
    return text


pgzrun.go()

