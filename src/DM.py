import numpy as np



class Analyze:

    def __init__(self, data):
        self.data = data
        self.normalize()


    def normalize(self):
        normalized = np.empty(shape=(len(self.data), len(self.data[0])))
        normalized.fill(0)
        min_max_dict: dict = {}
        for i in list(range(len(self.data[0]))):
            cols = self.data[:, i]
            cols = sorted(cols)
            minim = cols[0]
            maxim = cols[-1]
            min_max_dict[i] = [minim, maxim]
        for j in list(range(len(normalized))):
            for i in list(range(len(normalized[j]))):
                minim = min_max_dict[i][0]
                maxim = min_max_dict[i][1]
                normal = ((self.data[j][i] - minim) / (maxim - minim))

                normalized[j][i] = normal

        print(normalized)




if __name__ == '__main__':
    inpt = np.array([
        [652, 718, 43, 87, 1.95, 52, 55],
        [643, 570, 32, 55, 2.11, 45, 49],
        [49, 739, 48, 78, 1.97, 52, 50],
        [59, 570, 32, 40, 2.13, 41, 46]
        ]
    )

    a = Analyze(inpt)