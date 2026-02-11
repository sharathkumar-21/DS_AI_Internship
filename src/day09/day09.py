

print("Task 1: The Product Catalog (Series Creation & Indexing)")
import pandas as pd

products = pd.Series([700,150,300], index=['laptop', 'mouse', 'keyboard'])
laptop_price = products['laptop']
print("Laptop Price :", laptop_price)
print(products[['laptop','mouse']])
print(products)
print(products[0:2])


import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)