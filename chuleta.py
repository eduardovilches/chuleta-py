#Chuleta Py 

#check if exist index from array
#Example: data[i] list of range
def indexExist(self, ls, i):
  return (0 <= i < len(ls)) or (-len(ls) <= i < 0)

#sample input
#5 4
#1 2 3 4 5
#Left Rotate
def rotateLeft(d, arr):
    i =1 
    while i <= d:
        current = arr[0]
        arr.append(current)
        del arr[0]
        i += 1
     
    return arr
