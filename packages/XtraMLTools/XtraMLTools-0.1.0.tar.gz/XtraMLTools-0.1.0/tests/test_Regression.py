# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:04:09 2024

@author: atdou
"""


import pandas
from XtraMLTools.Regression import (Quadratic_Regression, Polynomial_Regression, Categorical_Linear_Regression, 
                                    Categorical_Quadratic_Regression, Categorical_Polynomial_Regression)
from auxiliary_classes import create_regress_data

# importing excel dataframe for testing
dataframe = pandas.read_excel("Test_Dataframes.xlsx", sheet_name = None)
df = dataframe["df"]
df_quad = dataframe["df_quad"]
df_poly = dataframe["df_poly"]
df_cat_lin = dataframe["df_cat_lin"]
df_cat_quad = dataframe["df_cat_quad"]
df_cat_poly = dataframe["df_cat_poly"]
X = df.drop("y", axis=1)
y = df["y"]    

# testing that the categorical columns, quad_columns, poly_columns are being constructed correctly from excel dataframe
def test_QR_fit():
    """
    Description
    -----------
    testing that QR is adding proper columns headings and values to excel dataframe
    """
    QR = Quadratic_Regression(quad_columns=["n1", "n2"])
    QR.fit(X,y)
    Truth_Table_1 = (QR.X_train == df_quad.drop("y", axis=1))
    assert Truth_Table_1.all().all() == True

def test_PR_fit():
    """
    Description
    -----------
    testing that PR is adding proper columns headings and values to excel dataframe
    """
    PR = Polynomial_Regression(poly_columns=["n1", "n2"], degree=3)
    PR.fit(X,y)
    Truth_Table_2 = (PR.X_train == df_poly.drop("y", axis=1))
    Truth_Table_2.all().all() == True

def test_CLR_fit():
    """
    Description
    -----------
    testing that CLR is adding proper columns headings and values to excel dataframe
    """
    CLR = Categorical_Linear_Regression(expand=["n1", "n2"], hues=[["c1b", "c1c"], ["c2b"]])  
    CLR.fit(X,y) 
    Truth_Table_3 = (CLR.X_train == df_cat_lin.drop("y", axis=1)) 
    assert Truth_Table_3.all().all() == True

def test_CQR_fit():
    """
    Description
    -----------
    testing that CQR is adding proper columns headings and values to excel dataframe
    """
    CQR = Categorical_Quadratic_Regression(quad_columns=["n1"], expand=["n1", "n2"], hues=[["c1b", "c1c"],["c2b"]])
    CQR.fit(X,y)
    Truth_Table_4 = (CQR.X_train == df_cat_quad.drop("y", axis=1))
    assert Truth_Table_4.all().all() == True

def test_CPR_fit_1():
    """
    Description
    -----------
    testing that CPR is adding proper columns headings and values to excel dataframe
    """
    CPR_1 = Categorical_Polynomial_Regression(expand=["n1", "n2"], hues=[["c1b", "c1c"],["c2b"]], degree=1)
    CPR_1.fit(X,y)
    Truth_Table_5 = (CPR_1.X_train == df_cat_lin.drop("y", axis=1))
    assert Truth_Table_5.all().all() == True

def test_CPR_fit_2():
    """
    Description
    -----------
    testing that CPR is adding proper columns headings and values to excel dataframe
    """
    CPR_2 = Categorical_Polynomial_Regression(poly_columns=["n1"], expand=["n1", "n2"], hues=[["c1b", "c1c"],["c2b"]], degree=2)
    CPR_2.fit(X,y)
    Truth_Table_6 = (CPR_2.X_train == df_cat_poly.drop("y", axis=1))
    assert Truth_Table_6.all().all() == True


# testing that the quadratic and polynomial regressions are being done correctly.  
def test_quad_coefs():
    """
    Description
    -----------
    testing that Quadratic_Regression guy is finding the correct regression coefficients, on 
    data with no outliers and no deviations from the fit, f.
    """
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**2 - 7*x[2]
    data_exp = create_regress_data()
    data_exp.set_X(x_min=-2, x_max=2, N=500, n_out=0, dim=3)
    data_exp.set_y(func=f, dev=0, min_y=0, max_y=0)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    QR = Quadratic_Regression(quad_columns=["x_0", "x_1", "x_2"])
    QR.fit(X,y)
    coefs = QR.coef_
    tol = 0.00001
    cond_1 = abs(coefs["x_0*x_0"]-10) < tol
    cond_2 = abs(coefs["x_0"]-5) < tol
    cond_3 = abs(coefs["x_1*x_1"]-4) < tol
    cond_4 = abs(coefs["x_2"]+7) < tol
    assert (cond_1 and cond_2 and cond_3 and cond_4)


def test_poly_coefs():
    """
    Description
    -----------
    testing that Polynomial_Regression guy is finding the correct regression coefficients, on 
    data with no outliers and no deviations from the fit, f.
    """
    f = lambda x: 10*(x[0])**2 + 5*x[0] + 4*x[1]**3 - 7*x[2]
    data_exp = create_regress_data()
    data_exp.set_X(x_min=-2, x_max=2, N=500, n_out=0, dim=3)
    data_exp.set_y(func=f, dev=0, min_y=0, max_y=0)
    data_exp.classify_outliers(metric="IQR", factor=2)
    X = data_exp.X
    y = data_exp.y
    PR = Polynomial_Regression(poly_columns=["x_0", "x_1", "x_2"], degree=3)
    PR.fit(X,y)
    coefs = PR.coef_
    tol = 0.00001
    cond_1 = abs(coefs["x_0*x_0"]-10) < tol
    cond_2 = abs(coefs["x_0"]-5) < tol
    cond_3 = abs(coefs["x_1*x_1*x_1"]-4) < tol
    cond_4 = abs(coefs["x_2"]+7) < tol
    assert (cond_1 and cond_2 and cond_3 and cond_4)






