# IMPORT STATEMENTS
from csvreader import readcsv, createclasses, createclassarrays
from cleaningarrays import cleaning, floating


# DEMONSTRATION CODE
howhappy, howsatisfied, howsafe, sex, age, income, howbeautiful = readcsv()
print("done1")#debug
income, age, sex = cleaning(income, age, sex)
howbeautiful = floating(howbeautiful)
howhappy = floating(howhappy)
howsafe = floating(howsafe)
howsatisfied = floating(howsatisfied)
print('done2')#debug
incomeandhappy, sexandsafe, ageandhappy, incomeandbeauty = createclassarrays(income, howsafe, age)
print('done3')#debug
incomeandhappy = createclasses(income, howhappy, incomeandhappy)
print('done4')#debug
sexandsafe = createclasses(sex, howsafe, sexandsafe)
ageandhappy = createclasses(age, howhappy, ageandhappy)
incomeandbeauty = createclasses(income, howbeautiful, incomeandbeauty)
print('done5')#debug
'''
normalize(income, howhappy, howsatisfied, howsafe, age)
'''
