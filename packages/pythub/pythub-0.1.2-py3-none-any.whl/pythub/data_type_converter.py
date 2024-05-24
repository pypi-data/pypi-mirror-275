import pandas as pd

class DataTypeConverter:
    @staticmethod
    def to_numeric(df, columns):

        """
        This method converts specified columns in a DataFrame to numeric data types (integers or floats).

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        columns (list) – A list of column names in the DataFrame to be converted to numeric types.
        
        Returns:
        The DataFrame with the specified columns converted to numeric types.

        note:
        Uses pd.to_numeric to attempt conversion of each value in the column to a numeric type.
        The errors='coerce' parameter ensures that any values which cannot be converted to numeric types are set to NaN.
        """

        if all(col in df.columns for col in columns):
            for col in columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. Conversion to numeric skipped.")
            return df


    @staticmethod
    def to_categorical(df, columns):

        """
        This method converts specified columns in a DataFrame to categorical data types.

        Parameters:
        df (pandas.DataFrame) – The DataFrame containing the data.
        columns (list) – A list of column names in the DataFrame to be converted to categorical types.
        
        Returns:
        The DataFrame with the specified columns converted to categorical types.
        
        Details:
        Uses astype('category') to convert each column to the pandas category data type.
        This can be useful for columns with a limited number of unique values, such as categorical features in machine learning.
        """

        if all(col in df.columns for col in columns):
            for col in columns:
                df[col] = df[col].astype('category')
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. Conversion to categorical skipped.")
            return df

