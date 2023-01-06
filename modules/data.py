## add code for data class here
class Data:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def make_df(self):
        import pandas as pd
        dataframe = pd.read_csv(self.filepath, parse_dates = True)
        return dataframe

    def plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots()
        
        plotdata = self.make_df()
        plt.plot(plotdata["time"], plotdata["mf"])  # Plot the chart
        plt.show()  # display
        