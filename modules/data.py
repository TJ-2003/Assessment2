## add code for data class here
class Data:
    def __init__(self, filepath):
        self.filepath = filepath  # saves the file path that is used in other funtions
        
        import pandas as pd
        df = pd.read_csv(filepath, index_col = "time", parse_dates = True)  # makes a dataframe with data in it
        self.data = df  # saving the new dataframe

    def plot(self, title):
        import matplotlib.pyplot as plt
        import numpy as np  
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plotdata = self.data
        # make the data frame for the data to plot using other funtion within the class
        plt.plot(plotdata)  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel("mf")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(title)  #  set the title of the plot
        plt.show()  # display the plot
        