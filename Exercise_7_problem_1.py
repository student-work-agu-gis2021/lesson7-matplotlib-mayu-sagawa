#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: Simple scatter plot using random 
# 
# We can generate random numbers using using a method `random.rand()` from the [NumPy package](https://numpy.org/). This example generates 10 random values:
# 
# ```
# import numpy as np
# random_numbers = np.random.rand(10)
# 
# ```
# 
# ### Part 1
# 
# Create an new data frame called `data` and add 1000 random numbers (`float`) into a new column `x` and another 1000 random numbers (`float`) into a new column `y`.

import numpy as np
import pandas as pd

# YOUR CODE HERE 1 to set data
# Create 1000 random numbers
x = np.random.rand(1000)
y = np.random.rand(1000)
# Create an new data frame called data
data = pd.DataFrame(zip(x,y), columns=['x','y'])

# Check your random values
print(data.head())

# Check that you have the correct number of rows
assert len(data) == 1000, "There should be 1000 rows of data."


# ### Part 2
# 

# YOUR CODE HERE 2 to set colors
#Create a variable colors.
colors = tuple(np.random.choice(range(256),size=1000))
# This test print should print out 10 first numbers in the variable colors
print(colors[0:10])

# Check that the length matches
assert len(colors) == 1000, "There should be 1000 random numbers for colors"


# ### Part 3 
# 
# #### Part 3.1
# 
# Create a scatter plot of points with random colors
# 
# #### Part 3.2
# 
# #### Part 3.3
# 

# Plot a scatter plot
# YOUR CODE HERE 3
#Create a scatter plot with random colors
DataFrame = data.plot(x='x', y='y',kind='scatter',
                      s = 50, c = colors,
                      colormap = 'jet', 
                      edgecolor = 'black')
#Plot a scatter plot
DataFrame.plot()

# Add labels and title
# YOUR CODE HERE 4
#Create variables title, xlabel and ylabel
title = "My random candy points"
xlabel = "X-label"
ylabel = "Y-labe"
#create matplotlib.pyplot method
import matplotlib.pyplot as plt
#add the title and labels to the figure
plt.title(title)
plt.xlabel(xlabel,size=10)
plt.ylabel(ylabel,size=10)

# Save the plot as a png file:
outputfp = "my_first_plot.png"

# YOUR CODE HERE 5
#save my plot as a PNG file
plt.savefig('my_first_plot.png')

# This test print statement should print the output filename of your figure
print("Saved my first plot as:", outputfp)

#Check that the file exists (also go and open the file to check that everything is ok!)
import os

assert os.path.exists(outputfp), "Can't find the output image."


# Remember to commit your changes (including the image file) to your GitHub repo!
# 
# ### Done!
# 
# Now you can move to [problem 2](Exercise-7-problem-2.ipynb).
