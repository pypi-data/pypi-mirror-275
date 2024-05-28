import dataVisualizing as dv
from data import TimeSeries
from model import Model, HoltWinters, Naive
from metrics import EvaluationMetrics
import heapq
import numpy as np

def main():
    # load the data
    ts = TimeSeries('./data/meanDailySolarPowerGeneration.csv')

    # handling outliers values
    ts.removeOutliers(ts.df.index[ts.df['SolarPower']==0], operation='diferent')

    # handling missing values
    ts.interpolate()

    # create visualization
    dv.createLinePlotGroupByDay(ts.df, 'SolarPowerByDay.png')
    dv.createLinePlotGroupByMonth(ts.df, 'SolarPowerByMonth.png')
    dv.createLagPlots(ts.df, 'lagPlot.png')

    # holt model training
    # split series in train and test with cross validation
    ts.trainTestSplit(0.9)
    smoothing_level_list = [i / 100.0 for i in range(1,10,2)]
    smoothing_trend_list = [i / 100.0 for i in range(1,10,2)]
    n_sets = 5
    holt_rmse_error_list = []
    holt_mape_error_list = []
    for smoothing_level in smoothing_level_list:
        for smoothing_trend in smoothing_trend_list:
            holt_mape_errors = []
            holt_rmse_errors = []

            ts.crossValidationSplit(n_sets)
            for train_index, test_index in ts.cross_validation_genarator:
                train = ts.df.index[train_index]
                valid = ts.df.index[test_index]
                model = HoltWinters()
                model.train(ts.df.loc[train].resample("D").sum(),optimized=False, smoothing_level= smoothing_level, smoothing_trend=smoothing_trend)
                forecasts = model.predict(ts.df.loc[valid])
                metrics = EvaluationMetrics()
                holt_mape_errors.append(metrics.evaluateMape(ts.df.loc[valid]['SolarPower'].tolist(),forecasts))
                holt_rmse_errors.append(metrics.evaluateRmse(ts.df.loc[valid]['SolarPower'].tolist(),forecasts))
                
            heapq.heappush(holt_mape_error_list, (sum(holt_mape_errors)/len(holt_mape_errors),smoothing_level, smoothing_trend))
            heapq.heappush(holt_rmse_error_list, (sum(holt_rmse_errors)/len(holt_rmse_errors),smoothing_level, smoothing_trend))
    
    # Naive approach
    # split series in train and test with cross validation
    naive_mape_errors = []
    naive_rmse_errors = []
    ts.crossValidationSplit(n_sets)
    for train_index, test_index in ts.cross_validation_genarator:
        train = ts.df.index[train_index]
        valid = ts.df.index[test_index]
        model = Naive()
        model.train(ts.df.loc[train]['SolarPower'].tolist()[-1])
        forecasts = len(valid)*[model.predict()]
        metrics = EvaluationMetrics()
        naive_mape_errors.append(metrics.evaluateMape(ts.df.loc[valid]['SolarPower'].tolist(),np.array(forecasts)))
        naive_rmse_errors.append(metrics.evaluateRmse(ts.df.loc[valid]['SolarPower'].tolist(),np.array(forecasts)))
    
    naive_mape = (sum(naive_mape_errors)/len(naive_mape_errors))
    naive_rmse = (sum(naive_rmse_errors)/len(naive_rmse_errors))
    best_holt = heapq.heappop(holt_rmse_error_list)
    with open('./images/validationMetrics.csv', 'w') as f:
        f.write('Model, RMSE, MAPE\n')
        f.write(f'Naive, {naive_rmse},{naive_mape}\n')
        f.write(f'Holt, {best_holt},{heapq.heappop(holt_mape_error_list)}\n')

    model_holt = HoltWinters()
    model_holt.train(ts.df.resample("D").sum(),optimized=False, smoothing_level= best_holt[1], smoothing_trend=best_holt[2])

    model_naive = Naive()
    model_naive.train(ts.df['SolarPower'].tolist()[-1])

    dv.compareHoltNaive(ts.df_test, model_holt, model_naive, 'modelsForecasting.png')

    



    

main()