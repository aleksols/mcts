import math
import random

import numpy as np

from state_manager import StateManager
from tree import Node


class MCTS:
    def __init__(self, state_manager: StateManager, c):
        self.state_manager = state_manager
        self.c = c

    def get_best_action(self, num_simulations, root):
        for _ in range(num_simulations):
            leaf_node = self.tree_search(root)
            z = self.rollout(leaf_node)
            self.backprop(leaf_node, z)
        self.state_manager.set_state(root.state, root.player)
        return self.select_node(root, c=0)

    def select_node(self, node: Node, c) -> Node:  # Tree policy
        if node.player:
            best_child = np.argmax([child.value + c * (math.log(node.N()) / child.N()) ** (1/2) for child in node.children])
        else:
            best_child = np.argmin([child.value - c * (math.log(node.N()) / child.N()) ** (1/2) for child in node.children])

        return node.children[best_child]

    def tree_search(self, root: Node):
        self.state_manager.set_state(root.state, root.player)
        while not self.state_manager.finished:
            if not root.expanded:
                new_node = root.expand(self.state_manager.generate_child_states())
                return new_node
            root = self.select_node(root, self.c)
            self.state_manager.set_state(root.state, root.player)
        return root

    def rollout(self, current_node: Node):
        self.state_manager.set_state(current_node.state, current_node.player)
        while not self.state_manager.finished:
            _, action = random.choice(self.state_manager.generate_child_states())
            self.state_manager.apply_action(action)
        if self.state_manager.player:
            return -1
        return 1

    def backprop(self, leaf_node: Node, z):
        while leaf_node is not None:
            leaf_node.visits += 1
            leaf_node.wins += z
            leaf_node = leaf_node.parent



if __name__ == '__main__':
    from nim_manager import NimManager

    for i in range(100):
        manager = NimManager(True)
        kernel = MCTS(manager)
        game_manager = NimManager(True)
        root = Node(manager.game_state, None, manager.player)

        while root.state != 0:
            root = kernel.get_best_action(500, root)
            root.pretty_print_values()
            game_manager.apply_action(root.edge_action, True)






