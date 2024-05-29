from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

def compute_rmse(df, col1, col2):
    return np.sqrt(mean_squared_error(df[col1], df[col2]))

def compute_mae(df, col1, col2):
    return mean_absolute_error(df[col1], df[col2])

def compute_metrics(df, col1, col2):
    rmse = compute_rmse(df, col1, col2)
    mae = compute_mae(df, col1, col2)
    correlation = df[col1].corr(df[col2])
    r_squared = correlation ** 2
    bias = (df[col1] - df[col2]).mean()
    return rmse, mae, correlation, r_squared, bias
