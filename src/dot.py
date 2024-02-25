import ast

DOT_STYLE = ('\tnode [fontname = "Fira Code" fontsize = 16\n'
             '\tstyle = filled fillcolor = "#E5FDCD" penwidth = 2]\n'
             '\tedge [fontname = "Fira Code" fontsize = 12]')


def to_dot(graph, labels, edge_labels):
    dot = [f'digraph G {{\n{DOT_STYLE}']

    for n in graph:
        dot.append(f'\t{n} [label="{labels[n]}" shape=box]')

    for a in graph:
        for b in graph[a]:
            dot.append(f'\t{a} -> {b} [label="{edge_labels[(a, b)]}"]')

    dot.append('}')

    return '\n'.join(dot)


def ast_to_dot(tree):
    graph = {0: []}
    labels = {0: type(tree).__name__}
    edge_labels = {}

    def walk_fields(node_id, tree):
        args = []

        for field in tree._fields:
            match getattr(tree, field):
                case ast.AST() | list() as child if child != []:
                    walk(node_id, child, field)

                case _ as value:
                    args.append(f'{field}: {repr(value)}')

        return '\\n'.join(arg for arg in args)

    def walk(parent_id, tree, field):
        node_id = len(graph)
        graph[parent_id].append(node_id)
        graph[node_id] = []
        edge_labels[(parent_id, node_id)] = field

        match tree:
            case ast.AST():
                args = walk_fields(node_id, tree)
                labels[node_id] = f'{type(tree).__name__}\\n{args}'

            case list():
                labels[node_id] = 'list'

                for idx, elem in enumerate(tree):
                    walk(node_id, elem, idx)

    walk_fields(0, tree)

    return to_dot(graph, labels, edge_labels)


def node_to_dot(graph):
    dot = [f'digraph G {{\n{DOT_STYLE}']

    for node in graph:
        dot.append(f'\t{node['id']} [label = "{node['id']}" shape = box]')

    for a in graph:
        for b in a['output_edges']:
            dot.append(f'\t{a['id']} -> {b['id']}')

    dot.append('}')

    return '\n'.join(dot)
