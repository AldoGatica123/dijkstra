import csv
import sys
from collections import defaultdict
from heapq import *

import flask
from flask import Flask
from flask import send_from_directory


app = Flask(__name__, static_folder='static')


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory(app.static_folder, filename)


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen = [(0, f, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return float("inf")


@app.route("/airport/<code>")
def airport(code):
    with open('airports.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['LocationID'] == code:
                return flask.jsonify(row)

    return flask.jsonify(None)


@app.route("/search/<search>")
def search(search):
    results = []
    with open('airports.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if search.upper() in row['LocationID']:
                results.append(row)
                if len(results) == 10:  # Max of 10 results
                    return flask.jsonify(results)

    return flask.jsonify(results)


@app.route("/route/<origin>/<destination>/<int:_range>")
def route(origin, destination, _range):
    items_count = 4515
    row_index = 0

    edges = []
    with open('airports-distance.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_index += 1
            if row_index % 100 == 0:
                print("Creating graph for range " + str(_range) + "... " + str(
                    round((row_index / items_count) * 100, 2)) + "%", file=sys.stderr)
            for code in row:
                if code != 'id' and float(row[code]) < _range:
                    edges.append((row['id'], code, float(row[code])))

    print("Calculating Route from " + origin + " to " + destination + " for range " + str(_range) + " miles...",
          file=sys.stderr)
    rt = dijkstra(edges, origin, destination)

    print("Route from " + origin + " to " + destination + " for range " + str(_range) + " miles.", file=sys.stderr)

    return flask.jsonify(rt)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, threaded=True)
