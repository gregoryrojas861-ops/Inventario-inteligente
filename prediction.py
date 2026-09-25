import numpy as np
from sklearn.linear_model import LinearRegression

def predict_demand(history, periods=7):
    if len(history) < 3:
        return None
    x = np.arange(len(history)).reshape(-1, 1)
    y = np.array(history, dtype=float)
    model = LinearRegression().fit(x, y)
    future_x = np.arange(len(history), len(history) + periods).reshape(-1, 1)
    return model.predict(future_x).tolist()
