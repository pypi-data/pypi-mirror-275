import pandas as pd 
from .outlier_handler import OutlierHandler as oh
import math

class MissingValueHandler:
    @staticmethod
    def impute_mean(dataframe, column):
        """
        Fills missing values in a numeric column with the mean of non-outlier values.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to impute.
        
        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        TypeError: If the specified column is not numeric.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric and cannot be imputed with mean.")
        
        lower_bound, upper_bound = oh.get_bounds(dataframe, column)
        non_outliers = dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]
        mean_value = math.floor(non_outliers[column].mean())
        dataframe[column] = dataframe[column].fillna(mean_value)


    @staticmethod
    def impute_median(dataframe, column):
        """
        Fills missing values in a numeric column with the median of non-outlier values.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to impute.
        
        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        TypeError: If the specified column is not numeric.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric and cannot be imputed with median.")

        lower_bound, upper_bound = oh.get_bounds(dataframe, column)
        non_outliers = dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]
        dataframe.loc[dataframe[column].isna(),column] = non_outliers[column].median()

    @staticmethod
    def impute_input(dataframe, column, value):
        """
        Fills missing values in a numeric column with a specified value.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to impute.
        value (numeric): The value to use for imputation.
    
        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        TypeError: If the specified column is not numeric.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric and cannot be imputed with median.")
        dataframe.loc[dataframe[column].isna(),column] =value

    @staticmethod
    def remove_missing(dataframe, column = None):
        """
        Removes rows from the DataFrame where the specified column has missing values.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to check for missing values.
        """
        if column:
            if column not in dataframe.columns:
                raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
            dataframe.dropna(subset=[column], inplace=True)
        else :
            dataframe.dropna(inplace = True)