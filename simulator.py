import random

from tqdm import tqdm

from ledge_manager import LedgeManager
from nim_manager import NimManager
from mcts_kernel import MCTS
from tree import Node

from config import *

class Simulator:

    def __init__(self, c, G, P, M, N, K, B, game):
        self.c = c
        self.G = G
        self.P = P
        self.M = M
        self.N = N
        self.K = K
        self.B = B
        self.game_type = game


    def player_one_starts(self):
        if self.P == 3:
            return bool(random.randint(0, 1))
        return self.P == 1

    def play(self, verbose=False):
        player_one_wins = 0
        for game in tqdm(range(1, self.G + 1)):
            player = self.player_one_starts()
            if self.game_type == "nim":
                sim_manager = NimManager(player, self.N, self.K)
            else:
                sim_manager = LedgeManager(player, self.B)
            kernel = MCTS(sim_manager, self.c)
            root = Node(sim_manager.game_state, None, sim_manager.player)

            while not sim_manager.is_winning_state(root.state):
                sim_manager.set_state(root.state, root.player)
                root = kernel.get_best_action(self.M, root)
                sim_manager.apply_action(root.edge_action, verbose=verbose)
            if not root.player:
                player_one_wins += 1
        print("Player one wins", player_one_wins, "of", game)


if __name__ == '__main__':
    import config
    sim = Simulator(
        c=1,
        G=5000,
        P=1,
        M=500,
        N=10,
        K=3,
        B=0,
        game="nim"
    )
    sim.play(verbose=False)
