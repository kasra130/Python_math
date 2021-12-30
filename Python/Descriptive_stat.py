import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import itertools


def space(n):
    print("\n"*n)


# A)
# load the CSV into python
originalDataset = pd.read_csv(r"descriptivestat\useless.csv")
print(originalDataset)
originalDataset = originalDataset.dropna()  # inplace = true is similar to
print(originalDataset.head())  # head() displays a dataframe in the cell output

# mean
column1_ave = originalDataset["column1"].mean()
column2_ave = originalDataset["column2"].mean()
column3_ave = originalDataset["column3"].mean()
column4_ave = originalDataset["column4"].mean()
column5_ave = originalDataset["column5"].mean()
column6_ave = originalDataset["column6"].mean()

# SD
column1_std = originalDataset["column1"].std()
column2_std = originalDataset["column2"].std()
column3_std = originalDataset["column3"].std()
column4_std = originalDataset["column4"].std()
column5_std = originalDataset["column5"].std()
column6_std = originalDataset["column6"].std()

# range
column1_range = originalDataset["column1"].max(
) - originalDataset["column1"].min()
column2_range = originalDataset["column2"].max(
) - originalDataset["column2"].min()
column3_range = originalDataset["column3"].max(
) - originalDataset["column3"].min()
column4_range = originalDataset["column4"].max(
) - originalDataset["column4"].min()
column5_range = originalDataset["column5"].max(
) - originalDataset["column5"].min()
column6_range = originalDataset["column6"].max(
) - originalDataset["column6"].min()


print("This is average of column 1 " + str(round(column1_ave, 4)) + " , Standard deviation " +
      str(round(column1_std, 4)) + " with range of " + str(round(column1_range, 4)))
print("This is average of column 2 " + str(round(column2_ave, 4)) + " , Standard deviation " +
      str(round(column2_std, 4)) + " with range of " + str(round(column2_range, 4)))
print("This is average of column 3 " + str(round(column3_ave, 4)) + " , Standard deviation " +
      str(round(column3_std, 4)) + " with range of " + str(round(column3_range, 4)))
print("This is average of column 4 " + str(round(column4_ave, 4)) + " , Standard deviation " +
      str(round(column4_std, 4)) + " with range of " + str(round(column4_range, 4)))
print("This is average of column 5 " + str(round(column5_ave, 4)) + " , Standard deviation " +
      str(round(column5_std, 4)) + " with range of " + str(round(column5_range, 4)))
print("This is average of column 6 " + str(round(column6_ave, 4)) + " , Standard deviation " +
      str(round(column6_std, 4)) + " with range of " + str(round(column6_range, 4)))

######################################################################################################################


# B)

column1_plot = originalDataset["column1"].plot(
    y='column1', use_index=True, label='column 1')
column2_plot = originalDataset["column2"].plot(
    y='column2', use_index=True, label='column 2')
column3_plot = originalDataset["column3"].plot(
    y='column3', use_index=True, label='column 3')
column4_plot = originalDataset["column4"].plot(
    y='column4', use_index=True, label='column 4')
column5_plot = originalDataset["column5"].plot(
    y='column5', use_index=True, label='column 5')
column6_plot = originalDataset["column6"].plot(
    y='column6', use_index=True, label='column 6')
plt.title("Garbs: Column vs Index")
plt.legend()
plt.show()
# print(column1_plot)

space(10)

################################################################################################################################


""" # C)
plt.scatter(y=originalDataset['column1'], x=originalDataset['column2'])
plt.title("column1 vs column2")
plt.xlabel("column2")
plt.ylabel("column1")
#plt.show()


plt.scatter(y=originalDataset['column3'], x=originalDataset['column4'])
plt.title("Garbs: Column3 vs column4")
plt.xlabel("column4")
plt.ylabel("column3")
#plt.show()

plt.scatter(y=originalDataset['column5'], x=originalDataset['column6'])
plt.title("Garbs: Column5 vs column6")
plt.xlabel("column6")
plt.ylabel("column5")
#plt.show() """


data = [originalDataset['column1'],
        originalDataset['column2'], originalDataset['column3'], originalDataset['column4'], originalDataset['column5'], originalDataset['column6']]

column1 = originalDataset["column1"]
column2 = originalDataset["column2"]
column3 = originalDataset["column3"]
column4 = originalDataset["column4"]
column5 = originalDataset["column5"]
column6 = originalDataset["column6"]

""" for i in range(0, len(data)+1):
    for subset in itertools.combinations(data, i):
        print(subset) """

""" for pair in itertools.combinations((column1, column2, column3,column4, column5, column6), 2):
    fig, ax = plt.subplots()
    ax.scatter(pair[0], pair[1])
plt.show()
 """
d = dict(a=originalDataset['column1'], b=originalDataset['column2'], c=originalDataset['column3'], d=originalDataset['column4'], f=originalDataset['column5'], e=originalDataset['column6'])

for (xk, xv), (yk, yv) in itertools.combinations(d.items(), 2):
    fig, ax = plt.subplots()
    ax.scatter(xv, yv, label=f'({xk}, {yk})')
    ax.set_xlabel(f'({xk})')
    ax.set_ylabel(f'({yk})')
    ax.legend()
plt.show() 
