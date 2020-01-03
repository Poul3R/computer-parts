import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

column_names = ['Cena', 'Ilość rdzeni', 'RAM', 'Rodzaj dysku', 'Pojemność dysku', 'Przekatna ekranu', 'Czas pracy',
                'System operacyjny', 'Gwarancja']

computers_data = pd.read_csv('computers-specification.csv', names=column_names)


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

    elif statistic == 'kwartyle':
        return None

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
    plt.show()
    # print(pearsoncorr)


# print(get_statistics('Ilość rdzeni', 'average'))

pearson_correlation()
