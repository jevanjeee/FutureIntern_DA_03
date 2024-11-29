# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
# Load the Iris dataset
IRIS = pd.read_csv('Iris.csv')

# Viewing the first rows of the dataset
print(IRIS.head())

# Viewing the last rows of the dataset
print(IRIS.tail())

# Viewing a random line
print(IRIS.sample())

# Overview of the data
print(IRIS.info())

# Obtaining summary statistics
print(IRIS.describe())

# Excluding the 'Id' column before plotting histograms
IRIS_clean = IRIS.drop(columns=['Id'])

# Plotting the histograms (excluding the 'Id' column)
plt.figure(figsize=(10, 8))  # Set the figure size
IRIS_clean.hist(bins=15, color='skyblue', edgecolor='black')  # Plot histograms without 'Id'
plt.suptitle("Histograms of Iris dataset", fontsize=14)  # Add a title
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit the title

# Show the plot
plt.show()
