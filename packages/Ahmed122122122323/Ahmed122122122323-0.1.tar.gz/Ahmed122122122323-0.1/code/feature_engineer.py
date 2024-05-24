import pandas as pd


class FeatureEngineer:
    @staticmethod
    def create_feature(df, column, func):

        """
        adds a new column to a DataFrame by applying a given function to an existing column.

        Parameters:

        df: The DataFrame containing the data.
        column: The name of the column in the DataFrame to which the function will be applied.
        func: The function to be applied to each element of the specified column.
        Return:

        The DataFrame with a new column appended, where the new column name is formed by appending '_feature' to the original column name.
        """

        df[column + '_feature'] = df[column].apply(func)
        return df
