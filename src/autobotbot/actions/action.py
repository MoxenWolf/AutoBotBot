from abc import abstractmethod


class Action:
    def __init__(self):
        self.condition = None
        self.attempt_limit: int = 0
        self.time_limit: int = 0
        self.start_callback = None
        self.finished_callback = None
        self.action_id: int = 0

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def check_condition(self):
        pass
