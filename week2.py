import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
A = np.array([[2, 3, 4], [5, 6, 7]])
B = np.array([[4, 5, 6], [7, 8, 9]])

vertical_stack = np.vstack((A, B))

horizontal_stack = np.hstack((A, B))

common_elements = np.intersect1d(A, B)

lower_bound = 5
upper_bound = 10
filtered_values = A[(A >= lower_bound) & (A < upper_bound)]
indices = np.where((A >= lower_bound) & (A < upper_bound))
values_using_where = A[indices]
filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]

print("Array A:\n", A)
print("Array B:\n", B)
print("Vertically Stacked Array:\n", vertical_stack)
print("Horizontally Stacked Array:\n", horizontal_stack)
print("Common elements:\n", common_elements)
print("Within a range:\n", indices)
print("Within a range using np.where:\n", values_using_where)
print("Filtered rows:\n", filtered_rows)


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df = df.iloc[::20, :][['Manufacturer', 'Model', 'Type']]
print(filtered_df)

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df['Min.Price'] = df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price'] = df['Max.Price'].fillna(df['Max.Price'].mean())
print(df[['Min.Price', 'Max.Price']].isnull().sum())

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
filtered_rows = df[df.sum(axis=1) > 100]
print(filtered_rows)