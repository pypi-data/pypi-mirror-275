import pandas as pd
from sklearn.preprocessing import LabelEncoder   

class CategoricalEncoder:
    @staticmethod
    def hot_encode(dataframe, columns):
        """
        One-hot encode categorical columns in a DataFrame.

        Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the columns to encode.
        columns (list): A list of column names to one-hot encode.

        Returns:
        pandas.DataFrame: The DataFrame with one-hot encoded categorical columns.
        """
        return pd.get_dummies(dataframe, columns=columns)

    @staticmethod
    def label_encoder(dataframe, columns):
        """
        Encode categorical columns in a DataFrame using LabelEncoder.

        Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the columns to encode.
        columns (list): A list of column names to encode.
        """
        labelEncoder = LabelEncoder()
        for column in columns:
            dataframe[column] = labelEncoder.fit_transform(dataframe[column])