import itertools
import pathlib
import typing as t

import PIL.Image
import pygame


class GIFPlayer:
    def __init__(
        self,
        path: str | pathlib.Path,
        fps: int = 30,
        pos: t.Sequence[int] | pygame.Vector2 = (0, 0),
        size: t.Sequence[int] | None = None,
        exclude: t.Sequence[int] | None = None,
    ):
        """Initializes an instance of GIFPlayer

        :param path: path to the GIF
        :param fps: framerate for playing the GIF
        :param pos: position on the surface where the GIF will be displayed
        :param size: size of the GIF, if None (the default) is used, the original size of the GIF will be used
        :param exclude: used for excluding specific frames
        """

        frames = []
        with PIL.Image.open(path) as gif:
            for frame in range(getattr(gif, "n_frames", 1)):
                if exclude is not None and frame in exclude:
                    continue
                gif.seek(frame)
                surface = pygame.image.frombuffer(
                    gif.tobytes(), gif.size, gif.mode
                )  # NOQA
                if size is not None:
                    surface = pygame.transform.scale(surface, size)
                frames.append(surface)

        self.rect = frames[0].get_rect(topleft=pos)
        self.frames = itertools.cycle(frames)
        self.current_frame = frames[0]

        self.last_time = pygame.time.get_ticks()
        self.interval = int((1 / fps) * 1000)

    def play(self, display: pygame.Surface) -> None:
        """Plays the GIF indefinitely.

        :param display: Surface where to blit the GIF
        :return: None
        """

        current_time = pygame.time.get_ticks()

        if current_time - self.last_time >= self.interval:
            self.current_frame = next(self.frames)
            self.last_time = current_time

        display.blit(self.current_frame, self.rect)
