import pandas as pd
from .utils import fill_missing, remove_duplicates, detect_and_handle_outliers, convert_data_types, standardize_features
from .visualization import visualize_missing_values, visualize_outliers
from .reporting import generate_report

class DataCleaningAssistant:
    def __init__(self, df):
        self.df = df.copy()
        self.cleaned_df = df.copy()
        self.logs = []

    def fill_missing_values(self, strategy='median'):
        self.cleaned_df = fill_missing(self.cleaned_df, strategy)
        self.logs.append(f'Filled missing values using {strategy} strategy.')

    def remove_duplicates(self):
        self.cleaned_df = remove_duplicates(self.cleaned_df)
        self.logs.append('Removed duplicate rows.')

    def detect_and_handle_outliers(self, method='IQR'):
        self.cleaned_df = detect_and_handle_outliers(self.cleaned_df, method)
        self.logs.append(f'Handled outliers using {method} method.')

    def convert_data_types(self):
        self.cleaned_df = convert_data_types(self.cleaned_df)
        self.logs.append('Converted data types.')

    def standardize_features(self):
        self.cleaned_df = standardize_features(self.cleaned_df)
        self.logs.append('Standardized features.')

    def generate_report(self, file_path):
        generate_report(self.df, self.cleaned_df, self.logs, file_path)

    def visualize_missing_values(self):
        visualize_missing_values(self.cleaned_df)

    def visualize_outliers(self):
        visualize_outliers(self.cleaned_df)

    def get_cleaned_data(self):
        return self.cleaned_df
