import csv
from math import sin, cos, sqrt, atan2, radians

coordinates = {}
earth_radius = 3959.0

with open('airports.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        coordinates[row['LocationID']] = [row['Latitude'], row['Longitude']]
fieldnames = ['id']

for code in coordinates:
    fieldnames.append(code)

with open('airports-distance.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()
    row_index = 0

    for code in coordinates:
        lat1 = radians(float(coordinates[code][0]))
        lon1 = radians(float(coordinates[code][1]))
        row = {'id': code}
        if row_index % 10 == 0:
            print("Processing " + str(row_index) + " of " + str(len(coordinates)) + " airports.")
        row_index += 1

        # Selects the destination airport, then calculates the distance between it and the origin using the distance over sphere based on the latitude and longitude.
        for code2 in coordinates:
            lat2 = radians(float(coordinates[code2][0]))
            lon2 = radians(float(coordinates[code2][1]))
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = earth_radius * c

            row[code2] = round(distance, 2)
        writer.writerow(row)