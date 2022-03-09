import csv 
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

file = pd.read_csv("data.csv")

b=file["Mobile Brand"].to_list()
r=file["Avg Rating"].to_list()

fig=pf.create_distplot([r],["mobile brand"],show_hist=False)
fig.show()

mean = st.mean(b)
median = st.median(b)
mode = st.mode(b)

print("Mean of brand is {}" .format(mean))
print("Median of brand is {}" .format(median))
print("Mode of brand is {}" .format(mode))

ST=st.stdev(b)
print("ST is {}" .format (ST))

min1= mean-ST
max1= mean+ST
firstSDList=[]
for o in b:
    if o>min1 and o<max1:
        firstSDList.append(o)

a=len(firstSDList)
total=len(b)

P=(a*100)/total

print("{}% of brand" .format(P))
