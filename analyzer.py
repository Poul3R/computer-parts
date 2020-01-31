#!/usr/bin/env python3

import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    print("Please use MAIN.py script to run.")
    sys.exit()


class Analyzer:
    column_names = ['price', 'core', 'ram', 'disc_type', 'disc_capacity', 'display',
                    'os', 'warranty']

    computers_data = pd.read_csv('computers-specification-media-markt.csv', names=column_names)

    def prepare_data(self):
        self.computers_data.disc_type = self.computers_data.disc_type.replace('SSD', 1)
        self.computers_data.disc_type = self.computers_data.disc_type.replace('HDD', 0)
        self.computers_data.os = self.computers_data.os.replace('Windows', 2)
        self.computers_data.os = self.computers_data.os.replace('macOS', 1)
        self.computers_data.os = self.computers_data.os.replace('Other', 0)

    def get_statistics(self, column, statistic):
        column_selected = self.computers_data[[column]]

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

    def pearson_correlation(self):
        self.prepare_data()

        pearson_corr = self.computers_data.corr(method="pearson")

        sns.heatmap(pearson_corr, ax=None, cmap="coolwarm", linewidths=0.1)
        plt.show()

    def linear_regression(self, specification):
        self.prepare_data()

        reg = linear_model.LinearRegression()

        x_train, x_test, y_train, y_test = train_test_split(self.computers_data[
                                                                ['core', 'ram', 'disc_type', 'disc_capacity', 'display',
                                                                 'os', 'warranty'
                                                                 ]], self.computers_data.price, train_size=0.8)

        reg.fit(x_train, y_train)

        predicted_price = reg.predict([specification])

        # print('--- test ---')
        effectiveness = reg.score(x_test, y_test)

        return predicted_price, effectiveness
