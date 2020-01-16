from typing import List

from . action import Action


class ConcurrentBin:
    def __init__(self):
        self.actions: List[Action]
        self.ordinal_marker: int = 0

    def completed(self):
        pass

    def execute(self):
        pass
