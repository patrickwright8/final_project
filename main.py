# IMPORT STATEMENTS
from csvreader import readcsv, createclasses, createclassarrays
from cleaningarrays import cleaning, floating, normalize
from clustering import iterate, createinitialcentroids, checkaccuracy
from regression import pandasframe, linearregression, incomehappiness, agehappiness, incomebeauty
import numpy as np

howhappy, howsatisfied, howsafe, sex, age, income, howbeautiful = readcsv()
income, age, sex, howhappy, howsatisfied, howsafe = cleaning(income, age, sex, howhappy, howsatisfied, howsafe)
howbeautiful = floating(howbeautiful)
howhappy = floating(howhappy)
howsafe = floating(howsafe)
howsatisfied = floating(howsatisfied)
incomeandhappy, sexandsafe, ageandhappy, incomeandbeauty = createclassarrays(income, howsafe, age)
incomeandhappy = createclasses(income, howhappy, incomeandhappy)
sexandsafe = createclasses(sex, howsafe, sexandsafe)
ageandhappy = createclasses(age, howhappy, ageandhappy)
incomeandbeauty = createclasses(income, howbeautiful, incomeandbeauty)
# Next two lines of code creates a normalized array of "howsafe" JUST for clustering
howsafe_cluster = normalize(howsafe, sexandsafe)
howsafe_cluster = howsafe_cluster.astype(np.float)
# *** Below is the clustering portion ***
maximum = 999
centroid = createinitialcentroids()
#yarray = generateyarray(howsafe_cluster)
centroid, assignments = iterate(maximum, centroid, sex, howsafe_cluster)
percentage = checkaccuracy(assignments, sex, centroid)
print('Histogram generated with centroids', centroid[0], 'and', centroid[1])
print('Accuracy of', percentage, '%')
print('*** Linreg Below ***')
# *** Below is the linreg portion ***
income, age, sex, howhappy, howsatisfied, howsafe = cleaning(income, age, sex, howhappy, howsatisfied, howsafe)
df = pandasframe(income, age, sex, howhappy, howsatisfied, howsafe, howbeautiful)
incomehappiness(df)
#agehappiness(df)
#incomebeauty(df)

# **** IMPORTANT NOTE ****
# in order to visualize a plot for the linear regression portion, the other two must be commented out. 
