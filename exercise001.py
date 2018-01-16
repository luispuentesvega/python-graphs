import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Sacramentorealestatetransactions.csv") #Reading the dataset in a dataframe using Pandas
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
arr_labels = df['city'].value_counts().keys().tolist()
arr_sizes = df['city'].value_counts().tolist()

labels = []
sizes = []
i=0
for label in arr_labels:
	if i>4:
		break
	labels.append(label)
	i=i+1

i=0
for size in arr_sizes:
	if i>4:
		break
	sizes.append(size)
	i=i+1

i = 0
explode = []
for i in range(5):
	if i==0:
		explode.append(0.1)
	else:
		explode.append(0)

print(len(labels))
print(len(sizes))
print(len(explode))


#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Cant Cities Use')

plt.show()