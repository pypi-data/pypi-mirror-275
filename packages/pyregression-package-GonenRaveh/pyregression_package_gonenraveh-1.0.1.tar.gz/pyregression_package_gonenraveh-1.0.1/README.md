# pyregression Package

Logistic Regression (aka logit, MaxEnt) classifier.
In the multiclass case, the training algorithm uses the one-vs-rest (OvR) 
scheme if the ‘multi_class’ option is set to ‘ovr’, and uses the 
cross-entropy loss if the ‘multi_class’ option is set to ‘multinomial’. 
(Currently the ‘multinomial’ option is supported only by the ‘lbfgs’, ‘sag’, ‘saga’ and ‘newton-cg’ solvers.)
This class implements regularized logistic regression using the ‘liblinear’ 
library, ‘newton-cg’, ‘sag’, ‘saga’ and ‘lbfgs’ solvers. Note that regularization 
is applied by default. It can handle both dense and sparse input. Use C-ordered 
arrays or CSR matrices containing 64-bit floats for optimal performance; any other 
input format will be converted (and copied).
The ‘newton-cg’, ‘sag’, and ‘lbfgs’ solvers support only L2 regularization with 
primal formulation, or no regularization. The ‘liblinear’ solver supports both 
L1 and L2 regularization, with a dual formulation only for the L2 penalty. 
The Elastic-Net regularization is only supported by the ‘saga’ solver.
