import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations as comb

# Import the dataset
iris_df = pd.read_csv("iris.data", sep=',', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Assign the list of features (columns) to a variable to be used further inside various functions as part of our analysis
features = iris_df.columns

"""
Write a function that takes a list of features and returns a string with summary statistics for each feature.
"""
def summary_stats(features):
    # Initialize a string with a title for the function to append the summary of each feature 
    summary_string = "IRIS DATASET FEATURE SUMMARY\n\n"

    # Iterate through each feature (column) in the list of features using a for loop
    for column in features:

        # Since the function performs certain calculations based on the column data type defined within the if/elif blocks, use try-except to handle any potential data type errors
        try:

            # We know that Iris dataset contains numerical and categorical data
            # We can check the data type of each column using the if function and the dtype attribute
            if iris_df[column].dtype == 'float64':
                
                # For numerical data, use pandas.DataFrame functions to calculate summary statistics: mean, median, standard deviation, min, and max
                mean = iris_df[column].mean()
                median = iris_df[column].median()
                st_dev = iris_df[column].std()
                min = iris_df[column].min()
                max = iris_df[column].max() 

                # Create a summary string for the numerical feature using f-string formatting 
                feature_summary = (f'{column}\n\n'
                            f'Mean:\t\t{mean:.2f}\n'
                            f'Median:\t\t{median:.2f}\n'
                            f'Std Dev:\t{st_dev:.2f}\n' 
                            f'Min:\t\t{min:.2f}\n' 
                            f'Max:\t\t{max:.2f}')
                
            # Using elif instead of else to give the function a different instruction for a specific data type 
            elif iris_df[column].dtype == 'object':

                # For categorical data we use pandas.Series functions to describe unique classes and values frequency within each class
                unique_class = iris_df[column].unique()
                frequency = iris_df[column].value_counts()  
                
                # Create a summary string for the categorical feature using f-string formatting
                feature_summary = (f'{column}\n\n'
                            f'Unique Classes:\t{unique_class}\n'
                            f'Value Frequency:\n{frequency}')

            # Append the summary string for each feature to the summary_string variable
            summary_string += feature_summary + "\n\n"
        
        # The except block is executed if an error occurs in the try block
        except:
            feature_summary = (f'{column}\n\n'
                 f"Summary could not be created for {column} due to unsupported data type {iris_df[column].dtype}")
            
            # Append the alert string to the summary_string variable
            summary_string += feature_summary + "\n\n"
    
    # Return the summary_string variable containing the summary for all features
    return summary_string 

# Call the summary_stats function to store the summary statistics output
summary_output = summary_stats(features)

# Print the summary output
print(summary_output)

# Initiate a variable to store the summary statistics in a text file
filename = 'summary.txt'

# Open the file in write mode using the with statement
with open(filename,'w') as f:
    # Call the summary_stats function that outputs the summary for each feature into the file
    f.write(summary_output)

"""
Write a function that takes a list of features, generates a histogram for each feature and saves it into a .png file
"""
def feature_hist(features):

    # Create a list of colors to be used for histograms
    colors = ['blue', 'green', 'red', 'orange', 'purple']
    
    # Set a for loop to iterate through:
    #   1. Each color from the "colors" list defined above,
    #   2. Eeach feature (column) in the list of features defined outside the function
    for i, column in enumerate(features):

        # Use try-except to handle any potential errors
        try:

            # Check the data type of each column using the if function and the dtype attribute
            if iris_df[column].dtype == 'float64':

                # Initiate an empty figure as a placeholder for each feature histogram
                plt.figure() 

                # Create variable "color" to pass it as an argument to the histogram 
                color = colors[i % len(colors)]

                # Use Matplotlib to plot a histogram 
                plt.hist(iris_df[column], color = color, bins=20, edgecolor = 'gray')

                # Set axes labels using xlabel() and ylabel() functions
                plt.xlabel(f"{column} (cm)")
                plt.ylabel('Frequency')

                # Add title
                plt.title(f"Histogram of {column}")

                # The savefig() function saves the plot to a file as ".png"
                plt.savefig(f'Hist_{column}.png')

                # Show the plot
                plt.show()
            
            elif iris_df[column].dtype == 'object':

                # Initiate an empty figure
                plt.figure()

                # Plot a different histogram for categorical data
                plt.hist(iris_df[column], color = 'purple', edgecolor = 'gray')

                # Set axes labels using xlabel() and ylabel() functions
                plt.xlabel(f'{column}')
                plt.ylabel('Frequency')

                # Add title 
                plt.title('Iris Species')
                
                # Save file as ".png"
                plt.savefig(f'Hist_{column}.png')

                # Show the plot         
                plt.show()   

                # Close the plot
                plt.close()       
       
        # The except block is executed if an error occurs in the try block
        except:
            print(f'Histogram could not be created for feature {column} due to unsupported data type {iris_df[column].dtype}')

# Call the feature_hist function and pass the features variable to it
feature_hist(features)

"""
Write a function that takes a list of features and returns a scatter plot for each pair of features. 
This function will handle only numerical features and will skip any non-numerical to keep analysis forcusing on useful insights
"""
def feature_scatter_basic(features):

    # Set a for loop to iterate through:
    #   1. Each pair of features (columns) in the list of features defined outside the function
    for x, y in comb(features, 2):

        # Check the data type of each column using the if function and the dtype attribute
        # If data type is not float64, skip the iteration using continue statement
        if iris_df[x].dtype != 'float64' or iris_df[y].dtype != 'float64':
            continue
        
        # Initiate an empty figure as a placeholder for each scatter plot
        plt.figure() 

        # Create a scatter plot 
        sns.scatterplot(data=iris_df, x = x, y = y, hue='class', marker='v')

        # Set axes labels 
        plt.xlabel(f'{x} (cm)')
        plt.ylabel(f'{y} (cm)')

        # Add title
        plt.title(f'{x} vs {y} relationship')

        # Show the plot
        plt.show() 

        # Close the plot
        plt.close()

# Call the feature_scatter_basic function and pass the features variable to it
feature_scatter_basic(features)

"""
Add a regression line to the the scatter plots created as part of feature_scatter() function
"""
def feature_scatter_with_regression(features):

    # Set a for loop to iterate through:
    #   1. Each pair of features (columns) in the list of features defined outside the function
    for x, y in comb(features, 2):

        # Check the data type of each column using the if function and the dtype attribute
        # If data type is not float64, skip the iteration using continue statement
        if iris_df[x].dtype != 'float64' or iris_df[y].dtype != 'float64':
            continue
        
        # Initiate an empty figure as a placeholder for each scatter plot
        plt.figure() 

        # Calculate the slope (m) and intercept (c) of the linear regression line using numpy's polyfit function
        m,c = np.polyfit(iris_df[x], iris_df[y], 1)

        # Print the slope and intercept values for the respective feature pair
        # Use f-string formatting for readable output 
        print(f"Linear regression for {x} vs {y}:\nSlope (m):\t{m}\nIntercept (c):\t{c}\n\n")

        # Create a scatter plot 
        sns.scatterplot(data=iris_df, x = x, y = y, hue='class', marker='v')

        # Set axes labels 
        plt.xlabel(f'{x} (cm)')
        plt.ylabel(f'{y} (cm)')

        # Fit the regression line
        plt.plot(iris_df[x], m * iris_df[x] + c, color = 'red', label = 'Regression line')

        # Add legend
        plt.legend()

        # Add title
        plt.title(f'{x} vs {y} relationship')

        # The savefig() function saves the plot to a file as ".png"
        plt.savefig(f'Scatter {x} vs {y}.png') 
        
        # Show the plot
        plt.show()

        # Close the plot
        plt.close()

# Call the feature_scatter_with_regression function and pass the features variable to it
feature_scatter_with_regression(features)

"""
Calculate Correlations
"""
# Use the corr() function to calculate the correlation matrix
# Pass the method as 'pearson' and set numeric_only to True to include only numerical columns
corr_matrix = iris_df.corr('pearson', numeric_only=True)

# Print the correlation matrix
print(f'Correlation matrix:\n\n{corr_matrix}')

"""
Create a heatmap to visualize the correlation matrix
"""
# Plot figure and axes using the subplots() function
fig, ax = plt.subplots()

# Set x & y axes labels
labels = corr_matrix.columns

# Generate a heatmap using matplotlib imshow() function
# Use cmap='PRGn' to set plot colors for better interpretation of results
ax.imshow(corr_matrix, cmap='PRGn')

# Set custom ticks and label them with the respective feature names
ax.set_xticks(range(len(labels)), labels=labels, rotation=45, ha="right")
ax.set_yticks(range(len(labels)), labels=labels)

# Loop over data dimensions and create text annotations
for i in range(len(labels)):
    for j in range(len(labels)):
        # Use the text() function to add text annotations to the heatmap
        # Use the iloc[] function to access the correlation values in the matrix
        text = ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                       ha="center", va="center", color="w")
# Set title
ax.set_title("Correlation between Iris features ")

# Show the plot
plt.show()

# Close the plot
plt.close()