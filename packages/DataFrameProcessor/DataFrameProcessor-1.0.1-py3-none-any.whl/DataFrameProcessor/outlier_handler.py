import pandas as pd 

class OutlierHandler:
    @staticmethod
    def get_bounds(df, column):
        """
        Calculate the lower and upper bounds for outliers in a numeric column using the IQR method.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column for which to calculate the bounds.

        Returns:
        tuple: A tuple containing the lower and upper bounds.
        
        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        TypeError: If the specified column is not numeric.
        """

        if column not in df.columns:
            raise ValueError(f"The Column '{column}' does not exist in this DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(f"The Column '{column}' is not numeric and cannot be used for outlier detection.")
        
        Q1 = df[column].quantile(0.30)
        Q3 = df[column].quantile(0.70)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return lower_bound, upper_bound

    @staticmethod
    def detect_outliers(df, column):
        """
        Detect and print outliers in a numeric column.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to check for outliers.
        """

        if column not in df.columns:
            raise ValueError(f"The Column '{column}' does not exist in this DataFrame.")
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(f"The Column '{column}' is not numeric and cannot be used for outlier detection.")

        lower_bound , upper_bound = OutlierHandler.get_bounds(df,column)
        outliers = df.loc[(df[column] < lower_bound) | (df[column] > upper_bound)]
        return outliers
        
    @staticmethod
    def remove_outliers(dataframe, column):
        """
        Remove outliers from a DataFrame based on a specific column.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to use for outlier removal.
        
        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        TypeError: If the specified column is not numeric.
        """

        if column not in dataframe.columns:
            raise ValueError(f"The Column '{column}' does not exist in this DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"The Column '{column}' is not numeric and cannot be used for outlier removal.")
        Q1 = dataframe[column].quantile(0.30)
        Q3 = dataframe[column].quantile(0.70)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        dataframe.drop(dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)].index, inplace=True)

    @staticmethod
    def modify_outliers(dataframe, column, outlier_value): 
        """
        Modify outliers in a DataFrame based on a specific column by replacing them with a specified value.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to use for outlier modification.
        outlier_value: The value to replace outliers with.
        
        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        TypeError: If the specified column is not numeric.
        """
        if column not in dataframe.columns:
            raise ValueError(f"The Column '{column}' does not exist in this DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"The Column '{column}' is not numeric and cannot be used for outlier modification.")
        Q1 = dataframe[column].quantile(0.30)
        Q3 = dataframe[column].quantile(0.70)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers_index = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)].index
        dataframe.loc[outliers_index, column] = outlier_value
