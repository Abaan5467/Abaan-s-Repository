import seaborn
import pandas
import matplotlib.pyplot as plt
 
df = pandas.read_csv("C:\\Users\\Abaan\\Documents\\titanic.csv")
seaborn.countplot(x="Survived",data=df)
plt.show()




'''
res = seaborn.FacetGrid(csv, col="Age", col_wrap=3)
res.map(seaborn.barplot, "Age")
plt.show()

violinplot
boxplot
boxenplot
barplot
pointplot
distplot
jointplot
countplot
'''