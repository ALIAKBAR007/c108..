import csv 
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

file = pd.read_csv("data.csv")

b=file["Mobile Brand"].to_list()
r=file["Avg Rating"].to_list()

fig=pf.create_distplot([r],["Ratings"],show_hist=False)
fig.show()

mean = st.mean(r)
median = st.median(r)
mode = st.mode(r)

print("Mean of rating is {}" .format(mean))
print("Median of rating is {}" .format(median))
print("Mode of rating is {}" .format(mode))

ST=st.stdev(r)
print("ST is {}" .format (ST))

min1= mean-ST
max1= mean+ST
firstSDList=[]
for o in r:
    if o>min1 and o<max1:
        firstSDList.append(o)

a=len(firstSDList)
total=len(r)

P=(a*100)/total

print("{}% of rating" .format(P))
