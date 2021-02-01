def drawSignal(n, A):
    fig = plt.figure()
    axis = fig.add_subplot(111)
    plt.title("Final Signal")
    axis.stem(n, A, use_line_collection=True)
