import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
#print(countries[1])
print(countries)

countries = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8,
'I' : 9,'J' : 10,'K' : 11,'L' : 12,'M' : 13,'N' : 14,'O' : 15,'P' : 16,'Q' : 17,'R' : 18,
'S' : 19,'T' : 20,'U' : 21,'V' : 22,'W' : 23,'X' : 24,'Y' : 25,'Z' : 26}

# Start your search algorithm here.
#for country in countries:
user_input = input("Type a country:")
if user_input == item in countries:
    print("Oh! we might be close.")
