opcodes = {
    "Start": "Start",
    "Stop": "Stop",
    "Constant": 1,
    "Return": 2,
}

unique_id = 1
graph = []


def create_basic_block(block_id=None):
    global unique_id
    block_id = block_id if block_id is not None else unique_id
    unique_id += 1

    block = {
        "id": block_id,
        "instructions": [],
        "input_edges": [],
        "output_edges": []
    }

    graph.append(block)

    return block


def add_instruction(block, opcode, destination, source0=None, source1=None):
    instruction = {
        "opcode": opcode,
        "destination": destination,
        "source0": source0,
        "source1": source1,
        "next_instruction": None
    }

    block["instructions"].append(instruction)


def add_input_edge(block, input_edge):
    block["input_edges"].append(input_edge)


def add_output_edge(block, output_edge):
    block["output_edges"].append(output_edge)


def create_start_block():
    return create_basic_block(opcodes["Start"])


def create_stop_block():
    return create_basic_block(opcodes["Stop"])


def create_constant_block(value):
    block = create_basic_block()
    add_instruction(block, opcodes["Constant"], "result", value)

    return block


def connect_blocks(source, destination):
    add_output_edge(source, destination)
    add_input_edge(destination, source)
