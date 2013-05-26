import MapReduce
import sys

"""
Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id as a string
    # value: tuple as list of strings
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_id as a string
    # value: list of lists of strings where 2nd item of each list is order_id 
    for i in list_of_values:
      if i[0] == "order":
        for j in list_of_values:
          if j[0] == "line_item":
            mr.emit((i + j))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
