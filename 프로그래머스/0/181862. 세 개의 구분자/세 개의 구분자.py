def solution(myStr):
    myStr = myStr.replace('a' ,' ').replace('b',' ').replace('c',' ')
    myStr = myStr.split()
    
    if len(myStr)==0:
        myStr.append('EMPTY')
        
    return myStr

