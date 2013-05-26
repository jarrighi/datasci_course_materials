import MapReduce
import sys

"""
Unique Trims Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: string of nucleotides
    key = record[0]
    value = record[1]
    new_value = value[:-10]
    mr.emit_intermediate(new_value, 1)

def reducer(key, list_of_values):
    # key: nucleotide string
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    if v == 1:
      mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
