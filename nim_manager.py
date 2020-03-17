from state_manager import StateManager

class NimManager(StateManager):

    def __init__(self, player, N, K):
        self.N = N
        super().__init__(player)
        self.K = K

    def generate_initial_state(self):
        self.game_state = self.N

    def generate_child_states(self):
        saps = []
        for i in range(1, min(self.game_state, self.K) + 1):
            saps.append((self.game_state - i, i))
        return saps

    def is_winning_state(self, state):
        return state == 0

    def apply_action(self, action, verbose=False):
        self.game_state -= action
        if verbose:
            before_action = self.game_state + action
            if before_action == self.N:
                print("Start Pile:", before_action, "stones")
            player = "1" if self.player else "2"
            print("Player", player, "selects", action, "stones:", "Remaining stones =", self.game_state)
            if self.finished:
                print("Player", player, "wins!\n")
        self.player = not self.player

    @property
    def finished(self):
        return self.game_state == 0
