def lag_cal(time_srs, tot_lag):
    """Calculates the autocorrelationlag of a given time series.
    
    PARAMETERS
    ==========
    
    time_srs: numpy array or list. It should be a 1*n array (only values of the variable we are considering).
    tot_lag: number of lags we want our correlation to estimate.
    """
    data_frame_time_srs = pd.DataFrame(time_srs, columns=["values"])
    lag_cal = []
    for num_lag in range(1, tot_lag+1):
        lag_cal.append(data_frame_time_srs["values"].autocorr(lag=num_lag))
    return np.array(lag_cal)

def lag_graph_ci(lag_array, num_periods, conf_inter=False):
    """"Given an array of lags, creates a lag graph."""
    """
    PARAMETERS
    ==========
    lag_array: array that contains the result of the autocorrelation function. np array or pandas series.
    num_periods: number of periods of the time series.
    conf_inter: plots the 95% CI's.
    
    """
    x = np.arange(1, len(lag_array)+1)
    plt.plot(np.linspace(1,len(lag_array)), np.repeat(0, len(np.linspace(1,len(lag_array)))), 
             "-", color="#526774")
    for i in range(len(lag_array)):
        plt.plot(np.repeat(i+1,len(np.linspace(0, lag_array[i]))),
                 np.linspace(0, lag_array[i]), "-", color="#B1A5A5")
    plt.plot(x, lag_array, "o", color="#5A99C4")
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1-0.3, x2+0.9, y1-0.05, y2+0.05))
    plt.title("Autocorrelation Lag {}".format(len(lag_array)))
    
    #Plotting confidence intervals, if selected
    if conf_inter:
        low_ci = norm.ppf(0.05, loc=0, scale=1/np.sqrt(200))
        up_ci = norm.ppf(0.95, loc=0, scale=1/np.sqrt(200))
        plt.plot(np.linspace(1, len(lag_array)), 
                 np.repeat(low_ci, len(np.linspace(1, len(lags_obs_ma_1)))),'--', color="#3B3C3F")
        plt.plot(np.linspace(1, len(lag_array)), 
                 np.repeat(up_ci, len(np.linspace(1, len(lags_obs_ma_1)))),'--', color="#3B3C3F")
                
        