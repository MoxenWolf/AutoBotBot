from typing import Tuple

from .action import Action


class ClickAction(Action):
    def __init__(self):
        super().__init__()
        self.coords: Tuple[int, int] = (0, 0)
        self.window = None
