
def diagonalDifference(arr):
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)
    
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]
        
    return abs(primary_sum - secondary_sum)
