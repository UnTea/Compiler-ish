import node


class StartNode(node.Node):
    def __init__(self):
        super().__init__()

    def isCFG(self):
        return True
