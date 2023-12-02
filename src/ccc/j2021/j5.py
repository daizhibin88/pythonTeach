"""
3
3
2
R 1
C 1

expect: 4
"""
def solution(M:int , N:int, listStr:list)->int:
    M = int(input())
    # row

    N = int(input())
    # colom

    K = int(input())

    listBrush=set()
    for i3 in range(K):
        brush = input()
        if brush in listBrush:
            listBrush.remove(brush)
        else:
            listBrush.add(brush)

    rtimes =0
    ctimes =0
    for brush in listBrush:
        if brush[0] =='R' :
            rtimes +=1
        else:
            ctimes+=1

    print ( rtimes * N + ctimes* M - rtimes * ctimes*2 )

if __name__ == "__main__":
    M = int(input())
    # row

    N = int(input())
    # colom

    K = int(input())
    listStr = []
    for i3 in range(K):
        listStr.append(input())


