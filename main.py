import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

# Calculating the mean and standard deviation of the whole data
mean_data = statistics.mean(data)
std_deviation_data = statistics.stdev(data)
print("Mean Of Data: ", mean_data)
print("Standard Deviation Of Data: ", std_deviation_data)
print()

# Plotting the graph
fig = ff.create_distplot([data], ["Reading Scores"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean_data, mean_data], y=[0, 0.20], mode="lines", name="MEAN"))
fig.layout.update({
    "title": "Reading Scores Of All Students",
    "xaxis": {"title": "Reading Scores"}
})
fig.show()

# Code to find the mean of 30 data points 100 times 
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

# Calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean Of Sampling Distribution: ", mean)
print("Standard Deviation Of Sampling Distribution: ", std_deviation)
print()

# Plotting the mean of the sampling distribution
figure = ff.create_distplot([mean_list], ["Reading Scores"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
figure.layout.update({
    "title": "Reading Scores Of Sample Students(With Mean)",
    "xaxis": {"title": "Reading Scores"}
})
figure.show()

# Finding the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("Standard Deviation 1: ", first_std_deviation_start, first_std_deviation_end)
print("Standard Deviation 2: ", second_std_deviation_start, second_std_deviation_end)
print("Standard Deviation 3: ", third_std_deviation_start, third_std_deviation_end)
print()

# Plotting the graph with traces
graph = ff.create_distplot([mean_list], ["Reading Scores"], show_hist=False)
graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.27], mode="lines", name="MEAN"))
graph.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.27], mode="lines", name="STANDARD DEVIATION 1 START"))
graph.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.27], mode="lines", name="STANDARD DEVIATION 1 END"))
graph.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.27], mode="lines", name="STANDARD DEVIATION 2 START"))
graph.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.27], mode="lines", name="STANDARD DEVIATION 2 END"))
graph.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.27], mode="lines", name="STANDARD DEVIATION 3 START"))
graph.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.27], mode="lines", name="STANDARD DEVIATION 3 END"))
graph.layout.update({
    "title": "Reading Scores Of Sample Students(With Traces)",
    "xaxis": {"title": "Reading Scores"}
})
graph.show()

# Creating New Sample Mean
ds = pd.read_csv("data.csv")
data2 = ds["reading_time"].tolist()

# Calculating the mean and standard deviation of the data 2
mean_data2 = statistics.mean(data)
std_deviation_data2 = statistics.stdev(data)
print("Mean Of Data 2: ", mean_data2)
print("Standard Deviation Of Data 2: ", std_deviation_data2)
print()

# Plotting Graph Of Data With New Sample Mean And Traces
chart = ff.create_distplot([mean_list], ["Reading Scores"], show_hist=False)
chart.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.27], mode="lines", name="MEAN (FOR WHOLE DATA)"))
chart.add_trace(go.Scatter(x=[mean_data2, mean_data2], y=[0, 0.27], mode="lines", name="MEAN (FOR SAMPLE DATA)"))
chart.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.27], mode="lines", name="STANDARD DEVIATION 1 START"))
chart.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.27], mode="lines", name="STANDARD DEVIATION 1 END"))
chart.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
chart.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
chart.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
chart.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
chart.layout.update({
    "title": "Reading Scores Of Sample Students(With Traces And New Sample Mean)",
    "xaxis": {"title": "Reading Scores"}
})
chart.show()

# New Mean Is Greater Than Smapling Mean
# Z-Score
z_score = (mean_data2 - mean) / std_deviation
print("The Z Score Is: ", z_score)
print()
