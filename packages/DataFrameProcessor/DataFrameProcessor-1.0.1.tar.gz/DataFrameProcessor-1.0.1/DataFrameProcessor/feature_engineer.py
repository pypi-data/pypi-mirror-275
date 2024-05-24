import pandas as pd

class FeatureEngineer:
    @staticmethod
    def create_interaction_features(dataframe, new_faeture_name , feature1, feature2 , replace = False):
        """
        Create interaction features by multiplying two specified numeric features element-wise.

        Parameters:
        data (pd.DataFrame): The DataFrame containing the data.
        feature1 (str): The name of the first feature.
        feature2 (str): The name of the second feature.

        Returns:
        interaction_feature (pd.Series): The interaction feature.

        Raises:
        ValueError: If either of the specified features does not exist in the DataFrame,
        or if either of the specified features is not numeric.
        """
        if feature1 not in dataframe.columns:
            raise ValueError(f"'{feature1}' column does not exist in the DataFrame.")
        if feature2 not in dataframe.columns:
            raise ValueError(f"'{feature2}' column does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[feature1]):
            raise ValueError(f"'{feature1}' column must be numerical.")
        if not pd.api.types.is_numeric_dtype(dataframe[feature2]):
            raise ValueError(f"'{feature2}' column must be numerical.")
        
        interaction_feature = dataframe[feature1] * dataframe[feature2]
        dataframe[new_faeture_name] = interaction_feature
        if replace:
            dataframe.drop(columns=[feature1, feature2], inplace=True)

    @staticmethod
    def sum_numeric_columns(dataframe, new_feature_name, *columns , replace=False):
        
        """
        Sum specified numeric columns and store the result in a new column.

        Parameters:
        dataframe (pd.DataFrame) : The DataFrame containing the data.
        new_feature_name (str) : The name of the new feature to be created.
        replace (bool) optional : if set to True, the original columns will be removed from the DataFrame after creating the new feature.
        columns (str) : The names of the columns to be summed.

        Raises:
        ValueError: If any of the specified columns do not exist in the DataFrame, or if any of the specified columns are not numeric.
        """
        
        for column in columns:
            if column not in dataframe.columns:
                raise ValueError(f"'{column}' column does not exist in the DataFrame.")
            if not pd.api.types.is_numeric_dtype(dataframe[column]):
                raise ValueError(f"'{column}' column must be numerical.")

        dataframe[new_feature_name] = dataframe[list(columns)].sum(axis=1)

        if replace:
            dataframe.drop(columns=list(columns), inplace=True)


    def create_string_interaction_features(dataframe, new_feature_name, feature1, feature2, replace = False):
        """
        Create interaction features by concatenating two specified string columns into one column

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        feature1 (str): The name of the first feature.
        feature2 (str): The name of the second feature.
        new_feature_name (str): The name of the new feature.

        Raises:
        ValueError: If either of the specified features does not exist in the DataFrame,
                    or if either of the specified features is not a string.
        """
        if feature1 not in dataframe.columns:
            raise ValueError(f"'{feature1}' column does not exist in the DataFrame.")
        if feature2 not in dataframe.columns:
            raise ValueError(f"'{feature2}' column does not exist in the DataFrame.")
        if dataframe[feature1].dtype != object:
            raise TypeError(f"Column '{feature1}' does not contain string values.")
        if dataframe[feature2].dtype != object:
            raise TypeError(f"Column '{feature2}' does not contain string values.")
        
        interaction_feature = dataframe[feature1] + " " + dataframe[feature2]
        dataframe[new_feature_name] = interaction_feature    
        if replace:
            dataframe.drop(columns=[feature1, feature2], inplace=True)

    @staticmethod
    def convert_scientific_notation(dataframe , column):
        """
        Convert values in the specified column from scientific notation to standard decimal notation.

        Parameters:
        dataframe (pd.DataFrame) : The DataFrame containing the data.
        column (str) : The name of the column with values in scientific notation.

        Raises:
        ValueError : If the column does not exist in the DataFrame.
        TypeError : If the column is not of numeric type.
        """
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not numeric.")

        dataframe[column] = dataframe[column].apply(lambda x: "{:,.0f}".format(x))        

