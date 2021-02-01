def OperationPartAdd(orginalSignal, UpdateSignal):
    
    check1 = {}
    check2 = {}
    #print("X_n : ",orginalSignal, "temp : ", UpdateSignal)
    x_n, n = orginalSignal
    x_n1, n1 = UpdateSignal
    #print("n = ",n , "x_n = ", x_n)
    #print("n = ",n1 , "x_n = ", x_n1)
    mnlen  = x_n[0]
    mnlen1 = x_n1[0]
    
    mxlen1 = x_n[len(x_n)-1]
    mxlen2 = x_n1[len(x_n1)-1]
    
    mn = min(mnlen,mnlen1)    # Check The Minimum index 
    mx = max(mxlen1,mxlen2)         # Check The Maximum index
    #print("Min : ", mn, "Max : ", mx)
    ind = np.arange(mn,mx+1,1)
    y_n = np.zeros(mx+1-mn)
    #print("ind : ", ind, "y_n : ", y_n)
    
    # Here Mapping The index
    for i in range(len(n)):
        check1[x_n[i]]=n[i]
        
    # Here Mapping The index
    for i in range(len(n1)):
        check2[x_n1[i]]=n1[i]
    
    # Here Matching The index and Operation
    index=0
    for i in ind:
        if i in check1.keys() and i in check2.keys():
            y_n[index]=check1[i]+check2[i]
        elif i in check1.keys():
            y_n[index]=check1[i]
        elif i in check2.keys():
            y_n[index]=check2[i]
        
        index+=1
    
    #print("y_n : ",y_n,"ind : ",ind)
    return (y_n, ind)
