from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


class CategoricalEncoder:
    @staticmethod
    def one_hot_encode(df, columns):
        """
        This method applies one-hot encoding to specified columns in a DataFrame.

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        columns (list) – A list of column names in the DataFrame to be one-hot encoded.
        
        Returns:
        The DataFrame with the specified columns replaced by their one-hot encoded versions.
        
        Note:
        One-hot encoding converts categorical values into a set of binary (0 or 1) columns, where each column represents a unique category.
        """
        if all(col in df.columns for col in columns):
            encoder = OneHotEncoder(sparse_output=False)
            encoded_columns = encoder.fit_transform(df[columns])
            df = df.drop(columns, axis=1)
            df = df.join(pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(columns)))
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. One-hot encoding skipped.")
            return df



    @staticmethod
    def label_encode(df, columns):

        """
        This method applies label encoding to specified columns in a DataFrame.

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        columns (list) – A list of column names in the DataFrame to be label encoded.
        
        Returns:
        The DataFrame with the specified columns label encoded.
        
        Details:
        Label encoding converts each category value in a column to a unique integer.

        """
        if all(col in df.columns for col in columns):
            encoder = LabelEncoder()
            for col in columns:
                df[col] = encoder.fit_transform(df[col])
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. Label encoding skipped.")
            return df
