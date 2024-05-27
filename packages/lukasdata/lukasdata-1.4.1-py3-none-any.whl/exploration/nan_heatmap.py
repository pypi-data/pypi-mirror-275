import matplotlib.pyplot as plt
import seaborn as sns
def nan_heatmap(df,title="NaN Values"):

    plt.figure(figsize=(20, 10))

    # Create a heatmap to visualize NaNs
    sns.heatmap(df.isna(), cbar=False, cmap='viridis', yticklabels=False)

    # Show the plot
    plt.title(title)
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.show()

