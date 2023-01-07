## add code for data class here
class Data:
    def __init__(self, filepath):
        self.filepath = filepath  # saves the file path that is used in other funtions 
        
    def make_df(self):
        import pandas as pd
        dataframe = pd.read_csv(self.filepath, parse_dates = True)  # reads csv file and makes a dataframe
        return dataframe  # returns the produced dataframe

    def plot(self, title):
        import matplotlib.pyplot as plt
        import numpy as np  
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plotdata = self.make_df() # make the data frame for the data to plot using other funtion within the class
        ax.plot(plotdata["time"], plotdata["mf"])  # Plot the chart
        ax.set_ylabel("mf")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(title)  #
        plt.show()  # display the plot
        