import numpy as np



class Analyze:

    def __init__(self, data):
        self.data = data
        self.normalize()


    def normalize(self):
        for i in list(range(len(self.data[0]))):
            cols = self.data[:, i]
            print(sorted(cols))


if __name__ == '__main__':
    inpt = np.array([
        [652, 718, 43, 87, 1.95, 52, 55],
        [643, 570, 32, 55, 2.11, 45, 49],
        [49, 739, 48, 78, 1.97, 52, 50],
        [59, 570, 32, 40, 2.13, 41, 46]
        ]
    )

    a = Analyze(inpt)