class Game:
    def __init__(self):
        pass

    def generate_children_states(self, state):
        raise NotImplementedError

    @property
    def state(self):
        raise NotImplementedError

    @property
    def valid_moves(self, state):
        raise NotImplementedError
