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

    try:
        computers_data_media = pd.read_csv('computers-specification-media-markt.csv', names=column_names)
        computers_data_morele = pd.read_csv('computers-specification-morele-net.csv', names=column_names)
        frames = [computers_data_media, computers_data_morele]

        computers_data = pd.concat(frames)

        def prepare_data(self):
            self.computers_data.disc_type = self.computers_data.disc_type.replace('SSD', 1)
            self.computers_data.disc_type = self.computers_data.disc_type.replace('HDD', 0)
            self.computers_data.os = self.computers_data.os.replace('Windows', 2)
            self.computers_data.os = self.computers_data.os.replace('macOS', 1)
            self.computers_data.os = self.computers_data.os.replace('Other', 0)

        def get_statistics(self, column):
            column_selected = self.computers_data[[column]]

            statistics = {
                "Average": round(column_selected.mean(), 2),
                "Dominant": round(column_selected.mode(), 2),
                "Median": round(column_selected.median(), 2)
            }

            return statistics

        def pearson_correlation(self):
            self.prepare_data()

            pearson_corr = self.computers_data.corr(method="pearson")

            sns.heatmap(pearson_corr, ax=None, cmap="coolwarm", linewidths=0.1)
            plt.show()

        def linear_regression(self, specification):
            self.prepare_data()

            reg = linear_model.LinearRegression()

            x_train, x_test, y_train, y_test = train_test_split(self.computers_data[
                                                                    ['core', 'ram', 'disc_type', 'disc_capacity',
                                                                     'display',
                                                                     'os', 'warranty'
                                                                     ]], self.computers_data.price, train_size=0.8)

            reg.fit(x_train, y_train)

            predicted_price = reg.predict([specification])

            effectiveness = reg.score(x_test, y_test)

            return predicted_price, effectiveness
    except:
        print("""
There are no all data files. Scrap data from MediaMarkt,pl and Morene.net first.
        """)
