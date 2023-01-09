## add code for data class here
class Data:
    def __init__(self, filepath):
        self.filepath = filepath  # saves the file path that is used in other funtions
        
        # code which extracts the site code from the filepath:
        
        self.sitecode = ""  # set the sitecode to nothing to be reassigned
        
        sitecode_extract = filepath[5]+filepath[6]+filepath[7]  # selects the characters from the filepath string which corresponds to the sitecode
        
        # sets self.sitecode to give full description of site
        if sitecode_extract == "mhd": 
            self.sitecode = "MHD: Mace Head, W. coast of the Republic of Ireland ect."
        elif sitecode_extract == "tac":
            self.sitecode = "TAC: Tacolneston, East Anglia"
            
        
        self.species = filepath[9]+filepath[10]+filepath[11]
        
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
        