import pandas as pd

class DataSorter:
    @staticmethod
    def sort_by_row(df, column, ascending=True):
        """
        Sorts the DataFrame rows based on the values in the specified column.

        Parameters:
        df (pd.DataFrame): The DataFrame to be sorted.
        column (str): The column name to sort by.
        ascending (bool): Sort order. True for ascending, False for descending. Default is True.

        Returns:
        pd.DataFrame: The sorted DataFrame.
        """
        return df.sort_values(by=column, ascending=ascending)
