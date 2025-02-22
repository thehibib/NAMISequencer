import json
data = None 
with open ('newdata.txt', 'r') as file:
    data = json.load(file)
print(data[174])
    