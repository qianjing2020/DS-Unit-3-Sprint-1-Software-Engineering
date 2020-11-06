# my_lambdata.states_oop.py

import pandas as pd

# refractor the state.py into oop approach

class DataFrameProcessor(): 
    
    def __init__(self, df):
        self.df = df
        
    def add_state_name_col(self):

        name_map = {
            "CA": "California",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DC": "District of Columbia",
            "TX": "Texas"}

        self.df["name"] = self.df["state"].map(name_map)
        

if __name__ == "__main__":
    df = pd.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
    
    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.add_state_name_col()
    print(processor.df.head())

