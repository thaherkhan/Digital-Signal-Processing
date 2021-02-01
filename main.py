if __name__ == "__main__":
    
    #filename = open("F:\All Subject\Digital Signal Processing\Lab\input.txt", "r")
    filename = open("input.txt", "r")
    #TestCase = int(input("Number of Test Case: "))
    TestCase = int(filename.readline())
    
    for T in range(TestCase):

        #SignalPart = int(input("Part of Signal: "))
        SignalPart = int(filename.readline())
        OutputPart = {}
        mn = 1000000000
        mx = -10000000000
        OperatorPart = 0
        ComponentsOperatorPart = []
        ComponentsSignalPart = {}
        for j in range(SignalPart):
            
            #Lower_bound = int(input("Enter The Lower Bound Range N1 = "))
            Lower_bound = int(filename.readline())
            #Upper_bound = int(input("Enter The Upper Bound Range N2 = "))
            Upper_bound = int(filename.readline())
            #Components  = int(input("Enter The Number of Components = "))
            Components = int(filename.readline())
            Operator = 0
            ComponentsOperator = []
            ComponentsSignal = []
            ComponentsSignalDict = {}
            for i in range(Components):
                #ScalingValue = int(input("Enter The Scaling value A = "))
                ScalingValue = int(filename.readline())
                #Signal_Type = int(input("Signal Type : 1=Impulse, 2=Step, 3=Remp : "))
                Signal_Type = int(filename.readline())
                
                if Signal_Type == 1:
                    delta = unitImpulse(Lower_bound, Upper_bound)
                    print(delta[0], delta[1])
                    Output = Scaling(delta,ScalingValue)
                    #Shifting_Operation = int(input("Shifting_Operation IF 1=YES and 2=NO : "))
                    Shifting_Operation = int(filename.readline())
                    if Shifting_Operation == 1:
                        #ShiftingAmount = int(input("Shifting Amount : "))
                        ShiftingAmount = int(filename.readline())
                        Output = timeShifting(Output, ShiftingAmount)            
                    #Mirroring_Operation = int(input("Mirroring_Operation IF 1=YES and 2=NO : "))
                    Mirroring_Operation = int(filename.readline())
                    if Mirroring_Operation == 1:
                        if Shifting_Operation == 1:
                            Output = Mirroring(Output)
                        else:
                            Output = Mirroring(Output)                
                    #DownSampling_Operation = int(input("DownSampling_Operation IF 1=YES and 2=NO : "))
                    DownSampling_Operation = int(filename.readline())
                    if DownSampling_Operation == 1:                
                        #SamplingValue = int(input("Sampling Value : "))
                        SamplingValue = int(filename.readline())
                        if Mirroring_Operation == 1:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                        elif Shifting_Operation == 1:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                        else:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                    else:
                        if Mirroring_Operation == 1:
                            print(Output[0], Output[1])
                        elif Shifting_Operation == 1:
                            print(Output[0], Output[1])
                        else:
                            print(Output[0], Output[1])
                
                elif Signal_Type == 2:            
                    Step = unitStep(Lower_bound, Upper_bound)
                    print(Step[0], Step[1])
                    Output = Scaling(Step,ScalingValue)            
                    #Shifting_Operation = int(input("Shifting_Operation IF 1=YES and 2=NO : "))
                    Shifting_Operation = int(filename.readline())
                    if Shifting_Operation == 1:                
                        #ShiftingAmount = int(input("Shifting Amount : "))
                        ShiftingAmount = int(filename.readline())
                        Output = timeShifting(Output, ShiftingAmount)            
                    #Mirroring_Operation = int(input("Mirroring_Operation IF 1=YES and 2=NO : "))
                    Mirroring_Operation = int(filename.readline())
                    if Mirroring_Operation == 1:
                        if Shifting_Operation == 1:
                            Output = Mirroring(Output)
                        else:
                            Output = Mirroring(Output)                
                    #DownSampling_Operation = int(input("DownSampling_Operation IF 1=YES and 2=NO : "))
                    DownSampling_Operation = int(filename.readline())
                    if DownSampling_Operation == 1:                
                        #SamplingValue = int(input("Sampling Value : "))
                        SamplingValue = int(filename.readline())
                        if Mirroring_Operation == 1:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                        elif Shifting_Operation == 1:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                        else:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                    else:
                        if Mirroring_Operation == 1:
                            print(Output[0], Output[1])
                        elif Shifting_Operation == 1:
                            print(Output[0], Output[1])
                        else:
                            print(Output[0], Output[1])
            
                elif Signal_Type == 3:
                    Ramp = unitRamp(Lower_bound, Upper_bound)
                    print(Ramp[0], Ramp[1])
                    Output = Scaling(Ramp,ScalingValue)            
                    #Shifting_Operation = int(input("Shifting_Operation IF 1=YES and 2=NO : "))
                    Shifting_Operation = int(filename.readline())
                    if Shifting_Operation == 1:                
                        #ShiftingAmount = int(input("Shifting Amount : "))
                        ShiftingAmount = int(filename.readline())
                        Output = timeShifting(Output, ShiftingAmount)            
                    #Mirroring_Operation = int(input("Mirroring_Operation IF 1=YES and 2=NO : "))
                    Mirroring_Operation = int(filename.readline())
                    if Mirroring_Operation == 1:
                        if Shifting_Operation == 1:
                            Output = Mirroring(Output)
                        else:
                            Output = Mirroring(Output)                
                    #DownSampling_Operation = int(input("DownSampling_Operation IF 1=YES and 2=NO : "))
                    DownSampling_Operation = int(filename.readline())
                    if DownSampling_Operation == 1:                
                        #SamplingValue = int(input("Sampling Value : "))
                        SamplingValue = int(filename.readline())
                        if Mirroring_Operation == 1:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                        elif Shifting_Operation == 1:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                        else:
                            Output = DownSampling(Output, SamplingValue)
                            print(Output[0], Output[1])
                    else:
                        if Mirroring_Operation == 1:
                            print(Output[0], Output[1])
                        elif Shifting_Operation == 1:
                            print(Output[0], Output[1])
                        else:
                            print(Output[0], Output[1])
                
                if ((Components-i) != 1):
                    #Operator = int(input("Component Operator : 1=Add, 2=Subtruct, 3=Product : "))
                    Operator = int(filename.readline())
                    ComponentsOperator.append(Operator)
                    
                ComponentsSignal.append(Output[1])
            
            ComponentsSignal = np.array(ComponentsSignal)
            #print(ComponentsSignal)
            if Operator != 0:
                OutputComponents = Operation(ComponentsSignal,ComponentsOperator,Output[0])
            #drawSignal(Output[0], Output[1])
            else:
                OutputComponents = Output
            
            ComponentsSignalDict = OutputComponents
            
            if OperatorPart != 0 :
                
                if OperatorPart == 1:
                    signalPart = OperationPartAdd(ComponentsSignalPart,ComponentsSignalDict)
                    ComponentsSignalPart = signalPart
                elif OperatorPart == 2:
                    signalPart = OperationPartSub(ComponentsSignalPart,ComponentsSignalDict)
                    ComponentsSignalPart = signalPart
                elif OperatorPart == 3:
                    signalPart = OperationPartMul(ComponentsSignalPart,ComponentsSignalDict)
                    ComponentsSignalPart = signalPart
                    
            else:
                ComponentsSignalPart = OutputComponents
            
            print(ComponentsSignalPart[1], ComponentsSignalPart[0])
            if ((SignalPart-j) != 1):
                #OperatorPart = int(input("Part Operator : 1=Add, 2=Subtruct, 3=Product : "))
                OperatorPart = int(filename.readline())
                
            #drawSignal(ComponentsSignalPart[0], ComponentsSignalPart[1])
            print(ComponentsSignalPart[1], ComponentsSignalPart[0])
        drawSignal(ComponentsSignalPart[1], ComponentsSignalPart[0])
        
