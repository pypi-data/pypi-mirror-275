import matplotlib.pyplot as plt
import seaborn as sns

def visualize_missing_values(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.show()

def visualize_outliers(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, orient='h')
    plt.title('Boxplot for Outlier Detection')
    plt.show()
