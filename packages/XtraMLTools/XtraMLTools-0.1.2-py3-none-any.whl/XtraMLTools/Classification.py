# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:54:03 2024

@author: atdou
"""


import pandas
import numpy
from itertools import chain
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold

class Categorical_Polynomial_Logistic_Regression():
    """
    Description
    -----------
    this takes a dataframe whose categorical columns are all one-hot-encoded (with one column dropped).  then the numeric columns in 
    poly_columns are expanded polynomially, e.g., (a,b) --> (a**3, a**2*b, a**2*c, a*b**2, a*b*c, a*c**2, b**3, b**2*c, b*c**2, c**3) if 
    degree = 3.  hues is a list of feature lists that we want to expand the expand columns in the dataframe on.  A feature list is a list 
    of the one-hot-encoded column names corresponding to the same feature.  The expand columns is a list of column names, possibly including 
    some or all of the hues columns, that we want to expand. The algorithm starts by taking the first feature list columns out of the 
    expand set, if present, then multiplying every remaining expand column by every column in the first feature list, and then appending these 
    columns to the original expand set. Then it takes the first and second feature list columns out of the new augmented expand set, as 
    present, and multiplies every remaining expand column in the new augmented expand set by every column in the second feature list, and 
    appends these columns to the augmented expand set. And this continues for every feature list in hues.  Finally, the expand set is appended 
    to the 'unexpanded' columns in the dataframe. This final augmented dataframe then has all columns in the expand set split by every possible 
    combination of hue values.  Thus when logistically linearly regressed, we can get in the exponential function, a different slope and 
    intercept coeffients for every 'hue' of all the values in the expand columns, whereas before, we would only get different intercepts.  
    """
    def __init__(self, poly_columns = [], degree = 1, hues = [], expand = "all", C = 1, penalty = "l1", solver = "saga", max_iter=2000):
        """
        Parameters
        ----------
        poly_columns: list
            list of numerical column names that we wanted expanded polynomially
        degree: int
            degree of the desired polynomial
        hues: list of lists
            list of list of same-feature column names which we want to expand the expand columns on
        expand: list
            list of column names that we wanted expanded/differentiated by hue.  default "all" means all columns.
        C: int
            the C parameter in sklearn's logistic regression class
        penalty: string
            the penalty in sklearn's logistic regression class.  can be L1 or L2
        solver: string
            the solver in sklearn's logistic regression class'
        max_iter: int
            maximum number of iterations (SGD?) that sklearn's solver will run

        Attributes
        ----------
        poly_columns: list
        degree: int
            the degree of the desired polynomial
        intercept_: float
            the regression intercept
        coef_: pandas Series
            series mapping column heading: logistic regression slope coefficient (the coefficient of column in the exponential)
        model: sklearn logistic regression model
        X_train: pandas dataframe
            once fit method is employed, the augmented X_train is stored here. 
        hues: list of lists
            list of the one-hot-encoded column names we want to expand expand columns on.  Each sublist corresponds to the same
            feature.  looks like hues = [["f1_b", "f1_c"], ["f2_b"]], etc.
        expand: list
            list of one-hot-encoded column names we want to be expanded by hue.
        C: float
        max_iter: int
        penalty: string
        solver: string
        """
        self.poly_columns = poly_columns
        self.degree = degree
        self.intercept_ = None
        self.coef_ = None
        self.model = None
        self.X_train = None
        self.hues = hues
        self.expand = expand
        self.C = C
        self.max_iter = max_iter
        self.penalty = penalty
        self.solver = solver

    def augment(self, X, poly_columns, degree, hues, expand):
        """
        Description
        -----------
        this is a helper function/method for the fit method.  It augments the quad columns quadratically.  And then augments the 
        expand columns of the dataframe by the hue columns

        Parameters
        ----------
        X: pandas dataframe
        poly_columns: list
        degree: int
        hues: list of list
        expand: list

        Returns
        -------
        pandas dataframe
            the augmented X
        """
        def first_word(string):                         # this is for extracting the first column name of a column string, e.g., "col1*col2*col3", etc.
            if '*' not in string:                       # it's a helper function for unique_powers function
                return string
            else: 
                return string[0:string.find('*')]      
        def powers_columns(X, columns, degree):            # function finds all unique combinations of column names and th4ir powers involved when raise the whole set of them to degree poewr.
            if degree == 1:
                return columns
            else:
                previous_powers_columns = powers_columns(X, columns, degree-1)
                new_powers = []
                for elem_c in columns:
                    for elem_t in previous_powers_columns:
                        if columns.index(elem_c) <= columns.index(first_word(elem_t)):
                            new_powers.append("{:s}*{:s}".format(elem_c, elem_t))
                            X["{:s}*{:s}".format(elem_c, elem_t)] = X[elem_c]*X[elem_t]
                return new_powers   
        if type(X) == numpy.ndarray:
            columns = ["c{:d}".format(n) for n in range(len(X[0]))]
            X = pandas.DataFrame(X, columns=columns)
        powers_columns(X, poly_columns, degree)
        X_added_columns = []                                        # now doing categorical augment. expanding a list of all added columns to later winnow 
        for i in range(len(hues)):
            features = list(chain.from_iterable(hues[0:i+1]))       # this flattens hues array
            X_columns_to_remove = []                                # when multiplying df by feature in hues, have to first remove all columns in df that hvae been multiplyied by current or previous feature
            X_columns_to_add = pandas.DataFrame()                   # these are columns in reduced df * columns in feature that will be added to df
            for feature in features:
                    for X_column in X.columns:
                        if X_column[0:len(feature)] == feature:     # checking to see if X_column is a column that has already been multiplied by one of the features
                            X_columns_to_remove.append(X_column)    
            X_reduced = X.drop(X_columns_to_remove, axis=1)
            X_columns_to_multiply_X_reduced_by = hues[i]
            for X_column_to_multiply_X_reduced_by in X_columns_to_multiply_X_reduced_by:
                for X_reduced_column in X_reduced.columns:
                    X_column_to_add_name = "{:s}*{:s}".format(X_reduced_column, X_column_to_multiply_X_reduced_by)
                    X_columns_to_add[X_column_to_add_name] = X[X_reduced_column]*X[X_column_to_multiply_X_reduced_by]
                    X_added_columns.append(X_column_to_add_name)    
            X = pandas.concat([X, X_columns_to_add], axis=1) 
        if expand == "all":                                           # now dropping all columns split by hues that aren't in expand
            return X
        else:
            drop_list = []
            for X_added_column in X_added_columns:
                drop = True
                for expand_column in expand:
                    if X_added_column[0:len(expand_column)] == expand_column: # checking that X_column name starts with expand_column name
                        drop = False
                        break
                if drop == True:
                    drop_list.append(X_added_column)
            X.drop(drop_list, axis=1, inplace=True)
        return X 
    
    def fit(self, X_train, y_train):
        """
        Description
        ----------
        augments X_train using augment method, and fits previously specified regression model to y_train.
        Then works out the regression intercept, coefficients
        
        Parameters
        ----------
        X_train: pandas dataframe
        y_train: pandas series

        Returns
        -------
        None
        """
        X_train = self.augment(X_train.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        y_train = y_train.copy()
        self.model = LogisticRegression(C = self.C, penalty = self.penalty, solver = self.solver, max_iter=self.max_iter)
        self.model.fit(X_train, y_train)
        self.intercept_ = self.model.intercept_
        self.coef_ = pandas.Series(self.model.coef_[0], index = X_train.columns)
        self.X_train = X_train
        
    def predict(self, X_test):
        """
        Description
        -----------
        augments X_test according to augment method.  Then returns prediction on X_test, i.e., y_pred
        
        Parameters
        ----------
        X_test: pandas dataframe

        Returns
        -------
        pandas series
        """
        X_test = self.augment(X_test.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        return self.model.predict(X_test)                                      # need to convert to numpy array if such output is expected

    def score(self, X_test, y_test):
        """
        Description
        -----------
        augments X_test according to augment method.  Then works out the fit score between X_test prediction and y_test.  
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series

        Returns
        -------
        float
            this is the accuracy score presumably
        """
        X_test = self.augment(X_test.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        y_test = y_test.copy()
        return self.model.score(X_test, y_test)

    def cross_val_scores(self, X, y, n, r):
        """
        Description
        ----------
        augments X according to specifications above, then splits, X, y, into n parts.  trains on n-1 of the parts, 
        tests on the nth part, and calculates the score.  Then repeats n-1 more times for each of the different folds.
        and creates dictionary of scores, as determined from the score method.
        
        Parameters
        ----------
        X: pandas dataframe
            this is probably the original entire dataset independent variables
        y: pandas series
            this is also the original entire dataset dependent variables, probably
        n: int
            the number of cross validation folds
        r: int
            a random state seed
        
        Returns
        -------
        dictionary
            looks like {"fold 0": score 1, "fold 1": score 2, ..., "fold n": score n, "average": average of scores}
        """
        X = self.augment(X.copy(), self.poly_columns, self.degree, self.hues, self.expand).reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            model = LogisticRegression(C = self.C, penalty = self.penalty, solver = self.solver, max_iter = self.max_iter)
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results

