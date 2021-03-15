import csv;
data_Set1 = []
data_Set2 = []
with open("dataset_1.csv","r") as f:
    reader = csv.reader(f)
    for rows in reader:
        data_Set1.append(rows)
with open("dataset_2_sorted.csv","r") as f:
    reader = csv.reader(f)
    for rows in reader:
        data_Set2.append(rows)
headers_1 = data_Set1[0]
planet_data_1 = data_Set1[1:]
headers_2 = data_Set2[0]
planet_data_2 = data_Set2[1:]
headers = headers_1+headers_2
planet_data = []
for index,data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])
with open("final.csv","a+") as f:
    writer =  csv.writer(f)
    writer.writerow(planet_data)
    writer.writerows(planet_data)
     