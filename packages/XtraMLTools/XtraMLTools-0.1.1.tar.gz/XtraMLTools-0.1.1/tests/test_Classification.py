# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:04:09 2024

@author: atdou
"""

import pandas
from XtraMLTools.Classification import Categorical_Polynomial_Logistic_Regression
from auxiliary_classes import create_classy_data


# testing that the cat_poly_log_regression guy correctly classifies points separated by a polynomial
def test_classification_1():
    """
    Description
    -----------
    testing that the Categorical_Polynomial_Logistic_Regression guy is finding the correct classes on 
    data with no outliers and no deviations from the fit, f.  I guess we can't demand a perfect fit, per se'.  
    Well, I can get 100% accuracy if I play with C hyperparameter, but whatever.
    """
    def f(x):
        def poly(x):
            return 10*(x[0])**2 - 2*x[1]*x[2] + 5*x[0] + 4*x[1]**2 - 7*x[2] - 10
        if poly(x) <= 0:
            return 0
        else: 
            return 1
    data_exp = create_classy_data()
    data_exp.set_X(x_min=-2, x_max=2, N=2000, n_out=0, dim=3)
    data_exp.set_y(func=f, f_values=[0,1], p_norm=1, p_out=1)
    X = data_exp.X
    y = data_exp.y
    CPLR = Categorical_Polynomial_Logistic_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=2, C=1)
    CPLR.fit(X,y)
    y_pred = pandas.Series(CPLR.predict(X))
    percent_correct = ((y == y_pred).sum())/len(y)
    print(percent_correct)
    assert (1-percent_correct) <= 0.005


def test_classification_2():
    """
    Description
    -----------
    Now doing the same, but with three classes
    """
    def f(x):
        def poly(x):
            return 10*(x[0])**2 - 2*x[1]*x[2] + 5*x[0] + 4*x[1]**2 - 7*x[2] - 10
        if poly(x) <= 0:
            return 0
        elif poly(x) <= 5: 
            return 1
        else:
            return 2
    data_exp = create_classy_data()
    data_exp.set_X(x_min=-2, x_max=2, N=2000, n_out=0, dim=3)
    data_exp.set_y(func=f, f_values=[0,1,2], p_norm=1, p_out=1)
    X = data_exp.X
    y = data_exp.y
    CPLR = Categorical_Polynomial_Logistic_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=2, C=10, max_iter=5000)
    CPLR.fit(X,y)
    y_pred = pandas.Series(CPLR.predict(X))
    percent_correct = ((y == y_pred).sum())/len(y)
    print(percent_correct)
    assert (1-percent_correct) <= 0.005
    
    
    