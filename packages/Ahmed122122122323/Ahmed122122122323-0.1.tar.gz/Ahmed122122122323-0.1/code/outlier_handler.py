import numpy as np


class OutlierHandler:
    @staticmethod
    def iqr_outliers(df, column, threshold=1.5):

        """
        detect and handle outliers in a specific column of a DataFrame using the Interquartile Range (IQR) method.

        Parameters:
        df: The DataFrame containing the data.
        column: The specific column of the DataFrame in which outliers are to be detected.
        threshold (optional): The multiplier for the IQR to define the bounds for detecting outliers. The default value is 1.5.

        Return the Filtered DataFrame:
        The method returns a DataFrame that 'Excludes' the outliers based on the IQR method.

        """
        if column in df.columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        else:
            print(f"Column '{column}' not found in DataFrame.")
            return df  # Return the original DataFrame if the column is not found

