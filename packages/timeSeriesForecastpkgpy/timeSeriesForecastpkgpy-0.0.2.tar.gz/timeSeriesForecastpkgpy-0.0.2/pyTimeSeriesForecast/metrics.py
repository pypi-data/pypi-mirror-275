from math import sqrt
import numpy as np

class EvaluationMetrics():
    def __init__(self):
        self.mse = None
        self.rmse = None
        self.mae = None
        self.mape = None

    def evaluateMse(self, test_targets, test_pred):
        self.mse = np.mean((test_targets - test_pred) ** 2)
        return self.mse
    
    def evaluateRmse(self, test_targets, test_pred):
        if self.mse:
            self.rmse = sqrt(self.mse)
        else:
            self.mse = self.evaluateMse(test_targets, test_pred)

        return self.mse
    
    def evaluateMae(self, test_targets, test_pred):
        self.mae = np.mean(np.abs(test_targets - test_pred))
        return self.mae

    def evaluateMape(self, test_targets, test_pred):
        self.mape = np.mean(np.abs((test_targets - test_pred) / test_targets)) * 100
        return self.mape

    def print(self,mse=True,rmse=True,mae=True,mape=True):
        print(f"  Mean Squared Error (MSE): {mse}")
        print(f"  Root Mean Squared Error (RMSE): {rmse}")
        print(f"  Mean Absolute Error (MAE): {mae}")
        print(f"  Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

    def save(self, path, file_name):
        with open(path+file_name+'.csv', 'w') as f:
            f.write('Metric,Value,\n')
            if self.mse:
                f.write(f'MSE,{self.mse}\n')
            if self.rmse:
                f.write(f'RMSE,{self.rmse}\n')
            if self.mae:
                f.write(f'MAE,{self.mae}\n')
            if self.mape:
                f.write(f'MSE,{self.mape:.2f}%\n')
