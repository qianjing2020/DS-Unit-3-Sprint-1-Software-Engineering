import pandas

def add_state_names_column(my_df):
    """ 
    Add a column of corresponding state names to a dataframe. 

    Params (my_df) a dateframe with a column "abbrev" that has state abbreviation

    Return a copy of the original dataframe, but with an extra column with full state names.
    """
    new_df = my_df.copy()
    name_map = {"CA": "California", "CO": "Colorado", "CT":"Connecticut", "DC":"District of Columbia", "TX":"Texas" }
    # breakpoint()
    new_df["name"] = new_df["state"].map(name_map)
    return new_df

if __name__=="__main__":
    df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
    print(df.head())

    new_df = add_state_names_column(df)
    print(new_df.head())