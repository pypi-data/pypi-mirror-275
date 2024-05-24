import pandas as pd

class DataFrameModifier:
    @staticmethod
    def delete_column(df, column):
        """
        Deletes a column from the DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame from which the column will be deleted.
        column (str): The name of the column to delete.

        Returns:
        pd.DataFrame: The DataFrame with the specified column deleted.

        Note: column name should be passed as string "column_name" not ["column_name"]
        """
        if column in df.columns:
            del df[column]
            return df
        else:
            print(f"Column '{column}' not found in DataFrame.")
            return df
