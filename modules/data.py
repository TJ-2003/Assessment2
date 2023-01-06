## add code for data class here
class Data:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def make_df(self):
        import pandas as pd
        dataframe = pd.read_csv(self.filepath, index_col = "time", parse_dates = True)
        return dataframe
        