import os  
import csv
import pandas as pd
import secrets
from geopy.geocoders import Nominatim

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

id = secrets.token_hex(4)
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode(address)

if first_name[-1] == 'a':
    gender = "F"
elif first_name[-1] == 'i':
    gender = "F"
elif first_name[-1] == 'o':
    gender =  "M"
else:
    gender = "M"

rows = [[id, first_name.capitalize(), last_name.capitalize(), gender, age, str(getLoc.address), str(getLoc.latitude), str(getLoc.longitude)]]

with open("cleandata.csv", 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
    

