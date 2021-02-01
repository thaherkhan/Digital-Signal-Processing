def DownSampling(orginalSignal, SamplingValue):
    n, x_n = orginalSignal
    y_n = np.zeros(n.shape[0])
    Neg = n[0]
    Pos = n[n.shape[0]-1]
    k=Neg
    for i in n:
        j = i*SamplingValue
        if (j>=Neg and j<=Pos):
            y_n[k+SamplingValue+1] = x_n[j+SamplingValue+1]
        else:
            y_n[k+SamplingValue+1] = 0
        k+=1
        
    return(n, y_n)
