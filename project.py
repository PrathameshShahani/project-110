import statistics
import pandas as pd
import plotly.figure_factory as ff
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
population_stdev=statistics.stdev(data)
print("Population mean: ",population_mean)
print("Population Standard Deviation: ",population_stdev)

def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    sample_mean=statistics.mean(mean_list)
    sample_stdev=statistics.stdev(mean_list)
    print("Mean of sampling distibution: ",sample_mean)
    print("Standard deviation of sampling distribution: ",sample_stdev)
    show_fig(mean_list)
setup()