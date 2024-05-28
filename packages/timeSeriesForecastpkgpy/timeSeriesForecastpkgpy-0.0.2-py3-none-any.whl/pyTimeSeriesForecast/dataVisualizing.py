import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as ts

# create line plot grouped by month
def createLinePlotGroupByMonth(df, file_name):
    df_monthly = df.resample('M')['SolarPower'].sum()
    # Create the plot

    for month, data in df_monthly.groupby(df_monthly.index.month):
        plt.plot(data.index.year, data, label=f"Month {month}")

    # Customize labels and title
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Solar Power (Sum)", fontsize=12)
    plt.title("Seasonal Variation of Solar Power", fontsize=14)

    # Add legend
    plt.legend()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the plot
    plt.savefig('./images/' + file_name, bbox_inches='tight')

    plt.tight_layout()
    plt.show()

# create line plot grouped by day
def createLinePlotGroupByDay(df, file_name):
    df_day = df.resample('D')['SolarPower'].sum()
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
  
    plt.plot(df_day.index, df_day, label=f"Daily Solar Power")

    # Customize labels and title
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Solar Power (Sum)", fontsize=12)
    plt.title("Daily Solar Power", fontsize=14)

    # Add legend
    plt.legend()

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the plot
    plt.savefig('./images/' + file_name, bbox_inches='tight')
    plt.tight_layout()
    plt.show()

# receive a df and create a lag plot
def createLagPlots(df, file_name):

    acf = ts.acf(df)

    # Plot the ACF


    plt.plot(acf)
    plt.xlabel("Lags")
    plt.ylabel("Autocorrelation")
    plt.title("Autocorrelation Function (ACF)")
    plt.savefig('./images/' + file_name, bbox_inches='tight')
    plt.show()

# create plot to compare Holt and Naive model
def compareHoltNaive(test_df, holt, naive, file_name):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(test_df.index, test_df.values, color="gray")
    ax.plot(test_df.index, holt.predict(test_df), label="alpha="+str(holt.model.params['smoothing_level'])[:4]+", beta="+str(holt.model.params['smoothing_trend'])[:4], color='#ff7823')
    ax.plot(test_df.index, len(test_df.values)*[naive.predict()], color="#3c763d")
    plt.legend()
    plt.savefig('./images/' + file_name, bbox_inches='tight')
    plt.show()