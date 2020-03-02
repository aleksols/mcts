from state_manager import StateManager
from config import NIM_N, NIM_K

class NimManager(StateManager):
    def generate_initial_state(self):
        self.game_state = NIM_N

    def generate_child_states(self, state):
        saps = []
        for i in range(1, min(state, NIM_K) + 1):
            saps.append((i, state - i))
        return saps

    def is_winning_state(self, state):
        return state == 0

    def apply_action(self, action, verbose=False):
        self.game_state -= action
        if verbose:
            player = "1" if self.player else "2"
            print("Player", player, "selects", action, "stones:", "Remaining stones =", self.game_state)
        self.player = not self.player

if __name__ == '__main__':
    NIM = NimManager(0)
    NIM.apply_action(2)
    print("state = 10\nchildren:")
    print(NIM.generate_child_states(10))