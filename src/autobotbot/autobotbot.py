from typing import Dict

from . action_engine import ActionEngine


class AutoBotBot:
    def __init__(self, config: Dict[str, str] = None):
        self.config = config
        self.actions = ActionEngine()

    def engage(self):
        pass
