from game import Game


class Nim(Game):

    def __init__(self, N, K):
        super().__init__()
        self.num_stones = N
        self.k = K

    def apply_move(self, move):
        self.num_stones -= move


    def valid_moves(self, state):
        if state == 1:
            return None  # May be better to return []
        return [i for i in range(1, min(state, self.k) + 1)]

    def generate_children_states(self, state):
        pass

    @property
    def state(self):
        pass


if __name__ == '__main__':
    game = Nim(9, 10)
    print(game.valid_moves(9))
