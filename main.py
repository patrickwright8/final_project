# IMPORT STATEMENTS
from csvreader import readcsv, createclasses, createclassarrays
from cleaningarrays import clean #, normalize


# DEMONSTRATION CODE
howhappy, howsatisfied, howsafe, sex, age, income, howbeautiful = readcsv()
print("done1")#debug
income, age, sex = clean(income, age, sex)
print('done2')#debug
incomeandhappy, sexandsafe, ageandhappy, incomeandbeauty = createclassarrays(income, sex, age)
print('done3')#debug
incomeandhappy = createclasses(income, howhappy, incomeandhappy)
print('done4')
'''
sexandsafe = createclasses(sex, howsafe, sexandsafe)
ageandhappy = createclasses(age, howhappy, ageandhappy)
incomeandbeauty = createclasses(income, howbeautiful, incomeandbeauty)
normalize(income, howhappy, howsatisfied, howsafe, age)
'''
