def miniMaxSum(arr):
    # Write your code here
    #take the array 
    #iterate position per position
    # remember range(0, len(foo))
    

    stack = list(map( lambda i: sum(arr) - arr[i], range(0, len(arr))))
    print(min(stack), max(stack) )
       
    '''for i in range(0, len(arr)):
        suum =  0
        for j  in range(0, len(arr)):
            index = arr[i]
            suum = suum + arr[j]
    
            total = suum - index
        stack.append(total)
    print(min(stack), max(stack))'''
