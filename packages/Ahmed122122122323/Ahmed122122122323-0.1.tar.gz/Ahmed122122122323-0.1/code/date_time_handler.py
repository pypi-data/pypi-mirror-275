import pandas as pd

class DateTimeHandler:
    @staticmethod
    def to_datetime(df, columns):
        """
        This method converts specified columns in a DataFrame to datetime data types.

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        columns (list) – A list of column names in the DataFrame to be converted to datetime types.
        
        Returns:
        The DataFrame with the specified columns converted to datetime types.
        
        Details:
        The errors='coerce' parameter ensures that any values which cannot be converted to datetime are set to NaT (Not a Time).
        """
        if all(col in df.columns for col in columns):
            for col in columns:
                df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. Conversion to datetime skipped.")
            return df


    @staticmethod
    def extract_date_parts(df, column):

        """
        This method extracts the year, month, and day parts from a datetime column and creates new columns for each part.

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        column (str) – The name of the datetime column from which to extract date parts.

        Returns:
        The DataFrame with new columns for year, month, and day extracted from the specified datetime column.

        Note: column name should be passed as string "column_name" not ["column_name"]
        """

        if column in df.columns:
            # Ensure the column is in datetime format
            df = DateTimeHandler.to_datetime(df, [column])

            # Extract year, month, and day parts
            df[column + '_year'] = df[column].dt.year
            df[column + '_month'] = df[column].dt.month
            df[column + '_day'] = df[column].dt.day
            return df
        else:
            print(f"Column ['{column}'] not found in DataFrame. Date parts extraction skipped.")
            return df
