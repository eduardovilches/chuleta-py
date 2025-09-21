def diagonalDifference(arr):
    # Write your code here
    n =  len(arr)
    first_diagonal_sum =  0
    second_diagonal_sum = 0
    
    for i  in range(n):
        first_diagonal_sum += arr[i][i]
        second_diagonal_sum += arr[i][n - i - 1]
        
    return abs(first_diagonal_sum - second_diagonal_sum)
