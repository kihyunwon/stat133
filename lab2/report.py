import json

infile = open('data/test.json')# open the file 'data/test.json'
student = json.load(infile)
# close infile

name = student['name']
grades = student['grades']

print "." * 70
print name, "got a", grades['lab1']['earned'], "out of", grades['lab1']['possible'], "on lab1"
print name, "got a", grades['lab2']['earned'], "out of", grades['lab1']['possible'], "on lab2"
print name, "got a", grades['lab3']['earned'], "out of", grades['lab1']['possible'], "on lab3"