import random
import digest
import learn


def createNodes(neurons, dimensions, rang):
    return [Node(dimensions, rang) for _ in range(neurons)]


class intelligence:
    def __init__(self, dimensions, neurons, rang, learn_rate):
        self.dimensions = dimensions
        self.nodes = createNodes(neurons, dimensions, rang)
        self.stored = [0.0 for _ in range(neurons)]
        self.matrix = None
        self.inputs = 0
        self.outputs = 0
        self.learnRate = learn_rate
        self.digest()

    def digest(self):
        self.matrix = digest.digest(self)

    def setContext(self, inputNodes, outputNodes):
        # changes where inputs are dropped and where readings are taken.
        if type(inputNodes) == int:
            if inputNodes < len(self.nodes):
                self.inputs = inputNodes
            else:
                print(f"warning 2001: input nodes unable to fit in the intelligence.")
        if type(inputNodes) is list:
            for inn in inputNodes:
                if type(inn) is not int or inn >= len(self.nodes):
                    print(f"warning 2002: input node {inn} unable to fit in the intelligence.")
                    break
            self.inputs = inputNodes
        # now for outputs
        if type(outputNodes) == int:
            if outputNodes < len(self.nodes):
                self.outputs = outputNodes
            else:
                print(f"warning 2003: output nodes unable to fit in the intelligence.")
        if type(outputNodes) is list:
            for inn in outputNodes:
                if inn is not int or inn >= len(self.nodes):
                    print(f"warning 2004: output nodes unable to fit in the intelligence.")
                    break
            self.outputs = outputNodes

    def learn(self, error_rate):
        self.nodes = learn.learn(self, error_rate)
        self.digest()

    def predict(self, inputValues, new):
        if new:
            self.digest()
        if type(self.inputs) is list:
            if len(inputValues) != len(self.inputs):
                raise ValueError("Error 1014: inputs cannot be different size than input values")
            result = self.listPredict(inputValues)
        else:
            result = self.intPredict(inputValues)

        # print(f"matrix: {self.stored}")
        return result

    def listPredict(self, inputValues):
        for i, index in enumerate(self.inputs):
            self.stored[index] = inputValues[i]
        self.defuse(3)
        return self.stored[self.outputs]

    def intPredict(self, inputValues):
        self.stored[self.inputs] = inputValues
        self.defuse(3)
        return self.stored[self.outputs]

    def defuse(self, cnt):
        # do the message thing
        for x in range(cnt):
            output = [[0.0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]
            for i in range(len(self.stored)):
                for j in range(len(self.stored)):
                    output[j][i] = self.stored[i] * self.matrix[j][i]
            # get averages
            i = 0
            for row in output:
                non_zero_values = [value for value in row if value != 0]  # Filter out 0 values
                if len(non_zero_values) != 0:
                    self.stored[i] = sum(non_zero_values) / len(non_zero_values)
                else:
                    self.stored[i] = 0
                i += 1

    def export(self):
        stringy = f"Intelligence\nDimensions: {self.dimensions}\nNode Count: {len(self.nodes)}\nNodes: "
        x = False
        for node in self.nodes:
            if x:
                stringy += f", {node.location}"
            else:
                stringy += f"{node.location}"
            x = True
        stringy += f"\ninputs: {self.inputs}\noutputs: {self.outputs}\nlearning rate: {self.learnRate}"
        return stringy


class Node:
    def __init__(self, dimensions, r):
        self.location = [2 * r * random.random() - r for _ in range(dimensions)]

    def learn(self, vector):
        if len(vector) != len(self.location):
            raise ValueError("Error 1001: Cannot apply a vector of a different dimensionality")
        for component in range(len(vector)):
            self.location[component] += vector[component]


if __name__ == '__main__':
    intel = intelligence(10, 256, 1, 0.001)
    intel.setContext([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0)
    intel.learn(-0.9)
    # print(f"result: {intel.predict([3, 5, 4, 2, 1, 8], True)}")
