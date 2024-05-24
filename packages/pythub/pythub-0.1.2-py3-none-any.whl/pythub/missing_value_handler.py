import pandas as pd
from typing import List, Union, Any
import numpy as np



class MissingValueHandler:
    
    @staticmethod
    def replace_value(df: pd.DataFrame, value: Any) -> pd.DataFrame:
        """
        Replace all possible missing values in the DataFrame with a specified value.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        value (Any): The value to replace missing values with.

        Returns:
        pd.DataFrame: The DataFrame with missing values replaced.
        """
        missing_values = [None, pd.NA, pd.NaT, 'NA', 'N/A', 'n/a', 'na', 'NaN', 'nan', 'null', 'Null', '', '/N', '\\N', np.nan]
        return df.replace(missing_values, value)


    @staticmethod
    def impute_mean(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Impute missing values in specified columns with the mean of the column.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to impute.

        Returns:
        pd.DataFrame: The DataFrame with imputed values.
        """
        for col in columns:
            if col in df.columns:
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                print(f"Column '{col}' not found in DataFrame. Skipping imputation.")
        return df

    @staticmethod
    def impute_median(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Impute missing values in specified columns with the median of the column.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to impute.

        Returns:
        pd.DataFrame: The DataFrame with imputed values.
        """
        for col in columns:
            if col in df.columns:
                df[col].fillna(df[col].median(), inplace=True)
            else:
                print(f"Column '{col}' not found in DataFrame. Skipping imputation.")
        return df


    @staticmethod
    def impute_constant(df: pd.DataFrame, columns: List[str], value: Any) -> pd.DataFrame:
        """
        Impute missing values in specified columns with a constant value.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to impute.
        value (Any): The constant value to impute.

        Returns:
        pd.DataFrame: The DataFrame with imputed values.
        """
        for col in columns:
            if col in df.columns:
                df[col].fillna(value, inplace=True)
            else:
                print(f"Column '{col}' not found in DataFrame. Skipping imputation.")
        return df


    @staticmethod
    def delete_missing(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Delete rows with missing values in specified columns.

        Parameters:
        df (pd.DataFrame): The DataFrame to process.
        columns (List[str]): List of column names to check for missing values.

        Returns:
        pd.DataFrame: The DataFrame with rows containing missing values removed.
        """
        return df.dropna(subset=columns)

    @staticmethod
    def get_rows_with_missing_data(df, column):
        """
        Finds rows with missing data in the specified column.

        Parameters:
        df (pd.DataFrame): The DataFrame to check for missing data.
        column (str): The column name to check for missing data.

        Returns:
        pd.DataFrame: A DataFrame containing rows with missing data in the specified column.

        Note: column name should be passed as string "column_name" not ["column_name"]
        """
        if column in df.columns:
            missing_values = [None, pd.NA, pd.NaT, 'NA', 'N/A', 'n/a', 'na', 'NaN', 'nan', 'null', 'Null', '', '/N', '\\N', np.nan]
            return df[df[column].isin(missing_values)]
        else:
            print(f"Column '{column}' not found in DataFrame.")
            return pd.DataFrame()  # Return an empty DataFrame if the column is not found




    