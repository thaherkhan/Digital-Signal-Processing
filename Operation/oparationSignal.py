def Operation(orginalSignal, Operator, Output):
    x_n = orginalSignal
    #print(x_n)
    y_n = np.copy(x_n[0])
    #components = x_n.shape[0]
    index = x_n.shape[1]
    
    row = 1
    for k in Operator:
        #print(k)
        if k == 1:
            for i in range(row,row+1):
                for j in range(index):
                    y_n[j]+=x_n[i][j]
            #print("k = 1 :", y_n)
        if k == 2:
            for i in range(row,row+1):
                for j in range(index):
                    y_n[j]-=x_n[i][j]
            #print("k = 2 :", y_n)
        if k == 3:
            for i in range(row,row+1):
                for j in range(index):
                    y_n[j]*=x_n[i][j]
            #print("k = 3 :", y_n)
        row=row+1

    #print(Output, y_n)
    #drawSignal(Output, y_n)
    return (Output, y_n)
