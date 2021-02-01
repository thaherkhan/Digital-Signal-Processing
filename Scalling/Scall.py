def Scaling(orginalSignal, ScalingValue):
    n, x_n = orginalSignal
    y_n = x_n*ScalingValue
    
    return (n, y_n)
