if __name__=='__main__':
    import sys
    n=int(sys.argv[1])
    try:
        if sys.argv[2]=="dict":
            a={}
            a[2]=0
            a[5]=0
            a[7]=0
    except:
        a=range(4)
    k=None
    for i in range(n):
        a[3]=i
