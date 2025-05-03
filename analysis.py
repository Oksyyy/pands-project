import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations as comb

# Pass the file name when calling pandas read_csv() function
# Specifing separator is optional in this case as pandas automatically detects commas
# The file doesn't include a header row as confirmed by checking the original data source
# Column names were manually assigned based on iris.names metadata file
iris_df = pd.read_csv("iris.data", sep=',', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

"""
Write a function that takes a list of features and returns a string with summary statistics for each feature.
"""
def summary_stats(features):
    # Initialize an empty string for the function to append the summary of each feature 
    summary_string = ""

    # Iterate through each feature (column) in the list of features using a for loop
    # Feature names are stored in the variable "features" defined outside the function
    for column in features:

        # Since the function performs certain calculations based on the column data type defined within the if/elif blocks, use try-except to handle any potential data type errors
        # The try block contains the code that might raise an error
        try:

            # We know that Iris dataset contains numerical and categorical data
            # We can check the data type of each column using the if function and the dtype attribute
            # [] is used to access the column in the dataframe
            if iris_df[column].dtype == 'float64':
                
                # For numerical data, use pandas.DataFrame functions to calculate summary statistics: mean, median, standard deviation, min, and max
                mean = iris_df[column].mean()
                median = iris_df[column].median()
                st_dev = iris_df[column].std()
                min = iris_df[column].min()
                max = iris_df[column].max() 

                # Create a summary string for the numerical feature using f-string formatting 
                # To dynamically create the string we pass the column name in the first line followed by the calculated statistics values
                # The \n character is used to create a new line in the string for readability 
                # The \t character is used to create a tab space in the string - it allows to align calculated values so the output looks neat
                feature_summary = (f'{column}\n\n'
                            f'Mean:\t\t{mean}\n'
                            f'Median:\t\t{median}\n'
                            f'Std Dev:\t{st_dev}\n' 
                            f'Min:\t\t{min}\n' 
                            f'Max:\t\t{max}')
                
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
            # Add two new lines to separate each feature summary for readability
            summary_string += feature_summary + "\n\n"
        
        # The except block is executed if an error occurs in the try block
        # It outputs a alert string if the program encounterred any other data type other than float64 or object
        except:
            feature_summary = (f'{column}\n\n'
                 f"Summary could not be created for {column} due to unsupported data type {iris_df[column].dtype}")
            
            # Append the alert string to the summary_string variable
            summary_string += feature_summary + "\n\n"
    
    # Return the summary_string variable containing the summary for all features
    return summary_string 
    
# Assign the list of features (columns) to a variable to be used inside the summary stats function
features = iris_df.columns

# Call the summary_stats function and pass the features variable to it
summary_stats(features)

# Initiate a variable to store the summary statistics in a text file
filename = 'summary.txt'

# Open the file in write mode using the with statement
with open(filename,'w') as f:
    # Call the summary_stats function that outputs the summary for each feature into the file
    f.write(summary_stats(features))

"""
Write a function that takes a list of features, generates a histogram for each feature and saves it into a .png file
"""
def feature_hist(features):

    # Create a list of colors to be used for histograms
    # This allows to set a different color for each feature histogram to make them visually distinct
    colors = ['blue', 'green', 'red', 'orange', 'purple']
    
    # Set a for loop to iterate through:
    #   1. Each color from the "colors" list defined above,
    #   2. Eeach feature (column) in the list of features defined outside the function
    # Use the enumerate() function to add a counter along with feature names passed through the features variable
    # The enumerate() function returns both the index and the value of each item in the list
    # The counter (or index) is used to select the color from the colors list
    # The feature name (or column) is used to access feature values in the dataframe
    for i, column in enumerate(features):

        # Use try-except to handle any potential errors
        try:

            # Check the data type of each column using the if function and the dtype attribute
            if iris_df[column].dtype == 'float64':

                # Initiate an empty figure as a placeholder for each feature histogram
                # This allows to create a new figure for each histogram and to avoid overlapping histogrmas on the same figure
                plt.figure() 

                # Create variable "color" to pass it as an argument to the histogram 
                # Use counter [i] along with the modulo operator % to select a color from the colors list above
                # The modulo operator % returns the remainder of the division of i by the length of the colors list
                # This allows to cycle through the colors list. The same color can be used for multiple histograms if there are more features than colors
                color = colors[i % len(colors)]

                # Use Matplotlib to plot a histogram 
                # bins is an optional parameter, default = 10
                # The color and edgecolor parameters are used to set the color of the bars and the color of the edges respectively (also optional parameters)
                plt.hist(iris_df[column], color = color, bins=20, edgecolor = 'gray')

                # Set axes labels using xlabel() and ylabel() functions
                # For x axis we use the column name and add a unit of measurement (cm)
                plt.xlabel(f"{column} (cm)")

                # For y axis we use the count of values, i.e. frequency of how many times each flower with a particular measure appears in the dataset
                plt.ylabel('Frequency')

                # Add title
                plt.title(f"Histogram of {column}")

                # The savefig() function saves the plot to a file as ".png"
                plt.savefig(f'Hist_{column}.png')
            
            elif iris_df[column].dtype == 'object':

                # Initiate an empty figure
                plt.figure()

                # Plot a different histogram for categorical data
                plt.hist(iris_df[column], color = 'purple', edgecolor = 'gray')

                # For x axis we use the column name
                plt.xlabel(f'{column}')

                # For y axis we use the count of values, i.e. frequency of how many times each flower appears in the dataset
                plt.ylabel('Frequency')

                # Add title 
                plt.title('Iris Species')
                
                # Save file as ".png"
                plt.savefig(f'Hist_{column}.png')          
       
        # The except block is executed if an error occurs in the try block
        # It outputs a message
        except:
            print(f'Histogram could not be created for feature {column} due to unsupported data type {iris_df[column].dtype}')
    
# Assign the list of features (columns) to a variable to be used inside the summary stats function
features = iris_df.columns

# Call the feature_hist function and pass the features variable to it
feature_hist(features)

"""
Write a function that takes a list of features and returns a scatter plot for each pair of features. 
This function will handle only numerical features and will skip any non-numerical to keep analysis forcusing on useful insights
"""
def feature_scatter(features):

    # Set a for loop to iterate through:
    #   1. Each pair of features (columns) in the list of features defined outside the function
    # Use the itertools.combinations() function to create all possible pairs of features
    # This function was imported at the beginning of the script
    for x, y in comb(features, 2):

        # Check the data type of each column using the if function and the dtype attribute
        # If data type is not float64, skip the iteration using continue statement
        # This also replaces the need for try-except for error handling
        if iris_df[x].dtype != 'float64' or iris_df[y].dtype != 'float64':
            continue
        
        # Initiate an empty figure as a placeholder for each scatter plot
        plt.figure() 

        # Create a scatter plot 
        # Pass iris_df dataframe, x & y combinations
        # "hue" argument automatically maps distinct colors to each unique class value
        # "marker" sets the data points to triangle shapes
        sns.scatterplot(data=iris_df, x = x, y = y, hue='class', marker='v')

        # Set axes labels 
        plt.xlabel(f'{x} (cm)')
        plt.ylabel(f'{y} (cm)')

        # Add title
        plt.title(f'{x} vs {y} relationship')

        # The savefig() function saves the plot to a file as ".png"
        plt.savefig(f'Scatter_{x} vs {y}.png') 
    
# Assign the list of features (columns) to a variable to be used inside the summary stats function
features = iris_df.columns 

# Call the feature_scatter function and pass the features variable to it
feature_scatter(features)
