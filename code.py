import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv('StudentsPerformance.csv')
data = df['writing score'].tolist()

mean = st.mean(data)
stDev = st.stdev(data)
median = st.median(data)
mode = st.mode(data)

first_stdev_start, first_stdev_end = mean - stDev, mean + stDev
second_stdev_start, second_stdev_end = mean - (2*stDev), mean + (2*stDev)
third_stdev_start, third_stdev_end = mean - (3*stDev), mean + (3*stDev)

fig = ff.create_distplot([data], ['writing score'], show_hist = False)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = 'lines', name = 'Mean'))

fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = 'lines', name = 'Standard Deviation 1 Start'))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = 'lines', name = 'Standard Deviation 1 End'))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = 'lines', name = 'Standard Deviation 2 Start'))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = 'lines', name = 'Standard Deviation 2 End'))

fig.show()

listofDataWithinFirstDev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
listofDataWithinSecondDev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
listofDataWithinThirdDev = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print('{}% of data lies within first standard deviation'.format(len(listofDataWithinFirstDev)*100/len(data)))
print('{}% of data lies within second standard deviation'.format(len(listofDataWithinSecondDev)*100/len(data)))
print('{}% of data lies within third standard deviation'.format(len(listofDataWithinThirdDev)*100/len(data)))