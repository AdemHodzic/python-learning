# We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum 
# of the average of each group. What is the largest score we can achieve?  





def solution(arr, length):
    results = []
    
    for i in range(0, len(arr) - length):
        temp = arr[i:i+length]
        new_arr = list(filter(lambda x: x not in temp ,arr))
        
        print('new arr is ', new_arr)
        print('temp arr is ', temp)
        
        sum_all = sum(new_arr) + sum(temp) / length
        results.append(sum_all)
    return max(results)
