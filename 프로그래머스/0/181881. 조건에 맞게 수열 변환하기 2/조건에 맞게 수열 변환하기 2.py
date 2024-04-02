def solution(arr):
    count = 0
    while True:
        changed = False  # 변화가 있었는지 추적하는 플래그
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
                changed = True
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = (arr[i] * 2) + 1
                changed = True
        if not changed:
            break
        count += 1
    return count
