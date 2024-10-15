import matplotlib.pyplot as plt
import pandas as pd

frame = pd.read_csv("hw2\\data_patients.csv", 
                    delimiter=';', encoding='utf-8')
fig, ax = plt.subplots(figsize=(10, 5))

print(frame)
rects = ax.bar(frame['Год'], frame['Значение показателя'])
ax.bar_label(rects, padding=3)
ax.yaxis.



plt.show()