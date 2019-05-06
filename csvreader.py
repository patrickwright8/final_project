'''
Csv Reader
Author: Patrick Wright
'''

import csv
import numpy as np

def readcsv():
    # Below stores all the raw data from the csv into 6 numpy arrays
    howhappy = np.array([], dtype=object) 
    howsatisfied = np.array([],dtype=object) 
    income = np.array([],dtype=object) 
    age = np.array([],dtype=object)
    howsafe = np.array([],dtype=object)
    sex = np.array([],dtype=object)
    howbeautiful = np.array([],dtype=object)
    with open('survey.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            howhappy = np.append(howhappy, row[2])
            howsatisfied = np.append(howsatisfied, row[3])
            howsafe = np.append(howsafe, row[22])
            howbeautiful = np.append(howbeautiful, row[23])
            sex = np.append(sex, row[26])
            age = np.append(age, row[28])
            income = np.append(income, row[38])
    howhappy = np.delete(howhappy, 0)
    howsatisfied = np.delete(howsatisfied, 0)
    howsafe = np.delete(howsafe, 0)
    sex = np.delete(sex, 0)
    age = np.delete(age, 0)
    income = np.delete(income, 0)
    howbeautiful = np.delete(howbeautiful, 0)
    return howhappy, howsatisfied, howsafe, sex, age, income, howbeautiful


howhappy, howsatisfied, howsafe, sex, age, income, howbeautiful = readcsv()
# Below creates a "classification" array whose value is 1 if x-array[index] AND y-array[index] both exist
def createclassarrays(income, howsafe, age):
    incomeandhappy = np.zeros(len(income))
    sexandsafe = np.zeros(len(sex))
    ageandhappy = np.zeros(len(age))
    incomeandbeauty = np.zeros(len(income))
    return incomeandhappy, sexandsafe, ageandhappy, incomeandbeauty

def createclasses(array1, array2, classarray):
    index = 0
    while index < len(array1):
        if type(array1[index])==float and type(array2[index])==float:
            classarray[index] = 1
            index = index+1
        else:
            index = index+1
    return classarray
