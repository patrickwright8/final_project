By Patrick Wright and Andres Hernandez

INSTRUCTIONS TO PERFORM DATA ANALYSIS:

Simply run main.py. Delete the comments at the bottom to display the different graphs (if there are no comments, all 3 graphs will display at once.

OVERVIEW OF PROGRAMS AND FUNCTIONS

main.py - Driver; contains no functions


csvreader.py - CSV reader that extracts data from survey.csv

Contains functions:

  -readcsv
    Simple CSV reader that reads survey.csv
 
 -createclassarray
	
    Creates a "class" array in order to perform clustering/linreg.
    This is a large data set so some people leave answers blank and fill in others.
    This function just creates a number of empty arrays the same size as the ones being classified
  
  -createclasses
	
    This function returns a class array that is 1 if both values of the two arrays at a given index are floatable 
    and 0 if they are not.
clustering.py - Contains functions for k-means clustering algorithm

  Functions are individually commented explaining what they do, but the gist is that:
	
    1. 2 random centroids are created from [0,1].
    2. The points in the "howsafe" array are assigned to the nearest centroid.
    3. The location of the centroid changes to the mean of all its constituent points.
    4. Steps 2 and 3 are repeated many many times.
    
    
    
    
 cleaningarrays.py - Cleans survey data by changing the survey brackets into float values
 
 Contains functions:
 	
   ~cleaningarrays - changes individual survey brackets (ex. "$10,000 to $24,000" to float value (ex. 19,000.0) in order to facilitate analysis.
   
   ~normalize - normalizes arrays for clustering purposes
   
   
 regression.py - puts arrays into pandas dataframe and then performs regression on three relationships. Contains global pandas dataframe creation.
 
  Contains functions:
  
  ~incomehappiness - performs regression for income vs happiness
  ~agehappiness - performs regression on age and happiness
  ~incomebeauty - performs regression on income and howbeautiful
    
    

