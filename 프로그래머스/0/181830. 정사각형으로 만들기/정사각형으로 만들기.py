def solution(arr):
    tmp=len(arr[0])
    if len(arr)>tmp: # 4>2
        for i in range(len(arr)): # 0 1 2 3
            for j in range(len(arr)-tmp): #2
                arr[i].append(0)
              
    else:
        for i in range(len(arr[0])-len(arr)):
            arr.append([0] * len(arr[0]))
    
    return arr
