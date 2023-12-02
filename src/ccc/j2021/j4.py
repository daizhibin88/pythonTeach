def solution(booklist:str)->int:
    ltimes = 0
    mtimes = 0
    stimes = 0

    for c in booklist :
        if c =="L":
            ltimes=ltimes+1
        elif c =="M":
            mtimes= mtimes +1
        else:
            stimes = stimes +1

    mltimes = 0
    sltimes = 0
    for c in booklist[0:ltimes]:
        if c =='M':
            mltimes = mltimes +1
        elif c=='S':
            sltimes = sltimes +1

    lmtimes = 0
    smtimes = 0

    for c  in booklist[ltimes: ltimes+mtimes]:
        if c =='L':
            lmtimes = lmtimes +1
        elif c =='S':
            smtimes = smtimes +1

    lstimes = 0
    mstimes = 0

    for c  in booklist[ltimes+mtimes:]:
        if c =='L':
            lstimes = lstimes +1
        elif c =='M':
            mstimes = mstimes +1

    count = 0
    count =count + min ( mltimes , lmtimes )
    difflm = abs (mltimes -lmtimes)
    count = count + min (sltimes , lstimes)
    diffsl  = abs (sltimes - lstimes)
    count = count + min (smtimes , mstimes)
    diffsm = abs (smtimes - mstimes)

    count = count + 2 * diffsl
    return count
if __name__ == "__main__":
    booklist = input()
    print ( solution(booklist))
