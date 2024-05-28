import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import TimeSeriesSplit

#   class that represents a time series data
class TimeSeries():
    def __init__(self, path):
        self.df = pd.read_csv(path, header=0)
        self.df['datetime'] = pd.to_datetime(self.df['datetime'])
        self.df = self.df.set_index('datetime')
        self.df = self.df.resample("D").sum()
        
        self.scaler = None
        self.cross_validation_genarator = None
        self.df_test = None

    #   pass a percentage to split the series in test and train
    def trainTestSplit(self, percentage):
        self.df_test = self.df[int(self.df.size*percentage):]
        self.df = self.df[:int(self.df.size*percentage)]

    #   normalize passing a range tuple
    #   the first elem should be the min value and the second, the max value
    def minMaxscaler(self, range):
        scaler = MinMaxScaler(feature_range=range)
        self.scaler = scaler

    #   The function check for missing values
    #   then return the index of then.
    def missingValuesCheck(self):
        index = self.df.index[self.df.isna().any(axis=1)]
        return index
    
    #   linear interpolate missing values
    def interpolate(self):
        self.df = self.df.interpolate(method='linear')

    #   the function receive a pandas df, the method that will be used to detect outliers.
    #   the threshold is used in z_score method and contamination in isolation_forest
    def outliersValuesCheck(df, method='iqr', threshold=3, contamination=0.1):
        outliers = None

        if 'z_score':
            mean = df.mean()
            std = df.std()
            z_scores = (df - mean) / std
            outliers = df[(z_scores.abs() > threshold)].index
        elif 'iqr':
            q1 = df.quantile(0.25)
            q3 = df.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = df[(df < lower_bound) | (df > upper_bound)].index
        elif 'isolation_forest':
            model = IsolationForest(contamination=contamination)
            model.fit(df.values.reshape(-1, 1))
            scores = model.decision_function(df.values.reshape(-1, 1))
            outlier_indices = scores.argsort()[-int(len(df) * contamination):]
            outliers = df.iloc[outlier_indices].index

        return outliers
    
    #   receive outliers and remove indeces in outliers list
    def removeOutliers(self, outliers, operation='diferent'):
        for outlier in outliers:
            if operation == 'diferent':
                self.df = self.df[self.df.index != outlier]
            elif operation == 'greater':
                self.df = self.df[self.df.index > outlier]
            elif operation == 'less':
                self.df = self.df[self.df.index < outlier]

    #   split data for training, validation and test
    def splitData(self):
        train_index = self.df.shape[0]*80//100
        val_index = self.df.shape[0]*90//100
        self.df = self.df.resample("D").sum()
        train_df = self.df[: self.df.index[train_index]]
        val_df = self.df[self.df.index[train_index]: self.df.index[val_index]]
        test_df = self.df[self.df.index[val_index]:]
        train_df.index = pd.to_datetime(train_df.index)
        test_df.index = pd.to_datetime(test_df.index)
        val_df.index = pd.to_datetime(val_df.index)
        return train_df, val_df, test_df
    
    #   split the dataset into n sets for cross validation.
    #   the method returns a generator object that generates train and test sets
    def crossValidationSplit(self, n_splits):
        tscv = TimeSeriesSplit(n_splits=n_splits)
        self.cross_validation_genarator = tscv.split(self.df)
        return tscv