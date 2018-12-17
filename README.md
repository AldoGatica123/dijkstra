# Description

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2de3509075bc46a7a1157f226041a18b)](https://app.codacy.com/app/AldoGatica123/dijkstra?utm_source=github.com&utm_medium=referral&utm_content=AldoGatica123/dijkstra&utm_campaign=Badge_Grade_Dashboard)

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
