import pandas as pd

class Search:
    @staticmethod
    def search_value(dataframe, value, column=None):
        """
        Search for rows that contain the specified value in any column or in a specified column.

        Parameters:
        dataframe (pd.DataFrame) : The DataFrame to search in.
        value (str) : The value to search for.
        column (str) , optional : The name of the column to search in. If None, search in all columns.

        Returns:
        pd.DataFrame
            A DataFrame containing rows that match the search criteria.

        Raises:
        ValueError: If the specified column does not exist in the DataFrame.    
        """
        if column:
            if column not in dataframe.columns:
                raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
            return dataframe[dataframe[column].astype(str).str.contains(value, case=False, na=False)]
        else:
            return dataframe[dataframe.astype(str).apply(lambda x: x.str.contains(value, case=False, na=False)).any(axis=1)]
    
    @staticmethod
    def remove_value(dataframe, value, column=None):
        """
        Remove rows that contain the specified value in any column or in a specified column.

        Parameters:
        dataframe (pd.DataFrame) : The DataFrame to search in.
        value (str) : The value to search for.
        column (str), optional : The name of the column to search in. If None, search in all columns.

        Raises:
        ValueError: If the specified column does not exist in the DataFrame.
        """
        if column:
            if column not in dataframe.columns:
                raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
            dataframe.drop(dataframe[dataframe[column].astype(str).str.contains(value, case=False, na=False)].index, inplace=True)
        else:
            dataframe.drop(dataframe[dataframe.astype(str).apply(lambda x: x.str.contains(value, case=False, na=False)).any(axis=1)].index, inplace=True)
            

    @staticmethod
    def search_numeric_range(dataframe, column, min_value, max_value):
        """
        Search for rows where the specified numeric column's values fall within the given range.

        Parameters:
        dataframe (pd.DataFrame) : The DataFrame to search in.
        column (str) : The name of the numeric column to search in.
        min_value (float) : The minimum value of the range.
        max_value (float) : The maximum value of the range.

        Returns (pd.DataFrame) : A DataFrame containing rows that match the search criteria.

        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not of numeric type.
        """
        
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")
        
        return dataframe[(dataframe[column] >= min_value) & (dataframe[column] <= max_value)]        