import pygame


class HorizontalSlider:
    def __init__(
        self,
        rect: pygame.Rect,
        min_value: int = 10,
        max_value: int = 1000,
        step: int = 10,
        callback: callable = lambda _: None,
    ):
        self.current_value = min_value

        self.rail_rect = rect.inflate(0, -0.8 * rect.height)
        self.button_rect = rect.inflate(-0.95 * rect.width, 0)
        self.button_rect.left = rect.left

        value_range = max_value - min_value
        adjusted_step = value_range / (rect.width - self.button_rect.width)
        value_step = max(step, int(adjusted_step))
        dist_step = (rect.width - self.button_rect.width) / (value_range / value_step)

        self.data = [
            (v, x)
            for v, x in zip(
                range(min_value, max_value, value_step),
                range(self.button_rect.width // 2, rect.width, round(dist_step)),
            )
        ]
        self.data += [(max_value, rect.width)]
        self.callback = callback
        self.callback(self.current_value)
        self.prev_value = self.current_value

        self.move = False

    def update(self, events: list) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    self.move = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.move = False
                if self.prev_value != self.current_value:
                    self.callback(self.current_value)
                self.prev_value = self.current_value
            elif event.type == pygame.MOUSEMOTION and self.move:
                x = self.clamp(event.pos[0])
                for value, pos in self.data:
                    if pos + self.rail_rect.left > x:
                        continue
                    self.current_value = value
                    self.button_rect.centerx = pos + self.rail_rect.left

    def clamp(self, x: int, min_value: int = None, max_value: int = None):
        min_value = min_value or self.rail_rect.left + self.button_rect.width / 2
        max_value = max_value or self.rail_rect.right
        return max(min_value, min(x, max_value))

    def draw(self, display: pygame.Surface) -> None:
        pygame.draw.rect(display, "grey20", self.rail_rect)
        pygame.draw.rect(display, "grey50", self.button_rect)
