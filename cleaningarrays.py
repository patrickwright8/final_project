

#### FILTERING AND CLEANING ARRAYS




for i in income:
    if i == "Less than $10,000":
        income[i] = 5000
    elif i == "$10,000 to $24,999":
        income[i] = 17500
    elif i == "$25,000 to $49,999":
        income[i] = 37500
    elif i == "$50,000 to $74,000":
        income[i] = 62500
    elif i == "$75,000 to $99,999":
        income[i] = 87500
    elif i == "$100,000 to $149,999":
        income[i] = 125000
    elif i == "$150,000 or more":
        income[i] = 150000
        
        
for i in age:
    
        
        
for i in sex:
    if i == "Male":
        sex[i] = 0
    elif i == "Female":
        sex[i] = 1
    
#Normalizing Arrays from 0 to 1

income = (income-np.min(income))/((np.max(income))-np.min(income))
howhappy = (howhappy-np.min(howhappy))/((np.max(howhappy))-np.min(howhappy))
howsatisfied = (howsatisfied-np.min(howsatisfied))/((np.max(howsatisfied))-np.min(howsatisfied))
howsafe = (howsafe-np.min(howsafe))/((np.max(howsafe))-np.min(howsafe))


    
        
