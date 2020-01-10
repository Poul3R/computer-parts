import matplotlib.pyplot as plt
import numpy as py
from sklearn import datasets, linear_model, metrics

boston = datasets.load_boston(return_X_y=False)

X = boston.data

y = boston.target

