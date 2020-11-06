import unittest
from pandas import DataFrame
from my_lambdata.states import add_state_names_column


class TestState(unittest.TestCase):
 
    def test_add_names_col(self):
        
        df = DataFrame({"state":["CA", "CO", "CT", "TX"]})
        self.assertEqual(len(df.columns), 1)
        self.assertEqual(list(df.columns), ["state"])
        self.assertEqual(df.iloc[0]["state"], 'CA')

        df2 = add_state_names_column(df)

        self.assertEqual(len(df2.columns), 2)
        self.assertEqual(list(df2.columns), ['state', 'name'])
        self.assertEqual(df2.iloc[0]["state"], 'CA')
        self.assertEqual(df2.iloc[0]["name"], 'California')


if __name__ == "__main__":
    unittest.main()
