# -*- coding: utf-8 -*-
"""Prob 1.2/17

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17Ct5kx6dpb7RPDVs1YPxHjEByh-w5lHt
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import statistics as st
import pandas as pd

spotwelds = pd.read_csv("https://raw.githubusercontent.com/eliozhangwa/MATH2315/main/exer01-0217.csv")
spotwelds.head()
spotwelds.shape
plt.hist(spotwelds['5434'],  color=['b'], density=True, bins = 10)