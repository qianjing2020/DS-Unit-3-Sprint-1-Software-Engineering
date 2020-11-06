import unittest
from pandas import DataFrame
from my_lambdata.states_oop import DataFrameProcessor


class TestStateOOP(unittest.TestCase):

    def test_dataframe_processor(self):

        df = DataFrame({"state": ["CA", "CO", "CT", "TX"]})
        processor = DataFrameProcessor(df=df)

        self.assertEqual(len(processor.df.columns), 1)
        self.assertEqual(list(processor.df.columns), ["state"])
        self.assertEqual(processor.df.iloc[0]["state"], 'CA')

        processor.add_state_name_col()

        self.assertEqual(len(processor.df.columns), 2)
        self.assertEqual(list(processor.df.columns), ['state', 'name'])
        self.assertEqual(processor.df.iloc[0]["state"], 'CA')
        self.assertEqual(processor.df.iloc[0]["name"], 'California')


if __name__ == "__main__":
    unittest.main()
