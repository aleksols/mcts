from state_manager import StateManager


class LedgeManager(StateManager):

    def __init__(self, player, B):
        self.B_init = B
        super().__init__(player)

    def generate_initial_state(self):
        self.game_state = self.B_init.copy()

    def generate_child_states(self):
        saps = []
        if self.game_state[0] != 0:
            state = [0] + self.game_state[1:]
            action = (0, None)
            saps.append((state, action))
        for from_index in range(1, len(self.game_state)):
            state = self.game_state.copy()
            to_index = from_index - 1
            while to_index >= 0 and state[from_index] != 0 and state[to_index] == 0:
                action = (from_index, to_index)
                state[to_index] = state[from_index]
                state[from_index] = 0
                saps.append((state, action))
                to_index -= 1
                state = self.game_state.copy()

        return saps

    def is_winning_state(self, state):
        return 2 not in state

    def apply_action(self, action, verbose=False):
        # action is a tuple (from_index, to_index). If to_index is None the piece was removed from the board
        from_index = action[0]
        to_index = action[1]
        coin = self.game_state[from_index]

        if verbose and self.game_state == self.B_init:
            print(f"Start Board: {self.B_init}. The board is zero indexed")

        self.game_state[from_index] = 0
        if to_index is not None:
            self.game_state[to_index] = coin

        if verbose:
            player = "1" if self.player else "2"
            coin_type = "copper" if coin == 1 else "gold"
            if action[1] is not None:
                print(f"Player {player} moves {coin_type} from cell {from_index} to {to_index}: {self.game_state}")
            else:
                print(f"Player {player} removes {coin_type}: {self.game_state}")
                if self.finished:
                    print(f"Player {player} wins!")

        self.player = not self.player

    def set_state(self, game_state, player):
        self.game_state = game_state.copy()
        self.player = player

    @property
    def finished(self):
        return 2 not in self.game_state


if __name__ == '__main__':
    man = LedgeManager(True, [1, 0, 0, 0, 1, 2, 1])
    for state, action in man.generate_child_states():
        print(state, action)

    man.apply_action((0, None), verbose=True)
    man.apply_action((4, 0), verbose=True)
    man.apply_action((0, None), verbose=True)
    man.apply_action((5, 0), verbose=True)
    man.apply_action((0, None), verbose=True)