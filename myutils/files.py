import os

def getInputs(path, strip=False):
    inputs = []
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path) as file:
        for line in file:
            if strip:
                inputs.append(line.strip())
            else:
                inputs.append(line)
    return inputs

def getNumInputs(path):
    inputs = []
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path) as file:
        for line in file:
            inputs.append(int(line))
    return inputs