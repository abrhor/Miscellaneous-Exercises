# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import quandl

x = y = np.arange(100)
plt.plot(x,y)
plt.show()

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(x)
plt.show()

x = quandl.get("WIKI/AMZN", start_date="2017-1-5")
print(x)

for i in range(3): print(i)