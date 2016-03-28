import numpy as np
import matplotlib.pyplot as plt
import unittest, environment, sys, agile_flows, waterfall_flows, copy

import time

from base import *

agile_results = [[],[]]
waterfall_results = [[],[]]

seed = 0

for i in range(8):
    agile_flows.setup_environment()
    random.seed(environment.resources["seed"])
    environment.resources["mutating"] = i % 2 == 1
    seed += 60
    environment.resources["seed"] = seed
    try:
        agile_flows.implement_50_features()
    except Exception, e:
        print str(e)
    agile_results[i%2].append(copy.deepcopy(environment.resources))

seed = 0

for i in range(8):
    waterfall_flows.setup_environment()
    random.seed(environment.resources["seed"])
    environment.resources["mutating"] = i % 2 == 1
    seed += 60
    environment.resources["seed"] = seed
    try:
        waterfall_flows.implement_50_features()
    except Exception, e:
        print str(e)
    waterfall_results[i%2].append(copy.deepcopy(environment.resources))

# Calculate some results. Which is more affected?
agile_aggregate_times = [0, 0]
waterfall_aggregate_times = [0, 0]

for i in range(4):
    agile_aggregate_times[0] += agile_results[0][i]["time"]
    agile_aggregate_times[1] += agile_results[1][i]["time"]
for i in range(4):
    waterfall_aggregate_times[0] += waterfall_results[0][i]["time"]
    waterfall_aggregate_times[1] += waterfall_results[1][i]["time"]

agile_average_times = [0,0]
waterfall_average_times = [0,0]

agile_average_times[0] = agile_aggregate_times[0]/4
agile_average_times[1] = agile_aggregate_times[1]/4
waterfall_average_times[0] = waterfall_aggregate_times[0]/4
waterfall_average_times[1] = waterfall_aggregate_times[1]/4

agile_delta = abs(agile_average_times[1] - agile_average_times[0])
waterfall_delta = abs(waterfall_average_times[1] - waterfall_average_times[0])

agile_delta /= float(agile_average_times[0])
waterfall_delta /= float(waterfall_average_times[0])

agile_deltas = []
waterfall_deltas = []
for index in range(4):
    agile_deltas.append(abs(agile_results[1][index]['time'] - agile_results[0][index]['time'])/float(agile_results[0][index]['time']))
    waterfall_deltas.append(abs(waterfall_results[1][index]['time'] - waterfall_results[0][index]['time'])/float(waterfall_results[0][index]['time']))

N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, agile_deltas, width, color='r')
rects2 = ax.bar(ind + width, waterfall_deltas, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Delta of time taken')
ax.set_title('Delta of time taken when mutated, varying seed')
ax.set_xticks(ind + width)
ax.set_xticklabels(('0', '50', '100', '150'))

ax.legend((rects1[0], rects2[0]), ('Agile', 'Waterfall'))
plt.show()

