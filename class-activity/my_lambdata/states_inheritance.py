# my_lambdata.states_oop.py

from pandas import DataFrame

class CustomFrame(DataFrame):
    """ Create a class inherited from pandas DataFrame class, and add additional method"""  
          
    def add_state_name_col(self):
        """ Add a column of names to the dataframe"""
        
        name_map = {
            "CA": "California",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DC": "District of Columbia",
            "TX": "Texas"}
        breakpoint()
        self["name"] = self["state"].map(name_map)
        

if __name__ == "__main__":
    df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})    
    # processor = DataFrameProcessor(df=df)
    # print(processor.df.head())
    # processor.add_state_name_col()
    # print(processor.df.head())

    custom_frame = CustomFrame({"state": ["CT", "CO", "CA", "TX"]})
    custom_frame.add_state_name_col()
    print(custom_frame.head())
