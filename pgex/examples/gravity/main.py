import pygame
from .ball import Ball
import time
import asyncio


async def main():
    screen_width, screen_height = 600, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Gravity!")
    clock = pygame.time.Clock()

    ball_list = []
    last = time.perf_counter()
    while True:
        # cap fps
        clock.tick(60)

        # calculate delta time
        dt = (time.perf_counter() - last) * 60
        # cap delta time in case the window is moving
        dt = min(dt, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # create a Ball if a mouse button is clicked
                ball_list.append(
                    Ball(
                        pos=pygame.Vector2(event.pos),
                        gravity=0.1,
                        radius=20,
                        color="red",
                    )
                )

        screen.fill("black")

        # update all balls
        for ball in ball_list:
            # delete the ball if it's not on the screen anymore
            if ball.pos.y >= screen_height:
                ball_list.remove(ball)

            ball.update(screen, dt)

        pygame.display.flip()

        await asyncio.sleep(0)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
