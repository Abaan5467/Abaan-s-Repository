import matplotlib.pyplot as plt
import pandas
import seaborn

path=input("Enter the path of the csv file with two backslashes: ")
column=input("Enter the column name to be ploted: ")
h = input("Enter the hue or n to skip this: ")
df=pandas.read_csv(path)

if h=='n':
    seaborn.countplot(x=column,data=df)
    plt.show()
else:
    seaborn.countplot(x=column,hue=h,data=df)
    plt.show()