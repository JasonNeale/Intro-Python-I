"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""
import json

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
# 43.593404" N, 83.88855" W
waypoints.append({
    "lat": 43.593404,
    "lon": 83.88855,
    "name": "Bay City, Michigan"
})

print("\n")
print(json.dumps(waypoints, indent=4))

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
for waypoint in waypoints:
    if waypoint["name"] == "a place":
        waypoint["lon"] = -130
        waypoint["name"] = 'not a real place'

print("\n")
print(json.dumps(waypoints, indent=4))

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for waypoints in waypoints:
    print("\n")
    print(waypoint["lat"])
    print(waypoint["lon"])
    print(waypoint["name"])