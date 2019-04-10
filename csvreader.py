'''
Csv Reader
Author: Patrick Wright
'''

import csv
import numpy as np
import time #Debug

def readcsv():
    howhappy = np.array([]) # Array of blood glucose
    howsatisfied = np.array([]) # Array of hemoglobin
    income = np.array([]) # Array of Class
    age = np.array([])
    howsafe = np.array([])
    sex = np.array([])
    with open('survey.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            howhappy = np.append(howhappy, row[2])
            howsatisfied = np.append(howsatisfied, row[3])
            howsafe = np.append(howsafe, row[22])
            sex = np.append(sex, row[26])
            age = np.append(age, row[28])
            income = np.append(income, row[38])
    howhappy = np.delete(howhappy, 0)
    howsatisfied = np.delete(howsatisfied, 0)
    howsafe = np.delete(howsafe, 0)
    sex = np.delete(sex, 0)
    age = np.delete(age, 0)
    income = np.delete(income, 0)
    return howhappy, howsatisfied, howsafe, sex, age, income

howhappy, howsatisfied, howsafe, sex, age, income = readcsv()

for index in range(len(howhappy)-1):
    try: 
        howhappy[index] = float(howhappy[index])
    except:
        print(howhappy[index], "at", index, " could not be converted to a float. Deleting...")
        howhappy = np.delete(howhappy, index)
        time.sleep(0.05)
        index = index-1