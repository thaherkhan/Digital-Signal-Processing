def Mirroring(orginalSignal):
    n, x_n = orginalSignal
    
    Neg = n[0]
    Pos = n[n.shape[0]-1]
    
    #print(Neg, Pos)
    
    y_n = np.zeros(n.shape[0])

    j=0
    for i in n:
        if i == 0:
            zero = j
        j+=1
    
    #print((Neg+Pos))
    if (Neg+Pos) == 0:
    
        NegCopy = x_n[ : zero ]
        PosCopy = x_n[ zero+1 : ]
        
        NegCopy = np.flipud(NegCopy)
        PosCopy = np.flipud(PosCopy)
        #print(PosCopy)
        #print(NegCopy)
        
        y_n[ : zero ] = PosCopy
        y_n[zero] = x_n[zero]
        y_n[ zero+1 : ] = NegCopy
    
    else:
        
        NegPlus  = Neg*(-1)
        PosMinus = Pos*(-1)
        
        #print(NegPlus,PosMinus)
        
        if (NegPlus<=Pos):
            PosCopy = x_n[ zero+1 : NegPlus+(NegPlus+1)]
            PosCopy = np.flipud(PosCopy)
            y_n[ : zero ] = PosCopy
        else:
            PosCopy = x_n[ zero+1 : ]
            PosCopy = np.flipud(PosCopy)
            y_n[ PosMinus+(-Neg) : zero ] = PosCopy
            
        if (PosMinus>=Neg):
            NegCopy = x_n[PosMinus+(-PosMinus+2) : zero ]
            NegCopy = np.flipud(NegCopy)
            y_n[zero] = x_n[zero]
        else:
            NegCopy = x_n[ : zero ]
            NegCopy = np.flipud(NegCopy)
            y_n[ zero+1 :  NegPlus+(NegPlus+1) ] = NegCopy
        
        #print(PosCopy)
        #print(NegCopy)
        
        #y_n[ : zero ] = PosCopy   -3,5
        #y_n[ PosMinus+(-PosMinus+2) : zero ] = PosCopy   -5,3
        #y_n[zero] = x_n[zero]
        #y_n[ zero+1 :  NegPlus+(NegPlus+1) ] = NegCopy
    
    #print(NegCopy)
    #print(PosCopy)
    #print(y_n)

    return (n,y_n)
