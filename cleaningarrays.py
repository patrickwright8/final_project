import numpy as np

#### FILTERING AND CLEANING ARRAYS



def cleaning(income, age, sex, howhappy, howsatisfied, howsafe): 
    income[income == 'Less than $10,000'] = 5000.0
    income[income == '$10,000 to $24,999'] = 17500.0
    income[income == "$25,000 to $49,999"] = 37500.0
    income[income == "$50,000 to $74,999"] = 62500.0
    income[income == "$75,000 to $99,999"] = 87500.0
    income[income == "$100,000 to $149,999"] = 125000.0
    income[income == "$150,000 or more"] = 150000.0
    income[income == "40,000 - $49,999"] = 45000.0
    income[income == "70,000 - $79,999"] = 75000.0
    income[income == "10,000 - $19,999"] = 15000.0
    income[income == "50,000 - $59,999"] = 55000.0
    income[income == "20,000 - $29,999"] = 25000.0
    income[income == "30,000 - $39,999"] = 35000.0
    income[income == "60,000 - $69,999"] = 65000.0
    income[income == "80,000 - $89,999"] = 85000.0
    income[income == "90,000 - $99,999"] = 95000.0
    income[income == "100,000 and up"] = 100000.0
    age[age == "18-24"] = 21.0
    age[age == "25-34"] = 29.5
    age[age == "35-44"] = 39.5
    age[age == "45-54"] = 49.5
    age[age == "55-64"] = 59.5
    age[age == "65-74"] = 69.5
    age[age == "75 or older"] = 75.0
    age[age == "26-30"] = 28.0
    age[age == "61+"] = 61.0
    age[age == "22-25"] = 23.5
    age[age == "41-50"] = 45.5
    age[age == "31-40"] = 35.5
    age[age == "51-60"] = 55.5
    age[age == "18-21"] = 19.5
    sex[sex == "Male"] = 0.0
    sex[sex == "Female"] = 1.0
    sex[sex == 'Female, Male'] = ''
    howhappy[1857] = ''
    howhappy[535] = ''
    howhappy[1338] = ''
    howhappy[2463] = ''
    howhappy[3769] = ''  
    return income, age, sex, howhappy, howsatisfied, howsafe
    
    
def floating(floatarray):
    for i in range(len(floatarray)):
        try:
            floatarray[i] = float(floatarray[i])
        except:
            floatarray[i] = floatarray[i]
    return floatarray
    

#Normalizing Arrays from 0 to 1

def normalize(howsafe, sexandsafe):          #income, howhappy, howsatisfied, howsafe, age):
    '''
    income = (income-np.min(income))/((np.max(income))-np.min(income))
    howhappy = (howhappy-np.min(howhappy))/((np.max(howhappy))-np.min(howhappy))
    howsatisfied = (howsatisfied-np.min(howsatisfied))/((np.max(howsatisfied))-np.min(howsatisfied))
    '''
    howsafe[sexandsafe==1] = (howsafe[sexandsafe==1]-np.min(howsafe[sexandsafe==1]))/((np.max(howsafe[sexandsafe==1]))-np.min(howsafe[sexandsafe==1]))
    #age = (age-np.min(age))/((np.max(age))-np.min(age))
    #return income, howhappy, howsatisfied, howsafe, age
    return howsafe[sexandsafe==1]

    
        
