# First import the Python JSON package
import json

student = {"name": "Student A",
    "grades": {
        "lab1": {
            "earned": 9,
            "possible": 12},
        "lab2": {
            "earned": 12,
            "possible": 15},
        "lab3": {
            "earned": 20,
            "possible": 22},
                },
}

#### begin CORRECTION NEEDED
outfile = open('data/test.json','w+') # open the file 'data/test.json' for writing
json.dump(student, outfile, sort_keys = True, indent = 4)
# close the file
#### end CORRECTION NEEDED