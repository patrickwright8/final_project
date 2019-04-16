'''
Csv Reader
Author: Patrick Wright
'''

import csv
import numpy as np

def readcsv():
    howhappy = np.array([]) # Array of blood glucose
    howsatisfied = np.array([]) # Array of hemoglobin
    income = np.array([]) # Array of Class
    age = np.array([])
    howsafe = np.array([])
    sex = np.array([])
    howbeautiful = np.array([])
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
incomeandhappy = np.zeros(income)
sexandsafe = np.zeros(howsafe)
ageandhappy = np.zeros(age)
incomeandbeauty = np.zeros(income)
index = 0
while index < len(income):
    try:
        








'''

Correlations:
    income (x axis) and happiness (y axis)
    sex and how safe they feel (clustering where male and female is the classification and howsafe is x AND y axis
    age (x axis) and happiness (y axis)
    income (x axis) and satisfaction of beauty of neighborhood (y axis)
    
    
    

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