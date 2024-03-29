def solution(arr, queries):
    for s, e in queries:
        while s<=e:
            arr[s]+=1
            s+=1
    return arr