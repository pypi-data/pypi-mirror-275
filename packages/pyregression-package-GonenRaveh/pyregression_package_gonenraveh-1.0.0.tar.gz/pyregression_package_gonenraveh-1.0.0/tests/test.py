import numpy as np
from pyregression import logistic_regression_N_to_1
lr = logistic_regression_N_to_1()
lr.fitcsv(csv_filename='iris.csv')
sample = np.array([5.8,3.08,5.12,1.81]).reshape(1,lr.num_features()) 
print(f'PREDICT       x={sample} y={lr.predict(sample)}')
print(f'PREDICT_PROBA x={sample} y={lr.predict_proba(sample)}')
ysample = np.array([2.0])
print(f'SCORE         x={sample} y={lr.score(sample, ysample)}')



