import numpy as np

def detect_anomalies(values, z_threshold=2.5):
    if len(values) < 3:
        return []
    values = np.array(values, dtype=float)
    mean, std = values.mean(), values.std()
    if std == 0:
        return []
    return [i for i, value in enumerate(values) if abs((value - mean) / std) >= z_threshold]
