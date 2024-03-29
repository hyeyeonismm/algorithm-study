from datetime import datetime
def solution(date1, date2):
    date1 = int(''.join(map(str, date1))) #20211228
    date2 = int(''.join(map(str, date2)))
    if date1 <date2:
        return 1
    else:
        return 0
   