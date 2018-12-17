# Description
This project consists in a Flask web application that calculates the shortest path using Dijsktra's algorithm.  
It contains information about US airports.

This project will change its domain.

The base project was taken from [here](https://github.com/theonemule/python-lab)

## Quickstart
First run distance_table.py to generate a csv file containing the distances between all the points of the first csv file.
```commandline
python distance_table.py
```
Then run the web application.
```commandline
python dijkstra.py
```

### csv format for the locations
```csv
LocationID,State,County,City,FacilityName,Latitude,Longitude
```
