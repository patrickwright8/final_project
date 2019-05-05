import numpy as np
import matplotlib.pyplot as plt

def createinitialcentroids():
    return np.random.random((2,))
'''
def generateyarray(howsafe_cluster):
    yarray = np.zeros((len(howsafe_cluster),))
    yarray = yarray + 1
    return yarray
'''
def graphdata(howsafe_cluster, sex, centroid):
    plt.figure()
    plt.hist(howsafe_cluster)
    plt.hist([centroid[0]], color='r')
    plt.hist([centroid[1]], color='green')
    plt.title('Histogram of How Safe one feels at Night')
    plt.xlabel('How safe one feels walking at night')
    plt.ylabel('Number of responses')
    plt.show()
    
def createdistances(howsafe_cluster, centroid):
    distancearray = np.zeros((2, len(howsafe_cluster)))
    for num in range(2):
        distancearray[num] = np.sqrt((howsafe_cluster - centroid[num])**2)
    return distancearray

def assigncentroids(howsafe_cluster, centroid, distancearray):
    assignments = np.zeros(len(howsafe_cluster))
    for number in range(len(howsafe_cluster)):
        assignments[number] = np.argmin(distancearray[:,number])
    return assignments

def update(howsafe_cluster, centroid, assignments):
    new_centroid = np.zeros((2,))
    for number in range(2):
        new_centroid[number] = np.mean(howsafe_cluster[assignments==number])
    return new_centroid

def iterate(maximum, centroid, sex, howsafe_cluster):
    a = 0
    while a < maximum:
        distancearray = createdistances(howsafe_cluster, centroid)
        assignments = assigncentroids(howsafe_cluster, centroid, distancearray)
        centroid = update(howsafe_cluster, centroid, assignments)
        a = a+1
    graphdata(howsafe_cluster, sex, centroid)
    return centroid, assignments

def checkaccuracy(assignments, sex, centroid):
    # sex==1: female; sex==0: male
    # if centroid is numerically ordered, flip assignments
    # if centroid is numerically out of order, leave assignments alone (higher value is centroid[0], male)
    counter = 0
    if centroid[0] > centroid[1]:
        assignments = (assignments-1)**2 # Changes 0s to 1s and  1s to 0s
    for i in range(len(assignments)):
        if assignments[i] == sex[i]:
            counter = counter + 1
    percentage = (counter/len(assignments))*100
    return percentage
    
    
    
    
    
    
    
    
    
    
    
