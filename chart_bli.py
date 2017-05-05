import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from radar_chart import radar

# Read csv with related columns
cols = ['Country', 'Indicator', 'Inequality', 'Unit', 'Value']
df = pd.read_csv('BLI_05052017143301063.csv', usecols=cols)

# Use total values only to make it simpler
df = df[df['Inequality'] == 'Total']
df['Value'] = df.groupby('Indicator')['Value'].apply(
    lambda x: (x - x.min()) / (x.max() - x.min()))
# Normalize values
df = df.groupby('Country')

# A country index can be querried by get_group(country)
# print(df.get_group('Japan'))

# setup radar chart


def plot_country(ax, theta, v, c, l):
    ax.plot(theta, v, color='k', label='')
    ax.fill(theta, v, color=c, alpha=.5, label=l)


labels = df.get_group('Japan')['Indicator'].unique()
theta = radar(len(labels))
fig, ax = plt.subplots(subplot_kw={'projection': 'radar'})

ax.set_varlabels(labels)
ax.get_yaxis().set_ticks([])
ax.set_ylim(0, 1)

plot_country(ax, theta, df.get_group('Japan')['Value'],
             np.random.rand(3, ), 'Japan')
plot_country(ax, theta, df.get_group('Turkey')['Value'],
             np.random.rand(3, ), 'Turkey')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height * 0.9])
ax.legend(bbox_to_anchor=(1.1, 1.1))

plt.show()
