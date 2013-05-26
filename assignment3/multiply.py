import MapReduce
import sys

"""
Matrix Multiplication Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: Index to send this value to
    # value: the whole record
    value = record
    if record[0] == 'a':
      for i in range(5):
        key = "AB%s%s" % (record[1], i)
        mr.emit_intermediate(key, value)
    if record[0] == 'b':
      for j in range(5):
        key = "AB%s%s" % (j, record[2])
        mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: index of new matrix
    # value: 
    index1 = int(key[2])
    index2 = int(key[3])
    total = 0
    a_list = [ x for x in list_of_values if x[0] == 'a']
    b_list = [ y for y in list_of_values if y[0] == 'b']
    for i in a_list:
      for j in b_list:
        if i[2] == j[1]:
          increment = i[3] * j[3]
          total += increment
    output = (index1, index2, total)
    if total != 0:
      mr.emit(output)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
