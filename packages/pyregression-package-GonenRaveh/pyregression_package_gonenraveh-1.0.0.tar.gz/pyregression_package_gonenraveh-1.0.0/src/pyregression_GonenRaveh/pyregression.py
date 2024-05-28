import numpy as np
from sklearn.linear_model import LogisticRegression

class logistic_regression_N_to_1:
    '''
    apply logistic regression (classification) to a set of numerical samples
    given x 2D array and y [N] shaped array of target classes: 0,1,2,3,...
    
    test me using:

    import numpy as np
    from pyregression import logistic_regression_N_to_1
    lr = logistic_regression_N_to_1()
    lr.fitcsv(csv_filename='iris.csv')
    sample = np.array([5.8,3.08,5.12,1.81]).reshape(1,lr.num_features()) 
    print(f'PREDICT       x={sample} y={lr.predict(sample)}')
    print(f'PREDICT_PROBA x={sample} y={lr.predict_proba(sample)}')
    ysample = np.array([2.0])
    print(f'SCORE         x={sample} y={lr.score(sample, ysample)}')
    '''
    def __init__(self):
        self.x = None
        self.y = None
        self.clf = None
        
    def fitcsv(self, csv_filename:str, delimiter:str=',', names:list[str]=None):
        '''
        csv file format is: N numerical features, 1 target "y" number, end of line:
        example of: [1] sample identifier x=[4] features, y=[1] class index|name
        #Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
        1,5.1,3.5,1.4,0.2,Iris-setosa
        2,4.9,3.0,1.4,0.2,Iris-setosa
        3,4.7,3.2,1.3,0.2,Iris-setosa
        ...
        more rows
        
        Another format: no header, no sample id, classes are numbers: 0,1,2,3
        5.1,3.5,1.4,0.2,0
        4.9,3,1.4,0.2,0
        4.7,3.2,1.3,0.2,0
        ...
        
        @param names like ['myint','myfloat','mystring']
        '''
        data = np.genfromtxt(csv_filename, delimiter=delimiter, names=names)
        n_columns = data.shape[1]
        self.x = data[:,0:n_columns-1]
        self.y = data[:,n_columns-1]
        print(f'PYTHON logistic_regression_N_to_1 x.shape={self.x.shape}')
        print(f'                                  y.shape={self.y.shape}')
        return self.fit(self.x, self.y)
                
    def fit(self,x:np.ndarray, y:np.ndarray):
        '''
        x shape [N,K]
        y shape [N]
        return dict with regression Object
        '''
        assert x.shape[0] == y.shape[0]
        self.x = x
        self.y = y
        self.clf = LogisticRegression(random_state=0).fit(x, y)
        print(f'PYTHON logistic_regression_N_to_1 fit ... SUCCESS')

    def num_features(self) ->int:
        assert self.x is not None
        return self.x.shape[1]
        
    def predict(self, x:np.ndarray) -> np.ndarray:
        '''
        x shape [K], [1,K] or [Batch,K]
        return numpy array with prediction
        '''
        assert self.clf != None
        return self.clf.predict(x)
        
    def predict_proba(self, x:np.ndarray) -> np.ndarray:
        '''
        x shape [K], [1,K] or [Batch,K]
        return numpy array with prediction
        '''
        assert self.clf != None
        return self.clf.predict_proba(x)

    def score(self, x:np.ndarray, y:np.ndarray) -> np.ndarray:
        '''
        Return the mean accuracy on the given test data and labels.
        In multi-label classification, this is the subset accuracy 
        which is a harsh metric since you require for each sample 
        that each label set be correctly predicted.
        Parameters:
        x array-like of shape (n_samples, n_features) Test samples.
        y array-like of shape (n_samples,) or (n_samples, n_outputs) True labels for X.        
        '''
        assert self.clf != None
        return self.clf.score(x, y)

