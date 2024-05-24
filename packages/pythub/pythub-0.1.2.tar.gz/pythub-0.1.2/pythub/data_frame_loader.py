import pandas as pd


class DataFrameLoader:
    @staticmethod
    def read_csv(file_path, **kwargs):
        """
        Reads a CSV file and returns a pandas DataFrame.

        Parameters:
        file_path (str): The path to the CSV file.
        **kwargs: Additional arguments to pass to pandas.read_csv().

        Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
        """
        return pd.read_csv(file_path, **kwargs)
