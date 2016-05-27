def lag_graph(lag_array):
    """"Given an array of lags, creates a lag graph."""
    x = np.arange(1, len(lag_array)+1)
    plt.plot(np.linspace(1,len(lag_array)), np.repeat(0, len(np.linspace(1,len(lag_array)))), 
             "-", color="#526774")
    for i in range(len(lag_array)):
        plt.plot(np.repeat(i+1,len(np.linspace(0, lag_array[i]))),
                 np.linspace(0, lag_array[i]), "-", color="#B1A5A5")
    plt.plot(x, lag_array, "o", color="#5A99C4")
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2+2, y1-0.05, y2+0.05))
    plt.title("Autocorrelation Lag {}".format(len(lag_array)))