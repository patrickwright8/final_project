import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns; sns.set(color_codes=True) #Seaborn is imported to be able to plot the data with nan values

#######
# The following code requires that income, age, sex, howhappy, howsatisfied and howsafe have already been defined as numpy
# arrays and cleaned through the cleaning.py function.

def pandasframe(income, age, sex, howhappy, howsatisfied, howsafe, howbeautiful): #Puts data in a pandas dataframe, changes all data to floats and changes blank data to 'nan' values
    df = pd.DataFrame({'income':income, 'age':age, 'sex':sex , 'howhappy':howhappy, 'howsatisfied':howsatisfied, 'howsafe':howsafe, 'howbeautiful':howbeautiful})
    df["income"] = pd.to_numeric(df.income, errors='coerce')
    df["age"] = pd.to_numeric(df.age, errors='coerce')
    df["howhappy"] = pd.to_numeric(df.howhappy, errors='coerce')
    df["sex"] = pd.to_numeric(df.sex, errors='coerce')
    df["howsatisfied"] = pd.to_numeric(df.howsatisfied, errors='coerce')
    df["howsafe"] = pd.to_numeric(df.howsafe, errors='coerce')
    df["howbeautiful"] = pd.to_numeric(df.howbeautiful, errors='coerce')
    return df

#df = pandasframe() #calling function, add to driver

def incomehappiness(df): #Returns numeric values for slope and intercept, plots scatter plot and regression line 
    X = df.income 
    Y = df.howhappy
    mask = ~np.isnan(X) & ~np.isnan(Y) #Creates a mask to ignore nan (not a number) values to perform regression
    linregstats = stats.linregress(X[mask], Y[mask])
    slope = linregstats[0]
    intercept = linregstats[1]
    sns.regplot(x="income", y="howhappy", data=df, scatter_kws={'s':0.1}).set_title("Income vs Happiness for Somerville") #plots regression
    print("Slope = " + str(slope)) 
    print("y-intercept = " + str(intercept))
   

def agehappiness(df): #Returns numeric values for slope and intercept, plots scatter plot and regression line 
    X = df.age 
    Y = df.howhappy
    mask = ~np.isnan(X) & ~np.isnan(Y) #Creates a mask to ignore nan (not a number) values to perform regression
    linregstats = stats.linregress(X[mask], Y[mask])
    slope = linregstats[0]
    intercept = linregstats[1]
    sns.regplot(x="age", y="howhappy", data=df, scatter_kws={'s':0.1}).set_title("Age vs Happiness for Somerville") #plots regression
    print("Slope = " + str(slope)) 
    print("y-intercept = " + str(intercept))
  

def incomebeauty(df): #Returns numeric values for slope and intercept, plots scatter plot and regression line 
    X = df.income 
    Y = df.howbeautiful
    mask = ~np.isnan(X) & ~np.isnan(Y) #Creates a mask to ignore nan (not a number) values to perform regression
    linregstats = stats.linregress(X[mask], Y[mask])
    slope = linregstats[0]
    intercept = linregstats[1]
    sns.regplot(x="income", y="howbeautiful", data=df, scatter_kws={'s':0.1}).set_title("Income vs Perception of Neighborhood Beauty for Somerville") #plots regression
    print("Slope = " + str(slope)) 
    print("y-intercept = " + str(intercept))
    

    
#linearregression()  #calling function, add to driver  

