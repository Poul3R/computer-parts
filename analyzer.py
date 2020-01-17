import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model



column_names = ['Cena', 'Ilość rdzeni', 'RAM', 'Rodzaj dysku', 'Pojemność dysku', 'Przekatna ekranu',
                'System operacyjny', 'Gwarancja']

computers_data = pd.read_csv('computers-specification-media-markt.csv', names=column_names)


# print(computers_data[['Cena']])


def get_statistics(column, statistic):
    column_selected = computers_data[[column]]

    if statistic == 'average':
        return column_selected.mean()

    elif statistic == 'standard-deviation':
        return None

    elif statistic == 'mode':  # dominanta
        return column_selected.mode()

    elif statistic == 'median':  # mediana
        return column_selected.median()

    else:
        average = column_selected.mean()
        standard_deviation = None
        mode = column_selected.mode()
        median = column_selected.median()
        return {
            'average': average,
            'standard-deviation': standard_deviation,
            'mode': mode,
            'median': median
        }


def pearson_correlation():
    pearsoncorr = computers_data.corr(method="pearson")

    plt.matshow(pearsoncorr)
    plt.title('Ceny laptopa wzgędem jego parametrów')
    plt.legend((1, 2, 3, 4, 5), ('Cena', 'Ilość rdzeni', 'RAM', 'Rodzaj dysku', 'Pojemność dysku', 'Przekatna ekranu',
                                 'System operacyjny', 'Gwarancja'))
    plt.show()


# print(get_statistics('Ilość rdzeni', 'average'))

# pearson_correlation()

def linear_regression(specification):
    reg = linear_model.LinearRegression()
    reg.fit(computers_data[['Ilość rdzeni', 'RAM', 'Pojemność dysku', 'Przekatna ekranu',
                            'Gwarancja']], computers_data.Cena)

    predicted_price = reg.predict([specification])
    return predicted_price


if __name__ == "__main__":
    print("This script is part of bigger program. Please use MAIN.py script to run")
