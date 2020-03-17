class StateManager:

    def __init__(self, player):
        self.game_state = None
        self.generate_initial_state()
        self.player = player

    def generate_initial_state(self):
        raise NotImplementedError

    def generate_child_states(self):
        raise NotImplementedError

    def is_winning_state(self, state):
        raise NotImplementedError

    def apply_action(self, action):
        raise NotImplementedError

    def set_state(self, game_state, player):
        self.game_state = game_state
        self.player = player

    @property
    def finished(self):
        raise NotImplementedError
