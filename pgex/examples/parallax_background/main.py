import asyncio
import os
import time

import pygame

from . import globals


def load_image(file: str) -> pygame.Surface:
    return pygame.image.load(
        os.path.join(os.path.dirname(__file__), "assets", file)
    ).convert_alpha()


async def main():
    globals.screen = pygame.display.set_mode((800, 600))
    globals.clock = pygame.time.Clock()
    globals.running = True

    # Load background assets
    globals.inner_cave_bg = load_image("inner_cave.png")
    globals.outer_cave_bg = load_image("outer_cave.png")
    globals.plains_bg = load_image("plains.png")
    globals.mountains_bg = load_image("mountains.png")
    globals.sky_bg = load_image("sky.png")

    while globals.running:
        loop()
        await asyncio.sleep(0)


def loop():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # As if we're moving 500 pixels per second to the right.
    # Relative to the camera, the backgrounds should move left --
    # thus we need to add the minus sign.
    bg_scroll = -500 * time.perf_counter()

    # Draw the backgrounds in order from the furthest to the nearest.
    for background, depth in [
        (globals.sky_bg, 50),
        (globals.mountains_bg, 20),
        (globals.plains_bg, 10),
        (globals.outer_cave_bg, 5),
        (globals.inner_cave_bg, 1),
    ]:
        draw_bg(background, bg_scroll, depth)

    pygame.display.flip()
    globals.clock.tick(60)

    pygame.display.set_caption(f"FPS: {globals.clock.get_fps():.2f}")


def draw_bg(background: pygame.Surface, scroll: float, depth: float):
    # If the background is placed far away -- by the rules of perspective,
    # the change of position in XY would be smaller by 1/Z.
    x = scroll / depth

    # X should loop back when it's out of range of the background's size.
    x %= background.get_width()

    # We want to be as efficient with our calls as possible.
    # If `x` is not out of the window, we can draw the main piece of the background.
    if x <= globals.screen.get_width():
        globals.screen.blit(background, (x, 0))

    # We need the background to loop; it happens that the back part gets left out.
    # Unless the main piece had covered it (x == 0), we'll draw it behind the main piece.
    if x != 0:
        globals.screen.blit(background, (x - background.get_width(), 0))


def run():
    # For WASM compatibility.
    asyncio.run(main())


if __name__ == "__main__":
    run()
