import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier as a string
    # value: document contents as a string
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#    output = []
#    for item in list_of_values:
#      if item not in output:
#        output.append(item)
    output = set(list_of_values)
    output = list(output)
    mr.emit((key, output))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
