import MapReduce
import sys

"""
Asymmetric Friendship Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: person's friend
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person + " " + friend, 1)
    mr.emit_intermediate(friend + " " + person, 1)

def reducer(key, list_of_values):
    # key: person's name as a string
    # list of values: all friends of person, list of strings
    total = 0
    for v in list_of_values:
      total += v
    if total == 1:
      output = key.split()
      mr.emit((output[0], output[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
