import matplotlib.pyplot as plt
import pandas
import seaborn

path=input("Enter the path of the csv file with two backslashes: ")
column=input("Enter the column name to be ploted: ")
df=pandas.read_csv(path)
seaborn.countplot(x=column,data=df)
plt.show()