import pandas as pd

def generate_report(original_df, cleaned_df, logs, file_path):
    with open(file_path, 'w') as f:
        f.write("Data Cleaning Report\n")
        f.write("===================\n\n")
        f.write("Original Data Description:\n")
        f.write(str(original_df.describe()) + "\n\n")
        f.write("Cleaned Data Description:\n")
        f.write(str(cleaned_df.describe()) + "\n\n")
        f.write("Cleaning Logs:\n")
        for log in logs:
            f.write(log + "\n")
