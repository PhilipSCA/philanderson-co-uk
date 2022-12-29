import csv

print()
print('Thursday 29th December 2022')
print('Python - Chapter 72  : Saving CSV files 3')
print('==============================================')
print()

with open("file02.csv", "w") as file:
    file.write("")
print("We write some rows of data using x.writerow([])")

with open("file02.csv", "w", newline="") as file02:
    data = csv.writer(file02, delimiter=",")
    data.writerow(["Date", "Name", "Age"])
    data.writerow(["16th Feb", "James", "14"])
    data.writerow(["29th Dec", "John", "17"])


with open("file02.csv",) as file02:
    data_2 = csv.reader(file02)
print(data_2)


'''
Thursday 29th December 2022
Python - Chapter 72  : Saving CSV files 3
==============================================

We write some rows of data using x.writerow([])
<_csv.reader object at 0x000001E9347625E0>
'''