def unitImpulse(lb, up):
    assert(lb<=up), "Lower Bound can't be greater than Upper bound"
    # Talking the samples range
    n = np.arange(lb, up+1, 1)
    x_n = []
    for i in n:
        if i == 0:
            x_n.append(1)
        else:
            x_n.append(0)        
    x_n = np.array(x_n)
    
    return (n, x_n)
