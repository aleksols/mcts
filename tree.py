class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = {}


class Node:
    def __init__(self, state, edge_action, player1):
        self.value = 0
        self.player1 = player1
        self.state = state
        self.children = []
        self.parent = None
        self.edge_action = edge_action  # The action applied to get to this node

    def add_children(self, child_saps):
        for action, state in child_saps:
            node = Node(state, action, not self.player1)
            if node in self.children:
                continue
            node.parent = self
            self.children.append(node)

    def has_children(self):
        return len(self.children) > 0

    def __eq__(self, other):
        return self.state == other.state and \
               self.edge_action == other.edge_action and \
               self.player1 == self.player1
