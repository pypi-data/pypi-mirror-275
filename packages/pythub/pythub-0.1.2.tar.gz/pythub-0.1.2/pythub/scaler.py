from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Scaler:
    @staticmethod
    def standard_scale(df, columns):

        """
        The specified columns in the DataFrame are scaled using StandardScaler,
        which standardizes features by removing the mean and scaling to unit variance.
        then the scaler is fitted to the data and then transforms it.
        
        Parameters:
        df: The DataFrame containing the data.
        columns: A list of column names in the DataFrame to be scaled.

        Return:
        The scaled DataFrame is returned, with the specified columns standardized.
        """
        if all(col in df.columns for col in columns):
            scaler = StandardScaler()
            df[columns] = scaler.fit_transform(df[columns])
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. Standard scaling skipped.")
            return df


    @staticmethod
    def minmax_scale(df, columns):

        """
        The specified columns in the DataFrame are scaled using MinMaxScaler,
        which transforms specified columns by scaling each one to a given range (default is 0 to 1).
        then the scaler is fitted to the data and then transforms it.
        

        Parameters:
        df: The DataFrame containing the data.
        columns: A list of column names in the DataFrame to be scaled.
        
        
        Return:
        The scaled DataFrame is returned, with the specified columns scaled to the range [0, 1].

        """

        if all(col in df.columns for col in columns):
            scaler = MinMaxScaler()
            df[columns] = scaler.fit_transform(df[columns])
            return df
        else:
            missing_columns = [col for col in columns if col not in df.columns]
            print(f"Columns {missing_columns} not found in DataFrame. MinMax scaling skipped.")
            return df

