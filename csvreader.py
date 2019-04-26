'''
Csv Reader
Author: Patrick Wright
'''

import csv
import numpy as np

def readcsv():
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

'''
Even though these functions will just be imported to a driver, 
if you read perform the functions in top-->bottom order, this should be
where the cleaning functions are run. (because they have to be run before )
'''



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



'''
***Notes***
Correlations:
    income (x axis) and happiness (y axis)
    sex and how safe they feel (clustering where male and female is the classification and howsafe is x AND y axis
    age (x axis) and happiness (y axis)
    income (x axis) and how satisfied with beauty of neighborhood (y axis)
    
    
***Old Code***
while index < len(howhappy):
    try:
        howhappy[index] = float(howhappy[index])
        howsatisfied[index] = float(howsatisfied[index])
        howsafe[index] = float(howsafe[index])
        index = index + 1
    except:
        howhappy = np.delete(howhappy, index)
        howsatisfied = np.delete(howsatisfied, index)
        howsafe = np.delete(howsafe, index)
howhappy = howhappy.astype(np.float)
howsatisfied = howsatisfied.astype(np.float)
howsafe = howsafe.astype(np.float)

'''