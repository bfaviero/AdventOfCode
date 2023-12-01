# Parse nodes
with open('adv21_part2.txt') as f:
    lines = [l.strip() for l in f.readlines()]
from math import floor, log10, inf
class Node:
    def __init__(self, line):
        name, expr = line.split(": ")
        self.name = name
        self.value = None
        self.expr = None

        if " " not in expr:
            self.value = eval(expr)
        else:
            self.expr = expr
            (varL, op, varR) = expr.split(" ")
            self.varL = varL
            self.op = op
            self.varR = varR

    def __repr__(self):
        return "{}: {}".format(self.name, self.value or self.expr)
    

# Get list of nodes
nodes = [Node(line) for line in lines]
node_map = {node.name: node for node in nodes}

# Get start node
start_node = node_map['root']

# evaluate the expressions for a given value VAL of humn
def get_value(node, val):
    if node.name == "humn":
        return val
    if node.value is not None:
        return node.value
    else:
        line = "{} {} {}".format(
            get_value(node_map[node.varL], val), 
            node.op, 
            get_value(node_map[node.varR], val)
        )
        return eval(line)

# Binary search algorithm
def binary_search(a, b):
    midpoint = a + ((b - a) / 2)
    val = get_value(start_node, midpoint)
    if val == 1 or (b - a == 1):
        return int(midpoint)
    return binary_search(midpoint, b) if val > 1 else binary_search(a, midpoint)
    
def findHumn():
    humn = 1
    while True:
        val = get_value(start_node, humn)
        if val > 1: # not there yet
            old_humn = humn
            humn *= 10
        else: # overshoot, now we know the bounds
            return binary_search(old_humn, humn)
print(findHumn())