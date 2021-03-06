import numpy as np


class Categorizer:

    def __init__(self, data):
        self.data = data

    def normalize(self, data):
        normalized = np.empty(shape=(len(data), len(data[0])))
        normalized.fill(0)
        min_max_dict: dict = {}
        for i in list(range(len(data[0]))):
            cols = data[:, i]
            cols = sorted(cols)
            minim = cols[0]
            maxim = cols[-1]
            min_max_dict[i] = [minim, maxim]
        for j in list(range(len(normalized))):
            for i in list(range(len(normalized[j]))):
                minim = min_max_dict[i][0]
                maxim = min_max_dict[i][1]
                # Minmax
                normal = ((data[j][i] - minim) / (maxim - minim))
                normalized[j][i] = normal
        return normalized

    def calc_euclidian_on_between_segments(self):
        segments_dist: dict = {}
        norm = self.normalize(self.data)
        lst = list(range(len(norm)))
        for i in lst:
            for j in lst[i + 1:]:
                segments_dist[f"{i}, {j}"] = self.calc_euclidian_dist(norm[i], norm[j])
        return segments_dist

    def calc_euclidian_dist(self, arr1, arr2):
        """
        Calculates euclidian dist between 2 arrays
        """
        dist = 0
        for i in list(range(len(arr1))):
            dist += ((arr1[i] - arr2[i]) ** 2)
        return dist

    def segmentize_client(self, client_array):
        """
        Calculates to which segment does the client best fit into, client is a part of the normalization process in this function
        """
        closest: dict = {}
        self.data = list(self.data)
        self.data.append(client_array)
        self.data = np.asarray(self.data)
        self.data = self.normalize(self.data)
        client = self.data[-1]
        self.data = self.data[:-1]
        for i in list(range(len(self.data[0]))):
            col = np.asarray(self.data[:, i])
            closest_value = self.find_nearest(col, client[i])
            closet_value_segment = list(np.where(col == closest_value))[0]
            if len(closet_value_segment) > 1:
                for n in closet_value_segment:
                    self.add_to_dct(n, closest)
            else:
                self.add_to_dct(closet_value_segment[0], closest)
        print(closest)
        return sorted(closest.items(), key=lambda x: x[1], reverse=True)[0][0]

    def add_to_dct(self, value, dct: dict):
        """
        Helper method to aad value to dictionary
        """
        if value in dct.keys():
            dct[value] += 1
        else:
            dct[value] = 1

    def find_nearest(self, array, value):
        """Finds the nearest value in np array to value"""
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    def print(self, lst):
        for i in lst:
            print(list(i))


if __name__ == '__main__':
    # Segments
    inpt = np.array([
        [652, 718, 43, 87, 1.95, 52, 55],
        [643, 570, 32, 55, 2.11, 45, 49],
        [49, 739, 48, 78, 1.97, 52, 50],
        [59, 570, 32, 40, 2.13, 41, 46]
    ]
    )
    a = Categorizer(inpt)

    euclid = a.calc_euclidian_on_between_segments()

    print(f"Euclidian distance between segments is: {euclid}")

    # New value
    ppl = [49, 78, 48, 87, 1.95, 52, 55]

    ans = a.segmentize_client(ppl)
    print(f"Your list is closest to {ans + 1} segment and therefore is in that category")
