import seaborn
import pandas
import matplotlib.pyplot as plt
 
csv = pandas.read_csv(r'C:\\Users\\Abaan\\Documents\\titanic.csv')
print(csv.head())
print(csv.tail())
print(csv.index)
print(csv.columns)
print(csv.shape)
seaborn.countplot(x="Survived", data=csv)
plt.show()




#csv.head() used for printing the first 5 rows 
#csv.tail() used for printing the last 5 rows 
#csv.index used for total no of records
#csv.columns used to print all column headings 
#csv.shape used to get the number of columns and rows (Rows,Columns)