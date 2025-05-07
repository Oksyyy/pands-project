# Programming And Scripting
by Oksana Abrosimova

This repository contains Progect materials related to the **Programming And Sripting** study module. To demonstrate learning and understanding of the core Python concepts learned throughout the programm, the analysis.py program was written providing analysis of the famous Iris data set.

## Dataset
Data that forms the foundation of the Iris dataset was originally collected by Edgar Anderson, an American botanist, likely between 1928 and 1935. It was later published in 1936, by Ronald A. Fisher, a British mathematician, statistician and biologist in his article *"The Use of Multiple Measurements in Taxonomic Problems"*,. The paper explored how measurements could be used to distinguish classes between species and highlighted the importance of accuracy in those measurements.

Despite its simplicity, the dataset has remained widely used in data science, machine learning, and statistical analyses to this day. Its popularity can be attributed to several factors: a small and clear structure, class component, a set of petal a sepal measures. These characteristics make it ideal for learning, testing statistical models and experimenting with classification techniques. 

At a high level, the Iris dataset contains measurements of three Iris flower species. 

It includes 150 rows and 5 columns: 
- Four columns hold numerical measurements of flower features:
    - sepal length (cm)
    - sepal width (cm)
    - petal length (cm) 
    - petal width (cm)
- The fifth column contains categorical data representing the class (species) of each flower: Setosa, Versicolor, Virginica.

Each row in the dataset represents one flower sample, showing its four measurements and a corresponding species. There are 50 samples per each Iris species.

## Dataset Source
>Fisher, R. (1936). Iris [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.

## Required Software

- Python - Programming language required to run the code. Download from [Python.org](https://www.python.org/downloads/).
- Jupyter - An environment for writing and running code, exploring, analysing and visualising data. For installation refer to [Jupiter documenation](https://docs.jupyter.org/en/stable/install.html).
- Codespaces (alternative to Jupyter) -  A cloud-based development environment provided by GitHub that allows running Jupyter Notebooks. Available in the repository under "Code" drop-down menu. 

## Required Packages

All necessary packages are imported and explained within the notebook. Here's a quick overview:

- [pandas](https://pandas.pydata.org/docs/index.html): used to load the Iris dataset into a Pandas DataFrame.
- [numpy](https://numpy.org/doc/stable/): used for numerical operations and data array manipulations.
- [matplotlib.pyplot](https://matplotlib.org/): used for creating plots and visualisations.
- [seaborn](https://seaborn.pydata.org/index.html): used for creating plots and visualisations.
- [itertools.combinations](https://docs.python.org/3/library/itertools.html): used to generate all possible pairs of features for plotting and analysis.