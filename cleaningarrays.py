

#### FILTERING AND CLEANING ARRAYS




for i in income:
    if i == "Less than $10,000":
        income[i] = 5000.0
    elif i == "$10,000 to $24,999":
        income[i] = 17500.0
    elif i == "$25,000 to $49,999":
        income[i] = 37500.0
    elif i == "$50,000 to $74,000":
        income[i] = 62500.0
    elif i == "$75,000 to $99,999":
        income[i] = 87500.0
    elif i == "$100,000 to $149,999":
        income[i] = 125000.0
    elif i == "$150,000 or more":
        income[i] = 150000.0
    elif i == "40,000 - $49,999":
        income[i] = 45000.0
    elif i == "70,000 - $79,999":
        income[i] = 75000.0
    elif i == "10,000 - $19,999":
        income[i] = 15000.0
    elif i == "50,000 - $59,999":
        income[i] = 55000.0
    elif i == "20,000 - $29,999":
        income[i] = 25000.0
    elif i == "30,000 - $39,999":
        income[i] = 35000.0
    elif i == "60,000 - $69,999":
        income[i] = 65000.0
    elif i == "80,000 - $89,999"
        income[i] = 85000.0
    elif i == "90,000 - $99,999"
        income[i] = 95000.0
    elif i == "100,000 and up":
        income[i] = 100000.0






    
    
for i in age:
    if i == "18-24":
        age[i] = 21.0
    elif i == "25-34":
        age[i] = 29.5
    elif i == "35-44":
        age[i] = 39.5
    elif i == "45-54":
        age[i] = 49.5
    elif i == "55-64":
        age[i] = 59.5
    elif i == "65-74":
        age[i] = 69.5
    elif i == "75 or older":
        age[i] = 75.0
    elif i == "26-30":
        age[i] = 28.0
    elif i == "61+":
        age[i] = 61.0
    elif i == "22-25":
        age[i] = 23.5
    elif i == "41-50":
        age[i] = 45.5
    elif i == "31-40":
        age[i] = 35.5
    elif i == "51-60":
        age[i] = 55.5
    elif i == "18-21":
        age[i] = 19.5
        
        
    
    
        
        
for i in sex:
    if i == "Male":
        sex[i] = 0
    elif i == "Female":
        sex[i] = 1
    
#Normalizing Arrays from 0 to 1

def normalize(income, howhappy, howsatisfied, howsafe, age):
    income = (income-np.min(income))/((np.max(income))-np.min(income))
    howhappy = (howhappy-np.min(howhappy))/((np.max(howhappy))-np.min(howhappy))
    howsatisfied = (howsatisfied-np.min(howsatisfied))/((np.max(howsatisfied))-np.min(howsatisfied))
    howsafe = (howsafe-np.min(howsafe))/((np.max(howsafe))-np.min(howsafe))
    age = (age-np.min(age))/((np.max(age))-np.min(age))
    return income, howhappy, howsatisfied, howsafe, age


    
        
