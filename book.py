# Import libraries
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

# Read and create Dataframe
covid = pd.read_csv("covid-variants.csv")

print(covid.head(20))

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')