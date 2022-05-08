import asyncio
import os
import time

import pygame

from . import common


def load_image(file: str) -> pygame.Surface:
    return pygame.image.load(
        os.path.join(os.path.dirname(__file__), "assets", file)
    ).convert_alpha()


async def main():
    common.screen = pygame.display.set_mode((800, 600))
    common.clock = pygame.time.Clock()
    common.running = True

    # Load background assets
    common.INNER_CAVE_BG = load_image("inner_cave.png")
    common.OUTER_CAVE_BG = load_image("outer_cave.png")
    common.PLAINS_BG = load_image("plains.png")
    common.MOUNTAINS_BG = load_image("mountains.png")
    common.SKY_BG = load_image("sky.png")

    while common.running:
        loop()
        await asyncio.sleep(0)


def loop():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            common.running = False

    # As if we're moving 500 pixels per second to the right.
    # Relative to the camera, the backgrounds should move left --
    # thus we need to add the minus sign.
    bg_scroll = -500 * time.perf_counter()

    # Draw the backgrounds in order from the furthest to the nearest.
    for background, depth in [
        (common.SKY_BG, 50),
        (common.MOUNTAINS_BG, 20),
        (common.PLAINS_BG, 10),
        (common.OUTER_CAVE_BG, 5),
        (common.INNER_CAVE_BG, 1),
    ]:
        draw_bg(background, bg_scroll, depth)

    pygame.display.flip()
    common.clock.tick(60)

    pygame.display.set_caption(f"FPS: {common.clock.get_fps():.2f}")


def draw_bg(background: pygame.Surface, scroll: float, depth: float):
    # If the background is placed far away -- by the rules of perspective,
    # the change of position in XY would be smaller by 1/Z.
    x = scroll / depth

    # X should loop back when it's out of range of the background's size.
    x %= background.get_width()

    # We want to be as efficient with our calls as possible.
    # If `x` is not out of the window, we can draw the main piece of the background.
    if x <= common.screen.get_width():
        common.screen.blit(background, (x, 0))

    # We need the background to loop; it happens that the back part gets left out.
    # Unless the main piece had covered it (x == 0), we'll draw it behind the main piece.
    if x != 0:
        common.screen.blit(background, (x - background.get_width(), 0))


def run():
    # For WASM compatibility.
    asyncio.run(main())


if __name__ == "__main__":
    run()
