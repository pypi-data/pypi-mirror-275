from enum import Enum 
import pandas as pd
import datetime
from typing import Union, Any

class MissingValueHandler:
    def __init__(self, const_int: int = 0, const_str: str = "NA", const_date: datetime.datetime = datetime.datetime(day=1, month=1, year=2024)):
        self.const_int = const_int
        self.const_str = const_str
        self.const_date = const_date

    class Strategy(Enum):
        MEAN = 1
        MEDIAN = 2
        CONSTANT = 3
        REMOVE_ROW = 4
        REMOVE_COLUMN = 5
        FORWARD_BACKWARD = 6

    def replace_missing_values(self, dataframe: pd.DataFrame, strategy: 'MissingValueHandler.Strategy' = Strategy.MEAN, column: Union[int, str] = 0) -> pd.DataFrame:
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        if strategy == self.Strategy.MEAN:
            return self.replace_mean(dataframe, column)
        elif strategy == self.Strategy.MEDIAN:
            return self.replace_median(dataframe, column)
        elif strategy == self.Strategy.CONSTANT:
            return self.replace_constant(dataframe, column)
        elif strategy == self.Strategy.REMOVE_ROW:
            return self.replace_remove_row(dataframe, column)
        elif strategy == self.Strategy.REMOVE_COLUMN:
            return self.replace_remove_column(dataframe, column)
        elif strategy == self.Strategy.FORWARD_BACKWARD:
            return self.replace_forward_backward(dataframe, column)
        else:
            raise ValueError("Invalid strategy")

    def replace_mean(self, dataframe: pd.DataFrame, column: Union[int, str]) -> pd.DataFrame:
        df_copy = dataframe.copy()
        if pd.api.types.is_numeric_dtype(df_copy[column]):
            mean_value = df_copy[column].mean()
            df_copy[column].fillna(mean_value, inplace=True)
        else:
            raise ValueError(f"Column '{column}' is not numeric. Skipping mean replacement...")
        return df_copy

    def replace_median(self, dataframe: pd.DataFrame, column: Union[int, str]) -> pd.DataFrame:
        df_copy = dataframe.copy()
        if pd.api.types.is_numeric_dtype(df_copy[column]):
            median_value = df_copy[column].median()
            df_copy[column].fillna(median_value, inplace=True)
        else:
            raise ValueError(f"Column '{column}' is not numeric. Skipping median replacement.")
        return df_copy

    def replace_constant(self, dataframe: pd.DataFrame, column: Union[int, str]) -> pd.DataFrame:
        df_copy = dataframe.copy()
        if pd.api.types.is_numeric_dtype(df_copy[column]):
            const_value = self.const_int
        elif pd.api.types.is_string_dtype(df_copy[column]):
            const_value = self.const_str
        elif pd.api.types.is_datetime64_any_dtype(df_copy[column]):
            const_value = self.const_date
        else:
            raise ValueError(f"Unsupported column type for column '{column}'")

        df_copy[column].fillna(const_value, inplace=True)
        return df_copy

    def replace_remove_row(self, dataframe: pd.DataFrame, column: Union[int, str]) -> pd.DataFrame:
        df_copy = dataframe.copy()
        return df_copy.dropna(subset=[column])

    def replace_remove_column(self, dataframe: pd.DataFrame, column: Union[int, str]) -> pd.DataFrame:
        df_copy = dataframe.copy()
        return df_copy.drop(columns=[column])

    def replace_forward_backward(self, dataframe: pd.DataFrame, column: Union[int, str]) -> pd.DataFrame:
        df_copy = dataframe.copy()
        df_copy[column].fillna(method='ffill', inplace=True)
        df_copy[column].fillna(method='bfill', inplace=True)
        return df_copy