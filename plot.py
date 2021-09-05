import matplotlib.pyplot as plt

from storage import MongoStorage


class Plot:

    def __init__(self):
        self.storage = self.__set_storage()
        self.data = self.__load_data()

    @staticmethod
    def __set_storage():
        return MongoStorage()

    def __load_data(self):
        return self.storage.load(
            filter_data={'row': {'$lt': 8}},
            collection_name='coronavirus'
        )

    def parse_data(self):
        data_set = {}

        for row in self.data:
            for key, value in row.items():
                if key not in data_set.keys():
                    data_set[key] = list()
                data_set[key].append(value)

        return data_set

    @staticmethod
    def draw_plot(names, values):
        plt.figure(figsize=(7, 7))

        plt.subplot(111)
        plt.bar(names, values)

    @staticmethod
    def save_plot_as_image():
        plt.savefig(fname='page/images/coronavirus.svg', format='svg')

    def start(self):
        data = self.parse_data()
        countries = data['country']
        total_cases = data['total_cases']

        self.draw_plot(
            names=countries,
            values=total_cases
        )
        self.save_plot_as_image()

        print('- Complete Draw And Store Plot')
