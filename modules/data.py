## add code for data class here
class Data:
    def __init__(self, filepath, speciesfile):
        import pandas as pd 
        import numpy as np 
        import matplotlib.pyplot as plt
        
        
        
        self.filepath = filepath  # saves the file paths
        self.speciesfile = speciesfile
        
        # code which extracts the site code from the filepath:
        self.sitecode = ""  # set the sitecode to nothing to be reassigned
        sitecode_extract = filepath[5]+filepath[6]+filepath[7]  # selects the characters from the filepath string which corresponds to the sitecode
        
        # sets self.sitecode to give full description of site
        if sitecode_extract == "mhd": 
            self.sitecode = "MHD: Mace Head"
        elif sitecode_extract == "tac":
            self.sitecode = "TAC: Tacolneston"
            
        # code which extracts the species from the filepath:
        self.species = "" # set the species to nothing to be reassigned 
        species_extract = filepath[9]+filepath[10]+filepath[11]
        
        # sets self.species to name of the species the data is for
        if species_extract == "ch4":
            self.species = "Methane"
        elif species_extract == "co2":
            self.species = "Carbon dioxide"
        elif species_extract == "n2o":
            self.species = "Nitrous oxide"
        
        # making dataframes
        df = pd.read_csv(filepath, index_col = "time", parse_dates = True)  # makes a dataframe with data in it
        self.data = df  # saving the new dataframe
        
        df_2 = pd.read_csv(speciesfile, index_col = "species")  # makes a dataframe with species info
        self.speciesinfo = df_2
        
        # code which extracts units of measurements using filepath
        self.units = ""
        units_extract = ""
        
        # code which uses the species_extract to extract the units from the species info file 
        if species_extract == "ch4":
            units_extract = df_2["units"].iloc[1]
        elif species_extract == "n2o":
            units_extract = df_2["units"].iloc[2]
        elif species_extract == "co2":
            units_extract = df_2["units"].iloc[0]
        
        if units_extract == "ppb":
            self.units = "Parts per billion"
        elif units_extract == "ppm":
            self.units = "Parts per million"
            
        # code which extracts calibration scale using filepath
        self.calibrationscale = ""
        calscale_extract = ""
        
        # code which uses the species_extract to extract the calibration scale from the species info file 
        if species_extract == "ch4":
            calscale_extract = df_2["scale"].iloc[1]
        elif species_extract == "n2o":
            calscale_extract = df_2["scale"].iloc[2]
        elif species_extract == "co2":
            calscale_extract = df_2["scale"].iloc[0]
            
        if calscale_extract == "noaa":
            self.calibrationscale = "National Oceanic and Atmospheric Administration"
        if calscale_extract == "sio":
            self.calibrationscale = "Scripps Institution of Oceanography"
    
    # code which calculates the daily average of the data
    def calculate_daily_average(self):
        daily_average = self.data.resample('D', origin = 'start_day').mean()
        return daily_average
    
    def plot_daily_average(self, dataframe):
        plotdata_daily = self.data
        daily_average_plotting_data = plotdata_daily.resample('D', origin = 'start_day').mean()
        
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plt.plot(daily_average_plotting_data, label = dataframe.sitecode, color = "blue")  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of {dataframe.species} in {dataframe.units}")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(f"daily average Mole fraction of {dataframe.species} over a year" )  #  set the title of the plot
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
    
    def multiplot_daily_average(self):
        pass
    
    # code which calculates the monthly average of the data
    def calculate_monthly_average(self):
        monthly_average = self.data.resample('M').mean()
        return monthly_average
    
    def plot_monthly_average(self, dataframe):
        plotdata_monthly = self.data
        monthly_average_plotting_data = plotdata_monthly.resample('M').mean()
        
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plt.plot(monthly_average_plotting_data, label = dataframe.sitecode, color = "blue")  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of {dataframe.species} in {dataframe.units}")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(f"monthly average Mole fraction of {dataframe.species} over a year" )  #  set the title of the plot
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
        
    def multiplot_monthly_average(self):
        pass
    
    def plot(self, dataframe):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plotdata = dataframe.data # make the data frame for the data to plot using other funtion within the class
        
        plt.plot(plotdata, label = dataframe.sitecode, color = "blue")  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of {dataframe.species} in {dataframe.units}")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(f"Mole fraction of {dataframe.species} over a year" )  #  set the title of the plot
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
        
    def multiplot(self, dataframe1, dataframe2):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))
        
        plotdata1 = dataframe1.data # creating a variable with two dataframes needed for plotting
        plotdata2 = dataframe2.data
        
        # plot both data sets:
        plt.plot(plotdata1, label = f"{dataframe1.sitecode}, {dataframe1.species}, units = {dataframe1.units}", color = "blue")
        plt.plot(plotdata2, label = f"{dataframe2.sitecode}, {dataframe2.species}, units = {dataframe2.units}", color = "red", alpha = 0.5)
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of gas species")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title("Mole fraction of gas species' over a year")
        plt.legend(loc = "upper left")
        plt.show()  # display the plot