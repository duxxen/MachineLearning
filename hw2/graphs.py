# coding = utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(figsize=(10, 5))
frame = pd.read_csv('hw2\\data_registration.csv',
                    delimiter=';', encoding='utf-8', header=1)

alldata = frame.columns[4:13]
quartals = frame['Квартал'].unique()
years = frame['Год'].unique()
x = np.arange(len(years))
bwidth = 0.25
bmult = 0

datatype = alldata[0]
frame1 = frame.loc[:, ['Год', 'Квартал', datatype]].sort_values('Квартал')
for i in range(0, 16, 4):
    offset = bwidth * bmult
    subframe = frame1[i : i + 4]
    rects = axs.bar(offset, subframe[datatype], bwidth, label=quartals)
    axs.bar_label(rects, padding=3)
    bmult += 1

print(frame1)
print(frame1[datatype])


axs.set_ylim(0, 50000)
axs.legend(loc='upper left', ncols = quartals.size)
axs.set_xticks(x + bwidth * 1.5, years)
plt.show()

