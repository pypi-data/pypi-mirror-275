import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

class logistic_regression_N_to_1:
    '''
    apply logistic regression (classification) to a set of numerical samples
    given x 2D array and y [N] shaped array of target classes: 0,1,2,3,...
    
    test me using:

    import numpy as np
    from pyregression_GonenRaveh import pyregression as pr
    lr = pr.logistic_regression_N_to_1()
    lr.fitcsv(csv_filename='iris.csv')
    sample = np.array([5.8,3.08,5.12,1.81]).reshape(1,lr.num_features()) 
    print(f'PREDICT       x={sample} y={lr.predict(sample)}')
    print(f'PREDICT_PROBA x={sample} y={lr.predict_proba(sample)}')
    ysample = np.array([2.0])
    print(f'SCORE         x={sample} y={lr.score(sample, ysample)}')
    
    lr = logistic_regression_N_to_1()
    lr.fitcsv(csv_filename='iris.csv', take_features=[0,1])
    files = lr.fit_multinomial_binary(show=False)
    print(f'files={files}')

    '''
    def __init__(self):
        self.x = None
        self.y = None
        self.clf = None
        
    def fitcsv(
        self, 
        csv_filename:str, 
        delimiter:str=',', 
        names:list[str]=None,
        take_features:list[int]=None,
        classifier:str='LogisticRegression'):
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
        self.classifier = classifier
        if take_features is not None:
            self.x = self.x[:, take_features]
        print(f'PYTHON logistic_regression_N_to_1 x.shape={self.x.shape}')
        print(f'                                  y.shape={self.y.shape}')
        return self.fit(self.x, self.y, classifier=classifier)
                
    def fit(self,x:np.ndarray, y:np.ndarray, classifier:str='LogisticRegression'):
        '''
        classifier can be: MLPClassifier, LogisticRegression
        x shape [N,K]
        y shape [N]
        return dict with regression Object
        '''
        assert x.shape[0] == y.shape[0]
        self.x = x
        self.y = y
        self.classifier = classifier
        n_classes = np.unique(self.y)
        
        if classifier == 'LogisticRegression':
            self.clf = LogisticRegression(random_state=0)
        elif classifier == 'MLPClassifier':
            from sklearn.neural_network import MLPClassifier
            self.clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, n_classes), random_state=1)
        else:
            print(f'No such classifier named {classifier}')
            return None
        #
        self.clf.fit(x, y)
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

    def fit_multinomial_binary(self, show:bool=False) -> list[str]:
        '''
        call me after calling fit() or fitcsv()
        works only on X with two features shape [N,2]
        return list of names of PNG generated plots
        '''
        X, y = self.x, self.y
        out = list()
        for multi_class in ("multinomial", "ovr"):
            clf = LogisticRegression(solver="sag", max_iter=100, random_state=42)
            if multi_class == "ovr":
                clf = OneVsRestClassifier(clf)
            clf.fit(X, y)

            # print the training scores
            print("training score : %.3f (%s)" % (clf.score(X, y), multi_class))
            print(f'classes={clf.classes_}')
            plt.clf()
            plt.cla()

            _, ax = plt.subplots()
            DecisionBoundaryDisplay.from_estimator(
                clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
            )
            plt.title(f"Decision surface of {self.classifier} (%s)" % multi_class)
            plt.axis("tight")

            # Plot also the training points
            colors = "bry"
            for i, color in zip(clf.classes_, colors):
                idx = np.where(y == i)
                plt.scatter(
                    X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
                )

            # Plot the three one-against-all classifiers
            xmin, xmax = plt.xlim()
            ymin, ymax = plt.ylim()
            if multi_class == "ovr":
                coef = np.concatenate([est.coef_ for est in clf.estimators_])
                intercept = np.concatenate([est.intercept_ for est in clf.estimators_])
            else:
                coef = clf.coef_
                intercept = clf.intercept_

            def plot_hyperplane(c, color):
                def line(x0):
                    return (-(x0 * coef[int(c), 0]) - intercept[int(c)]) / coef[int(c), 1]

                plt.plot([xmin, xmax], [line(xmin), line(xmax)], ls="--", color=color)

            for i, color in zip(clf.classes_, colors):
                fname = f'_{multi_class}_{i}.png'
                plot_hyperplane(i, color)
                plt.savefig(fname)
                out.append(fname)
            if show:
                plt.show()
        #
        return out