import digest
import random
import numpy as np


# returns all vectors that need to be applied to the nodes
def parseInstructions(nodes, matrix, lr, er):
    out = []
    for y, row in enumerate(matrix):
        for x, element in enumerate(row):
            if element != 0:
                difference = np.array(nodes[x]) - np.array(nodes[y])
                value = difference * (lr * er * random.random())
                out.append([x, value])

    return out


def combineVectors(instructions):
    combined = {}

    for instr in instructions:
        first_value = instr[0]
        if first_value not in combined:
            combined[first_value] = np.array(instr[1])  # Initialize with the array
        else:
            combined[first_value] += np.array(instr[1])  # Add the array to the existing sum

    # Convert the dictionary back to a list of lists
    combined_instructions = [[key, value.tolist()] for key, value in combined.items()]

    return combined_instructions


def learn(intel, error_rate):
    nodes = intel.nodes
    for i, node in enumerate(nodes):
        print(f"node: {node.location}")
    matrix = intel.matrix
    lr = intel.learnRate
    locations = []
    for node in nodes:
        locations.append(node.location)
    instructions = parseInstructions(locations, matrix, lr, error_rate)

    # completely unnecessary, but it makes the data easier to analyze by hand.
    instructions = combineVectors(instructions)

    for i, node in enumerate(nodes):
        node.location += np.array(instructions[i][1])
        print(f"node: {node.location}")
    return nodes
