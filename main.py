"""GDP graph generator
made by Alex 22 August 2022"""

import matplotlib.pyplot as plt, csv, pylab, numpy, pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Name', 'Age', 'Marks']

with open("life-exp-data.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        if i == 'PRK' or i == 'CHN':
            print('line[{}] = {}'.format(i, line))


"""xVals = df.Years
yVals = df.PRK

xVals2 = df.Years
yVals2 = df.CHN"""

"""from climate code:
""""""
plt.plot(xVals, yVals, color='blue', label='Life expectancy over time')
plt.plot(xVals2, yVals2, color='red', label='Life expectancy over time')
"""


"""PRK
CHN"""

"""pandas.errors.ParserError: Error tokenizing data. C error: Expected 3 fields in line 5, saw 67
"""