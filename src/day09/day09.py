

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


marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])















print("task-2,grade filter")
import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
null_values = grades.isnull()
filled_series = grades.fillna(0)
filtered_results = grades[grades > 60]
print(f'Original Series : \n{grades}\n')
print(f'Filled Series : \n{filled_series}\n')
print(f'Filtered Results : \n{filtered_results}\n')





















print("task-3,username formatter")

import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames.str.strip())
print(usernames.str.lower())
print(usernames.str.contains('a'))
print(f'Cleaned Series : \n{usernames.str.lower()}\n')
print(f' boolean result of the a search : \n{usernames.str.contains('a')}')








