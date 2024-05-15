import pandas

# pip install pandas

data = pandas.read_csv('records.csv', delimiter=";")
print(data)
#         name branch  year  cgpa
# 0      radek    coe     3   9.1
# 1      tomek    cos     2  19.1
# 2      zenek    cot     4   9.1
# 3  Krzysztof    cor     1  11.0
print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['radek' 'coe' 3 9.1]
#  ['tomek' 'cos' 2 19.1]
#  ['zenek' 'cot' 4 9.1]
#  ['Krzysztof' 'cor' 1 11.0]]
print(data.items)
# <bound method DataFrame.items of         name branch  year  cgpa
# 0      radek    coe     3   9.1
# 1      tomek    cos     2  19.1
# 2      zenek    cot     4   9.1
# 3  Krzysztof    cor     1  11.0>
