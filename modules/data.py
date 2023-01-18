## add code for data class here
class Data:
    def __init__(self, filepath, speciesfile):
        import pandas as pd 
        import numpy as np 
        import matplotlib.pyplot as plt
        import sys
        
        # error check for filepath and species file path type that exits the script if the filepaths are not a strings
        if type(filepath) != type("error test"):
            sys.exit('filepath must be a string with "" around it' )
        else:
            pass
        
        if type(speciesfile) != type("error test"):
            sys.exit('species info filepath must be a string with "" around it' )
        else:
            pass
        
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
        
        # sets self.species to set the name of the species the data is for
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
        
        # makes dataframes for the monthly and daily averages when making an instance of the data class
        self.daily_average = self.data.resample("D", origin = "start_day").mean()
        self.monthly_average = self.data.resample("M").mean()
        
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
    
    def plot_daily_average(self):
        plotdata_daily = self.daily_average
        
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plt.plot(plotdata_daily, label = self.sitecode, color = "blue")  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of {self.species} in {self.units}")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(f"Daily average Mole fraction of {self.species} over a year" )  #  set the title of the plot
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
    
    def multiplot_daily_average(self, dataset2):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))
        
        plotdata1 = self.daily_average # creating a variable with two dataframes needed for plotting
        plotdata2 = dataset2.daily_average
        
        # plot both data sets:
        plt.plot(plotdata1, label = f"{self.sitecode}, {self.species}, units = {self.units}", color = "blue")
        plt.plot(plotdata2, label = f"{dataset2.sitecode}, {dataset2.species}, units = {dataset2.units}", color = "red", alpha = 0.5)
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of gas species")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title("Daily average mole fraction of gas species' over a year")
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
    
    def plot_monthly_average(self):
        plotdata_monthly = self.monthly_average
        
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plt.plot(plotdata_monthly, label = self.sitecode, color = "blue")  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of {self.species} in {self.units}")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(f"monthly average Mole fraction of {self.species} over a year" )  #  set the title of the plot
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
        
    def multiplot_monthly_average(self, dataset2):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))
        
        plotdata1 = self.monthly_average # creating a variable with two dataframes needed for plotting
        plotdata2 = dataset2.monthly_average
        
        # plot both data sets:
        plt.plot(plotdata1, label = f"{self.sitecode}, {self.species}, units = {self.units}", color = "blue")
        plt.plot(plotdata2, label = f"{dataset2.sitecode}, {dataset2.species}, units = {dataset2.units}", color = "red", alpha = 0.5)
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of gas species")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title("Monthly average mole fraction of gas species' over a year")
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
    
    def plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        
        plotdata = self.data # make the data frame for the data to plot using other funtion within the class
        
        plt.plot(plotdata, label = self.sitecode, color = "blue")  # Plot the chart
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of {self.species} in {self.units}")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title(f"Mole fraction of {self.species} hourly over a year" )  #  set the title of the plot
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
        
    def multiplot(self, dataset2):
        import matplotlib.pyplot as plt
        import numpy as np
        fig, ax = plt.subplots(figsize = (8, 5))
        
        plotdata1 = self.data # creating a variable with two dataframes needed for plotting
        plotdata2 = dataset2.data
        
        # plot both data sets:
        plt.plot(plotdata1, label = f"{self.sitecode}, {self.species}, units = {self.units}", color = "blue")
        plt.plot(plotdata2, label = f"{dataset2.sitecode}, {dataset2.species}, units = {dataset2.units}", color = "red", alpha = 0.5)
        plt.gcf().autofmt_xdate()  # auto formats the date for the x axis
        ax.set_ylabel(f"Mole fraction of gas species")  # set y label
        ax.set_xlabel("Time")  # set x label
        ax.set_title("Mole fraction of gas species' over a year")
        plt.legend(loc = "upper left")
        plt.show()  # display the plot
        
    def residual_plot_hour(self):
        import seaborn as sns
        import matplotlib.pyplot as plt
        import numpy as np 
        
        residual_plot_data = self.data
        residual_plot_data["hour"] = residual_plot_data.index.hour # making a new column in a separate data frame for plotting data
        fig, ax = plt.subplots(figsize = (8, 5))
        sns.residplot(ax = ax, data = residual_plot_data, x = "hour", y = "mf", order = 1) # using seaborn to make a residuals plot
        ax.set_xlabel("Time/ Hour of the day") # setting axis' labels
        ax.set_ylabel(f"Mole fraction of {self.species}")
        
    def residual_plot_day(self):
        import seaborn as sns
        import matplotlib.pyplot as plt
        import numpy as np 
        
        residual_plot_data = self.data
        residual_plot_data["day"] = residual_plot_data.index.day # making a new column in a separate data frame for plotting data
        fig, ax = plt.subplots(figsize = (8, 5))
        sns.residplot(ax = ax, data = residual_plot_data, x = "day", y = "mf", order = 1) # using seaborn to make a residuals plot
        ax.set_xlabel("Time/ Day of the month") # setting axis' labels
        ax.set_ylabel(f"Mole fraction of {self.species}")
        
    def residual_plot_month(self):
        import seaborn as sns
        import matplotlib.pyplot as plt
        import numpy as np 
        
        residual_plot_data = self.data
        residual_plot_data["month"] = residual_plot_data.index.month # making a new column in a separate data frame for plotting data
        fig, ax = plt.subplots(figsize = (8, 5))
        sns.residplot(ax = ax, data = residual_plot_data, x = "month", y = "mf", order = 1) # using seaborn to make a residuals plot
        ax.set_xlabel("Time/ month pf the year") # setting axis' labels
        ax.set_ylabel(f"Mole fraction of {self.species}")
    
    def baseline_estimate(self):
        import pandas as pd
        # funtion that selects the 5th perecentile of the data for each month 
        self.baseline = self.data
        self.baseline = self.baseline.resample("M").quantile(q = 0.05, interpolation="linear") # resampling the dataframe so that only the 5th percentile for each month is in there
        return self.baseline
         
    
    def baseline_plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        
        fig, ax = plt.subplots(figsize = (8, 5))  # produces the figure to put the plot onto
        self.baseline = self.baseline_estimate()       
        ax.plot(self.data.index, self.data["mf"], label = self.sitecode) # plots original data 
        ax.plot(self.baseline.index, self.baseline["mf"], label = "Baseline") # plots baseline
        ax.set_ylabel(f"Mole fraction of {self.species} in {self.units}")
        ax.set_xlabel("Time")
        plt.legend(loc = "upper left")
        plt.show()