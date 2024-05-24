import pandas as pd
from datetime import datetime


class DateTimeHandeler:
    @staticmethod
    def calculate_years_passed(dataframe, column):
        """
        Calculates the time passed in years from dates in the specified column.

        Parameters: 
        dataframe (pd.DataFrame) : The DataFrame containing the data.
        column (str) : The name of the column with date values.

        Raises: 
        ValueError : If the column does not exist in the DataFrame.
        TypeError:If the column is not of datetime type.
        """

        dataframe[column] = pd.to_datetime(dataframe[column])
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        
        if not pd.api.types.is_datetime64_any_dtype(dataframe[column]):
            raise TypeError(f"Column '{column}' is not of datetime type.")

        current_date = datetime.now()
        new_column_name = f"Time_passed_since_{column}"
        
        def calculate_time_passed(date):
            if pd.isnull(date):
                return None
            delta = current_date - date
            years = delta.days // 365
            months = (delta.days % 365) // 30
            
            if years > 0:
                if months > 0:
                    return f"{years} years and {months} months"
                else:
                    return f"{years} years"
            elif months > 0:
                return f"{months} months"
            else:
                return "less than a month"

        dataframe[new_column_name] = dataframe[column].apply(calculate_time_passed)