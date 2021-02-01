def timeShifting(orginalSignal, shiftingAmount):
    n, x_n = orginalSignal
    y_n = np.zeros(n.shape[0])
    # Main Logic
    if shiftingAmount > 0:
        if shiftingAmount > n.shape[0]:
            shiftingAmount = n.shape[0]
        dataToCopy = x_n[ : n.shape[0]- shiftingAmount]
        y_n[shiftingAmount : ] = dataToCopy
    elif shiftingAmount < 0:
        if abs(shiftingAmount) > n.shape[0]:
            shiftingAmount = n.shape[0] * (-1)
        dataToCopy = x_n[ -shiftingAmount : ]
        y_n[ : n.shape[0] + shiftingAmount] = dataToCopy
    else:
        y_n = x_n
        
    return (n, y_n)
