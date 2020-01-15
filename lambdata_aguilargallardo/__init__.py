"""
lambdata – a collection of data science helper functions
"""

import pandas as pd
import numpy as np

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

def find_nulls(df):
    """
    Looks for null values in your dataframe.
    """

    return df.isnull().sum()


def ascending(df, x):
  """
  Ascends your dataframe from greatest to least by whichever column "x" that you
  call.

  Need to call x = "what ever column you are sorting by" to be able to sort the
  value for that specific column
  on your dataframe.
  """
  x = x
  return df.sort_values(by=x, ascending=False)


class Food:
"""
Class to type in your favorite food.
"""
    def __init__(self, name):
        self.name = name
        """
        First argument, name your favorite food.
        """

    def change_name(self, new_name):
        self.name = new_name
        """
        Second arguement change name of your favorite food.
        """
        
