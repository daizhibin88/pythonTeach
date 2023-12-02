def isCyclic(t:str , s:str)->bool:
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s in t:
            return True
    else:
        return False
if __name__ =="__main__":
    t = input()
    s = input()
    result = isCyclic(t , s)
    print("yes") if result else print("no")