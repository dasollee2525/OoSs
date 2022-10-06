import sys
from collections import deque

def main():
    #get the input from user
    data = []
    p_num = int(input())
    for i in range(p_num):
        data.append(list(map(int, sys.stdin.readline().split())))
    #define ready queue using deque
    rq0 = deque() #TQ = 2
    rq1 = deque() #TQ = 4
    rq2 = deque() #SRTN
    MFQ = [rq0, rq1, rq2]
    
    
 
if __name__ == "__main__":
    main()
