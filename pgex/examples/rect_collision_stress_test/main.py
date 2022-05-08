"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import asyncio

import pygame

from .reddy import Reddy
from .UI import HorizontalSlider

pygame.init()


async def main():
    screen = pygame.display.set_mode((500, 400))
    clock = pygame.time.Clock()

    group = pygame.sprite.Group()

    def spawn_entities(number):
        group.empty()
        for _ in range(number):
            entity = Reddy()
            group.add(entity)

    horizontal_slider = HorizontalSlider(
        pygame.Rect(50, 350, 400, 40), callback=spawn_entities
    )

    font = pygame.font.Font(None, 16)

    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        group.update()
        group.draw(screen)

        horizontal_slider.update(events)
        horizontal_slider.draw(screen)

        fps_text = font.render(f"FPS: {clock.get_fps():.0f}", True, "white")
        fps_rect = fps_text.get_rect()
        entity_count = len(group)
        check_text = font.render(
            f"Collision checks: {entity_count * (entity_count-1):,}", True, "white"
        )
        slider_value = font.render(
            f"Slider value (entities): {horizontal_slider.current_value}", True, "white"
        )
        screen.blits(
            (
                (fps_text, fps_rect),
                (check_text, check_text.get_rect(top=fps_rect.bottom)),
                (
                    slider_value,
                    slider_value.get_rect(
                        top=check_text.get_rect(top=fps_rect.bottom).bottom
                    ),
                ),
            )
        )

        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
