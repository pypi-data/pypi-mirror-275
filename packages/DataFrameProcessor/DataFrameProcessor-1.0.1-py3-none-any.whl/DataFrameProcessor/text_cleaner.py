import pandas as pd
from nltk.corpus import stopwords


class TextCleaner:

    @staticmethod
    def to_lowercase(dataframe, column):
        """
        Converts all text in the specified column to lowercase.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to convert to lowercase.
        
        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not of string type.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if dataframe[column].dtype != object:
            raise TypeError(f"Column '{column}' does not contain string values.")
        
        dataframe[column] = dataframe[column].str.lower()

    @staticmethod
    def to_uppercase(dataframe, column):
        """
        Converts all text in the specified column to uppercase.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to convert to uppercase.
        
        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not of string type.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if dataframe[column].dtype != object:
            raise TypeError(f"Column '{column}' does not contain string values.")
        
        dataframe[column] = dataframe[column].str.upper()    

    @staticmethod
    def to_titlecase(dataframe, column):
        """
        Converts all text in the specified column to title case.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to convert to title case.
        
        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not of string type.
        """     
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if dataframe[column].dtype != object:
            raise TypeError(f"Column '{column}' does not contain string values.")
        
        dataframe[column] = dataframe[column].str.title()    

    @staticmethod
    def remove_stopwords(dataframe, column):
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if dataframe[column].dtype != object:
            raise TypeError(f"Column '{column}' does not contain string values.")
        
        stop_words = set(stopwords.words('english'))
        dataframe[column] = dataframe[column].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]) if pd.notnull(x) else x) 

    @staticmethod
    def strip_whitespace(dataframe, column):
        """
        Removes leading and trailing whitespace and reduces multiple spaces to a single space in text in the specified column.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to strip whitespace from.
        
        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not of string type.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if dataframe[column].dtype != object:
            raise TypeError(f"Column '{column}' does not contain string values.")
        
        dataframe[column] = dataframe[column].str.strip().str.replace(r"\s+", " ", regex=True)

    @staticmethod
    def replace_text(dataframe, column, to_replace, replacement):
        """
        Replaces all occurrence of a specific String in the specified column with another string.
        
        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to replace text in.
        to_replace (str): The text to replace.
        replacement (str): The text to replace with.
        
        Raises:
        ValueError: If the column does not exist in the DataFrame.
        TypeError: If the column is not of string type.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if dataframe[column].dtype != object:
            raise TypeError(f"Column '{column}' does not contain string values.")
        if to_replace not in dataframe[column].unique():
            print(f"Warning: '{to_replace}' not found in column '{column}'. No replacements were made.")
            return
        dataframe[column] = dataframe[column].str.replace(to_replace, replacement)    