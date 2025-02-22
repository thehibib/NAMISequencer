import json
data = None
with open ('rawdata.txt', 'r') as file:
    data = json.load(file)
newdata = []
for entry in data:
    if "NAMI National Resource Directory as of January" in entry:
        pass
    else:
        newdata.append(entry)

with open ('newdata.txt', 'w') as file:
    json.dump(newdata, file)