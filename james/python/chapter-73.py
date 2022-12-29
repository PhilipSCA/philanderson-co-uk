import csv

print()
print('Thursday 29th December 2022')
print('Python - Chapter 73 : Appending rows to CSV files')
print('==============================================')
print()

print("When you use 'a' instead of 'w' or 'r' in the file opening the code, it will append new data.")
with open("file02.csv", "a", newline="") as file02:
    data = csv.writer(file02)
    data.writerow(["Date", "Name", "Age"])
    data.writerow(["16th Feb", "James", "14"])
    data.writerow(["29th Dec", "John", "17"])