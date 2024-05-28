# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:15:23 2024

@author: atdou
"""

import numpy  
from XtraMLTools.Preprocessing import Regression_Outlier_Removal  
from XtraMLTools.Regression import (Linear_Regression, Decision_Tree_Regression, Gradient_Boost_Regression, 
                                    Quadratic_Regression, Polynomial_Regression)
from auxiliary_classes import create_regress_data, CM_ROR_predictions


def test_ROR_fit_ave():
    """
    Description
    -----------
    testing that fit method correctly classifies all points using the final iteration (same as average in this case) 
    of a polynomial regressor.  First have to create data using create_data class.
    """
    data_exp = create_regress_data()
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    N, n_out = 500, 25
    data_exp.set_X(x_min=-2, x_max=2, N=N, n_out=n_out, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=20, max_y=30)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    model_dict = {"PR": PR}
    ROR = Regression_Outlier_Removal(model_dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.5) 
    ROR.fit(X,y)
    data_dict = {"train_ave": ROR.train_data_ave}
    CM = CM_ROR_predictions(data_exp.data, data_dict)["train_ave"]
    CM_actual = numpy.array([[n_out, 0],[0, N-n_out]])
    assert (CM == CM_actual).all()


def test_ROR_transform_ave():
    """
    Description
    -----------
    testing that the transform method correctly classifies all points it just fit, using a polynomial regressor.
    First have to create data using create_data class.
    """
    data_exp = create_regress_data()
    N, n_out = 500, 25
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    data_exp.set_X(x_min=-2, x_max=2, N=N, n_out=n_out, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=20, max_y=30)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    model_dict = {"PR": PR}
    ROR = Regression_Outlier_Removal(model_dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.5) 
    ROR.fit(X,y)
    ROR.transform(X,y)
    data_dict = {"test_ave": ROR.test_data_ave}
    CM = CM_ROR_predictions(data_exp.data, data_dict)["test_ave"]
    CM_actual = numpy.array([[n_out, 0],[0, N-n_out]])
    assert (CM == CM_actual).all()


def test_ROR_fit_and_transform_dicts():
    """
    Description
    -----------
    testing that when do ROR.fit(X,y) and get final prediction of outliers, this agrees with the ROR.transform(X,y), to within
    the percent_necessary threshold - because can't guarantee they'll be the same after every fit.  Checking this is true for every 
    model in self.models.  If it isn't, then doesn't mean anything is necessarily wrong with program, but wouldn't be good for 
    results.    First have to create data using create_data class.
    """
    data_exp = create_regress_data()
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    N, n_out = 500, 25
    data_exp.set_X(x_min=-2, x_max=2, N=N, n_out=n_out, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=20, max_y=30)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    LR = Linear_Regression()
    QR = Quadratic_Regression(quad_columns=["x_0"])
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    DTR_0 = Decision_Tree_Regression(min_samples_leaf=1)
    DTR_1 = Decision_Tree_Regression(min_samples_leaf=5)
    DTR_2 = Decision_Tree_Regression(min_samples_leaf=10)
    DTR_3 = Decision_Tree_Regression(min_samples_leaf=50)
    GBR = Gradient_Boost_Regression(min_samples_leaf=5, ccp_alpha=0.01)
    model_dict = {"LR": LR, "QR": QR, "PR": PR, "DTR_0": DTR_0, "DTR_1": DTR_1, "DTR_2": DTR_2, "DTR_3": DTR_3, "GBR": GBR}
    ROR = Regression_Outlier_Removal(model_dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.5) 
    ROR.fit(X,y)
    ROR.transform(X,y)
    for key in ROR.models:
        percent_match = (ROR.train_data[key][-1]["Outlying_Prediction"] == ROR.test_data[key][0]["Outlying_Prediction"]).sum()/N
        assert percent_match > ROR.percent_necessary


def test_ROR_cross_val_hist():
    """
    Just testing that cross_val_hist executes properly, outputting histograms for each of the folds and models, can't say if they're correct.
    """
    data_exp = create_regress_data()
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    data_exp.set_X(x_min=-2, x_max=2, N=1500, n_out=150, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=-40, max_y=40)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    LR = Linear_Regression()
    QR = Quadratic_Regression(quad_columns=["x_0"])
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    DTR_1 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.0001)
    DTR_2 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    DTR_3 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.1) 
    DTR_4 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=1)
    GBR = Gradient_Boost_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    Reg_Dict = {"LR": LR, "QR": QR, "PR": PR, "DTR_1":DTR_1, "DTR_2": DTR_2, "DTR_3": DTR_3, "DTR_4": DTR_4, "GBR":GBR}
    ROR = Regression_Outlier_Removal(Reg_Dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.50) 
    ROR.cross_val_hist(X, y, n_folds=2, n_bins=25)


def test_ROR_cross_val_scores():
    """
    Just testing that cross_val_scores executes properly, outputting dataframe of training and testing scores.  Can't say if they're correct.
    """
    data_exp = create_regress_data()
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    data_exp.set_X(x_min=-2, x_max=2, N=1500, n_out=150, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=-40, max_y=40)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    LR = Linear_Regression()
    QR = Quadratic_Regression(quad_columns=["x_0"])
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    DTR_1 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.0001)
    DTR_2 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    DTR_3 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.1) 
    DTR_4 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=1)
    GBR = Gradient_Boost_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    Reg_Dict = {"LR": LR, "QR": QR, "PR": PR, "DTR_1":DTR_1, "DTR_2": DTR_2, "DTR_3": DTR_3, "DTR_4": DTR_4, "GBR":GBR}
    ROR = Regression_Outlier_Removal(Reg_Dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.50) 
    ROR.cross_val_scores(X, y)


def test_ROR_res_hist():
    """
    just testing that the res_hist method works.  Can't say if it's right.
    """
    data_exp = create_regress_data()
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    data_exp.set_X(x_min=-2, x_max=2, N=1500, n_out=150, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=-40, max_y=40)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    LR = Linear_Regression()
    QR = Quadratic_Regression(quad_columns=["x_0"])
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    DTR_1 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.0001)
    DTR_2 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    DTR_3 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.1) 
    DTR_4 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=1)
    GBR = Gradient_Boost_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    Reg_Dict = {"LR": LR, "QR": QR, "PR": PR, "DTR_1":DTR_1, "DTR_2": DTR_2, "DTR_3": DTR_3, "DTR_4": DTR_4, "GBR":GBR}
    ROR = Regression_Outlier_Removal(Reg_Dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.50) 
    ROR.fit(X,y)
    data_dict = {"DTR_3": ROR.train_data["DTR_3"][-1], "PR": ROR.train_data["PR"][-1]}
    ROR.res_hist(data_dict, n_bins=25)


def test_ROR_outlier_overlap():
    """
    just testing that the outlier_overlap method outputs something.
    """
    data_exp = create_regress_data()
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    data_exp.set_X(x_min=-2, x_max=2, N=1500, n_out=150, dim=3)
    data_exp.set_y(func=f, dev=3, min_y=-40, max_y=40)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    LR = Linear_Regression()
    QR = Quadratic_Regression(quad_columns=["x_0"])
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    DTR_1 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.0001)
    DTR_2 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    DTR_3 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=0.1) 
    DTR_4 = Decision_Tree_Regression(min_samples_leaf=2, ccp_alpha=1)
    GBR = Gradient_Boost_Regression(min_samples_leaf=2, ccp_alpha=0.01)
    Reg_Dict = {"LR": LR, "QR": QR, "PR": PR, "DTR_1":DTR_1, "DTR_2": DTR_2, "DTR_3": DTR_3, "DTR_4": DTR_4, "GBR":GBR}
    ROR = Regression_Outlier_Removal(Reg_Dict, metric="IQR", factor=2, n_max=20, percent=0.99, window=4, threshold=0.50) 
    ROR.fit(X,y)
    data_dict = {"DTR_3": ROR.train_data["DTR_3"][-1], "PR": ROR.train_data["PR"][-1]}
    ROR.outlier_overlap(data_dict)










