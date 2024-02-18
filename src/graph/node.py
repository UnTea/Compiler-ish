class Node:
    UNIQUE_ID = 1

    def __init__(self, *inputs):
        self._nid = Node.UNIQUE_ID
        Node.UNIQUE_ID += 1

        self._inputs = list(inputs)
        self._outputs = []

        for n in self._inputs:
            if n is not None:
                n._outputs.append(self)

    def in_(self, i):
        return self._inputs[i]

    def n_ins(self):
        return len(self._inputs)

    def n_outs(self):
        return len(self._outputs)

    def is_unused(self):
        return self.n_outs() == 0

    def is_cfg(self):
        return False

    @staticmethod
    def reset():
        Node.UNIQUE_ID = 1
