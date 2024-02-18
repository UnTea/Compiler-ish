import node


class ReturnNode(node.Node):
    def __init__(self, ctrl, data):
        super().__init__(ctrl, data)

    def ctrl(self):
        return self.in_(0)

    def expr(self):
        return self.in_(1)

    def isCFG(self):
        return True
