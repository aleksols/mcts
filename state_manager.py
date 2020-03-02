class StateManager:

    def __init__(self, player):
        self.game_state = self.generate_initial_state()
        self.player = player

    def generate_initial_state(self):
        raise NotImplementedError

    def generate_child_states(self, state):
        raise NotImplementedError

    def is_winning_state(self, state):
        raise NotImplementedError

    def apply_action(self, action):
        raise NotImplementedError
