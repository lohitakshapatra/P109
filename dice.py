import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd

dice_result=[]
df=pd.read_csv("StudentsPerformance.csv")

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

#calculate mean , meadian,mode
mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)

print("Mean is :-",mean)
print("median is :-",median)
print("Mode is :-",mode)
print("standard deviation  is :-",std_deviation)

fig=ff.create_distplot([dice_result],["Result"],show_hist=False)

#finding first ,second and third std deviation start and end values
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print(first_std_deviation_start,first_std_deviation_end)
print(second_std_deviation_start,second_std_deviation_end)
print(third_std_deviation_start,third_std_deviation_end)
#plotting the graph lines of mean 
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="std_deviation1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="std_deviation1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="std_deviation2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="std_deviation2"))
fig.show()
#printing the findings
list_of_data_within_first_std_dev=[result for result in dice_result if result > first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_second_std_dev=[result for result in dice_result if result > second_std_deviation_start and result<second_std_deviation_end]
list_of_data_within_third_std_dev=[result for result in dice_result if result > third_std_deviation_start and result<third_std_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_first_std_dev)*100.0/len(dice_result))) 
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_second_std_dev)*100.0/len(dice_result))) 
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_third_std_dev)*100.0/len(dice_result)))