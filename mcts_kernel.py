from tree import Node
from state_manager import StateManager

class MCTS:
    def __init__(self, state_manager: StateManager):
        self.state_manager = state_manager
        self.tree = Node(self.state_manager.game_state, self.state_manager.player)

    def tree_search(self):
        pass

    def expand_nodes(self, current_node: Node):
        saps = self.state_manager.generate_child_states(current_node.state)
        current_node.add_children(saps)

    def rollout(self, current_node: Node):
        pass

    def backprop(self, end_node: Node):
        pass
