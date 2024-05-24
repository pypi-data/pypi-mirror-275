import pandas as pd
import numpy as np

class Scaler:
    """Mathematical Operations class"""
    @staticmethod
    def addition(dataframe, column, value):
        """
        Add a specified value to each element in the specified numeric column.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform addition on.
        value: The value to add to each element in the column.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
        """

        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column] + value

    @staticmethod
    def add_percentage(dataframe, column, percentage):
        """
        Add a percentage to each element in the specified column.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform addition on.
        percentage (float): The percentage to add to each element in the column.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
        """ 

        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column] * (1 + percentage / 100)

    @staticmethod
    def subtract(dataframe, column, value):
        """
        Subtract a specified value from each element in the specified column.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform subtraction on.
        value: The value to subtract from each element in the column.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
        """

        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column] - value

    @staticmethod
    def subtract_percentage(dataframe, column, percentage):
        """
        Subtract a percentage from each element in the specified column.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform subtraction on.
        percentage (float): The percentage to subtract from each element in the column.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
        """

        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column] * (1 - percentage / 100)


    @staticmethod
    def multiply(dataframe, column, value):
        """
        Multiply each element in the specified column by a given value.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform multiplication on.
        value: The value to multiply each element in the column by.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
        """

        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column] * value    

    @staticmethod
    def divide(dataframe, column, value , rounding = None):
        """
        Divide the values in the specified column by a given value with optional rounding.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform the division on.
        value (float): The value to divide each element in the column by.
        rounding (str, optional): Specifies the rounding method. Can be 'floor', 'round', or 'ceil'.
                                  If None, the result will not be rounded. Default is None.
        
        Raises:
        ValueError: If the column does not exist in the DataFrame or if value is zero.
        TypeError: If the column is not numeric.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = dataframe[column] / value
        if rounding:
            rounding = rounding.lower()
            if rounding == 'floor':
                result = np.floor(result)
            elif rounding == 'round':
                result = np.round(result)
            elif rounding == 'ceil':
                result = np.ceil(result)
        
        dataframe[column] = result

    @staticmethod
    def power(dataframe, column, exponent):
        """
        Raise each element in the specified column to a given exponent.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to perform exponentiation on.
        exponent: The exponent to raise each element in the column to.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not numeric.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        dataframe[column] = dataframe[column] ** exponent  