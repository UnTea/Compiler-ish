opcodes_map = {
    "Start": "START",
    "Stop": "STOP",
    "Add": 1,
    "Copy": 2,
    "If": 3,
    "Return": 4,
}

UNIQUE_ID = 1


def generate_unique_id():
    global UNIQUE_ID
    current_id = UNIQUE_ID
    UNIQUE_ID += 1

    return current_id


class BasicBlock:
    UNIQUE_ID = 1

    def __init__(self):
        self.instructions = []
        self.input_edges = []
        self.output_edges = []
        self.UNIQUE_ID = generate_unique_id()

    @staticmethod
    def generate_unique_id():
        current_id = BasicBlock.UNIQUE_ID
        BasicBlock.UNIQUE_ID += 1

        return current_id

    def add_instruction(self, opcode, destination, source0=None, source1=None):
        instruction = Instruction(opcode, destination, source0, source1)
        self.instructions.append(instruction)

    def add_input_edge(self, input_edge):
        self.input_edges.append(input_edge)

    def add_output_edge(self, output_edge):
        self.output_edges.append(output_edge)


class Instruction:
    def __init__(self, opcode, destination=None, source0=None, source1=None):
        self.opcode = opcodes_map[opcode]
        self.destination = destination
        self.source0 = source0
        self.source1 = source1
        self.next_instruction = None

    def set_next_instruction(self, next_instruction):
        self.next_instruction = next_instruction
