#Chuleta Py 

#check if exist index from array
#Example: data[i] list of range
def indexExist(self, ls, i):
  return (0 <= i < len(ls)) or (-len(ls) <= i < 0)
