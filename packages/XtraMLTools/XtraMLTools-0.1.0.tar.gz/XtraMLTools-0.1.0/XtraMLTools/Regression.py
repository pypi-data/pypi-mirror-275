# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:28:13 2024
@author: atdou
"""

import pandas
import numpy
from itertools import chain
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
#import tensorflow as tf
#from tensorflow import keras
#from keras.models import Sequential


class Linear_Regression():
    """
    Description
    -----------
    performs a linear regression, with option of Lasso regression if non-zero alpha.
    and then has a bunch of associated methods for analysis of prediction and fit.
    """
    def __init__(self, fit_intercept = True, alpha = 0, max_iter=1500):
        """
        Parameters
        ----------
        fit_intercept: Bool
            if True, then fits intercept, if False, then forces intercept through origin
        alpha: float
            this is the Lasso regression parameter; if zero, then get normal linear regression
        max_iter: int
            max iteractions
            
        Attributes
        ----------
        fit_intercept: Bool
            is just the above  fit_intercept parameter
        max_iter: int
            max number of iterations
        alpha: float
            the Lasso regression parameter.  alpha = 0 means employing Linear Regression
        intercept_: float
            once fit method employed, the intercept as determined by the regression program
        coef_: pandas Series
            once fit method employed, a series of X_train column heading: corresponding regression coefficient as determined by the regression program
        model: sklearn regression class
            if alpha = 0, then this is sklearn Linear Regression model; otherwise an sklearn Lasso Regression model

        res: pandas Series
            once res_hist method employed, a series of the residues = differences between y_test and y_pred
        """
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.alpha = alpha
        self.model = LinearRegression(fit_intercept = self.fit_intercept) if alpha==0 else \
            Lasso(fit_intercept=self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
        self.intercept_ = None
        self.coef_ = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.res = None
        
    def fit(self, X_train, y_train):
        """
        Description
        ----------
        fits X_train to y_train according to regression model specified by alpha, and works out the regression intercept, 
        coefficients
        
        Parameters
        ----------
        X_train: pandas dataframe
        y_train: pandas series

        Returns
        -------
        None
        """
        
        self.model.fit(X_train, y_train) 
        self.intercept_ = self.model.intercept_  
        self.coef_ = pandas.Series(self.model.coef_, index=X_train.columns)  

    def predict(self, X_test):
        """
        Description
        -----------
        returns prediction on X_test, i.e., y_pred
        
        Parameters
        ----------
        X_test: pandas dataframe

        Returns
        -------
        pandas series
        """
        return self.model.predict(X_test)
    
    def score(self, X_test, y_test):
        """
        Description
        -----------
        works out the fit score between X_test prediction and y_test.  
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series

        Returns
        -------
        float
            this is the R^2 value
        """
        
        return self.model.score(X_test, y_test)
    
    def res_hist(self, X_test, y_test, n_bins): 
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
        
    def cross_val_scores(self, X, y, n, r):
        """
        Description
        ----------
        splits data, X, into n parts.  trains on n-1 of the parts, tests on the nth part, and calculates the score,
        as determined from the score method.
        
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
        X = X.reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            X_train, y_train = X.loc[train_indices], y.loc[train_indices]
            X_test, y_test = X.loc[test_indices], y.loc[test_indices]            
            self.model.fit(X_train, y_train)
            cv_results["fold " + str(j)] = self.model.score(X_test, y_test)
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results
   


class Quadratic_Regression():
    """
    Description
    -----------
    expands the independent variable columns to include quadratic products of specified columns.  Then does a linear
    regression on it, or Lasso regression, depending on whether alpha is zero or not.  
    """
    def __init__(self, fit_intercept = True, quad_columns = [], alpha = 0, max_iter=1500):
        """
        Parameters
        ----------
        fit_intercept: Boolean
            if true, then fits intercept, else, fixes to zero.
        quad_columns: list
            list of column names in X_train to expand in quadratic product
        alpha: float
            if zero, then does linear regression; if non-zero, then Lasso regression.  The latter can be useful
            to nudge regression coefficients of expanded columns to zero, if they're not being predictive
        max_iter: int
            max iteractions
            
        Attributes
        -------
        fit_intercept: Boolean
        max_iter: int
        quad_columns: list
        intercept_: float
        coef_: pandas series
        model: sklearn regression class
        X_train: pandas dataframe
            once fit method is employed, this stores the augmented X_train dataframe with the extra quadratic columns.
        alpha: float
        res: pandas series      
        """
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.quad_columns = quad_columns
        self.alpha = alpha
        self.model = LinearRegression(fit_intercept = self.fit_intercept) if alpha==0 else \
            Lasso(fit_intercept=self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
        self.intercept_ = None
        self.coef_ = None
        self.X_train = None
        self.res = None
    def augment(self, X, quad_columns):
        """
        Description
        -----------
        takes columns in quad_columns = [a, b, c], and adds columns: a**2, b**2, c**2, ab, ac, bc
        This is a helper function employed by the fit method.
        
        Parameters
        ----------
        X: pandas dataframe
            could be X_train, or X_test
        quad_columns: list
            is a list of column names in dataframe that are to be expanded as outlined above.
            
        Returns
        -------
        pandas dataframe
            the dataframe X (could be X_train, X_test, whatever) augmented with the specified columns.
        """
        for i in range(len(quad_columns)):
            for j in range(i+1):
                X[quad_columns[i] + "*" + quad_columns[j]] = X[quad_columns[i]]*X[quad_columns[j]]
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
        X = self.augment(X_train.copy(), self.quad_columns)
        y = y_train.copy()
        self.model.fit(X, y)
        self.intercept_ = self.model.intercept_
        self.coef_ = pandas.Series(self.model.coef_, index = X.columns)
        self.X_train = X
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
        X = self.augment(X_test.copy(), self.quad_columns)
        return self.model.predict(X)
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
            this is the R^2 value
        """
        X = self.augment(X_test.copy(), self.quad_columns)
        y = y_test.copy()
        return self.model.score(X, y)
    def res_hist(self, X_test, y_test, n_bins):                     # bins can be number or list
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        X_test = self.augment(X_test.copy(), self.quad_columns)
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
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
        X = self.augment(X.copy(), self.quad_columns).reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0 
        for train_indices, test_indices in folds: 
            if self.alpha == 0: 
                model = LinearRegression(fit_intercept = self.fit_intercept) 
            else: 
                model = Lasso(fit_intercept = self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter) 
            model.fit(X.loc[train_indices], y.loc[train_indices]) 
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices]) 
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results




class Polynomial_Regression():
    """
    Description
    -----------
    expands the independent variable columns to include polynomial products of specified columns, out to specified order.  
    Then does a linear regression on it, or Lasso regression, depending on whether alpha is zero or not. 
    
    """
    def __init__(self, fit_intercept = True, poly_columns = [], degree = 1, alpha = 0, max_iter = 1500):
        """
        Parameters
        ----------
        fit_intercept: Boolean
            if true, then fits intercept, else, fixes to zero.
        max_iter: int
            max iterations
        poly_columns: list
            list of column names in X_train to expand in polynomial product, out to specified degree
        degree: int
            the order of the polynomial in aforementioned expansion
        alpha: float
            if zero, then does linear regression; if non-zero, then Lasso regression.  The latter can be useful
            to nudge regression coefficients of expanded columns to zero, if they're not being predictive

        Attributes
        -------
        fit_intercept: Boolean
        max_iter: int
        poly_columns: list
        intercept_: float
        coef_: pandas series
        model: sklearn regression class
        X_train: pandas dataframe
            once fit method is employed, this stores the augmented X_train dataframe with the extra quadratic columns.
        alpha: float
        res: pandas series      
        """
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.poly_columns = poly_columns
        self.degree = degree
        self.alpha = alpha
        self.model = LinearRegression(fit_intercept = self.fit_intercept) if alpha==0 else \
            Lasso(fit_intercept=self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
        self.intercept_ = None
        self.coef_ = None
        self.X_train = None
        self.res = None
    def augment(self, X, poly_columns, degree):
        """
        Description
        -----------
        takes columns in, say, poly_columns = [a, b, c], and adds unique columns of form (a**p)(b**q)(c**r) where p + q + r = degree.
        This is a helper function employed by the fit method.
        
        Parameters
        ----------
        X: pandas dataframe
            could be X_train, or X_test
        poly_columns: list
            is a list of column names in dataframe that are to be expanded as outlined above.
        degree: int
            the degree of the aforementioned polynomial
    
        Returns
        -------
        pandas dataframe
            the dataframe X (could be X_train, X_test, whatever) augmented with the specified columns.
        """
        def first_word(string):                         # this is for extracting the first column name of a column string, e.g., "col1*col2*col3", etc.
            if '*' not in string:                       # it's a helper function for unique_powers function
                return string
            else: 
                return string[0:string.find('*')]      
        def powers_columns(X, columns, degree):         # function finds all unique combinations of column names and their powers involved when raise the whole set of them to degree poewr.
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
        powers_columns(X, poly_columns, degree)
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
        X = self.augment(X_train.copy(), self.poly_columns, self.degree)
        y = y_train.copy()
        self.model.fit(X, y)
        self.intercept_ = self.model.intercept_
        self.coef_ = pandas.Series(self.model.coef_, index = X.columns)
        self.X_train = X
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
        X = self.augment(X_test.copy(), self.poly_columns, self.degree)
        return self.model.predict(X)
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
            this is the R^2 value
        """
        X = self.augment(X_test.copy(), self.poly_columns, self.degree)
        y = y_test.copy()
        return self.model.score(X, y)
    def res_hist(self, X_test, y_test, n_bins): 
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        X_test = self.augment(X_test.copy(), self.poly_columns, self.degree)
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
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
        X = self.augment(X.copy(), self.poly_columns, self.degree).reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {} 
        j = 0
        for train_indices, test_indices in folds:
            if self.alpha == 0:
                model = LinearRegression(fit_intercept = self.fit_intercept)
            else:
                model = Lasso(fit_intercept = self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results




class Categorical_Linear_Regression():
    """
    Description
    -----------
    this takes a dataframe whose categorical columns are all one-hot-encoded (with one column dropped).  hues is a list of feature 
    lists that we want to expand the expand columns in the dataframe on.  A feature list is a list of the one-hot-encoded column 
    names corresponding to the same feature.  The expand columns is a list column names, possibly including some or all of the
    hues columns, that we want to expand.  The algorithm starts by taking the first feature list columns out of the expand set, if 
    present, multiplying every remaining expand column by every column in the first feature list, and then appending these 
    columns to the original expand set. Then it takes the first and second feature list columns out of the new augmented expand set, 
    as present, and multiplies every remaining expand column in the new augmented expand set by every column in the second feature list, 
    and appends these columns to the augmented expand set. And this continues for every feature list in hues.  Finally, the 
    expand set is appended to the 'unexpanded' columns in the dataframe. This final augmented dataframe then has all columns in the expand
    set split by every possible combination of hue values.  Thus when linearly, regressed, we can get different slope and intercept
    coeffients for every 'hue' of all the values in the expand columns, whereas before, we would only get different intercepts.  
    """
    def __init__(self, fit_intercept = True, hues = [], expand = "all", alpha = 0, max_iter = 1500):
        """
        Parameters
        ----------
        fit_intercept: Boolean
            True if want to fit intercept, False if want to force it to zero
        max_iter: int
            max iterations
        hues: list of lists
            list of list of same-feature column names which we want to expand the expand columns on
        expand: list
            list of column names that we wanted expanded/differentiated by hue
        alpha: float
            is Lasso regression parameter.
            
        Attributes
        ----------
        fit_intercept: Boolean
        max_iter: int
        intercept_: float
            regression intercept
        coef_: pandas Series
            series mapping column heading: linear regression slope coefficient
        model: sklearn linear/Lasso regression model
        X_train: pandas dataframe
            once fit method is employed, the augmented X_train is stored here. 
        hues: list of lists
            list of the one-hot-encoded column names we want to expand the expand columns on.  Each sublist corresponds to the same
            feature.  looks like hues = [["f1_b", "f1_c"], ["f2_b"]], etc.
        expand: list
            list of one-hot-encoded column names we want to be expanded by hue.
        alpha: float
            Lasso regression parameter
        res: pandas Series
            stores residues y_test - y_pred            
        """
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.alpha = alpha
        self.hues = hues
        self.expand = expand
        self.model = LinearRegression(fit_intercept = fit_intercept) if alpha==0 else \
            Lasso(fit_intercept=self.fit_intercept, alpha = alpha, max_iter = self.max_iter)
        self.intercept_ = None
        self.coef_ = None
        self.X_train = None
        self.res = None
    def augment(self, X, hues, expand):
        """
        Description
        -----------
        this is a helper function/method for the fit method.  It augments the expand columns of the dataframe by the hue columns

        Parameters
        ----------
        X: pandas dataframe
        hues: list of list
        expand: list

        Returns
        -------
        pandas dataframe
            the augmented X
        """
        X = X.copy()
        X_added_columns = []                                        # keeping a list of all added columns to later winnow 
        for i in range(len(hues)):
            features = list(chain.from_iterable(hues[0:i+1]))       # this flattens hues array
            X_columns_to_remove = []                                # when multiplying df by feature in hues, have to first remove all columns in df that hvae been multiplyied by current or previous feature
            X_columns_to_add_dict = {}                              # this is dictionary of columns in reduced df * columns in feature that will be added to df
            for feature in features:
                    for X_column in X.columns:
                        if X_column[0:len(feature)] == feature:     # checking to see if X_column is a column that has already been multiplied by one of the features
                            X_columns_to_remove.append(X_column)    
            X_reduced = X.drop(X_columns_to_remove, axis=1)
            X_columns_to_multiply_X_reduced_by = hues[i]
            for X_column_to_multiply_X_reduced_by in X_columns_to_multiply_X_reduced_by:
                for X_reduced_column in X_reduced.columns:
                    X_column_to_add_name = "{:s}*{:s}".format(X_reduced_column, X_column_to_multiply_X_reduced_by)
                    X_columns_to_add_dict[X_column_to_add_name] = X[X_reduced_column]*X[X_column_to_multiply_X_reduced_by]
                    X_added_columns.append(X_column_to_add_name)    
            X_columns_to_add = pandas.DataFrame(X_columns_to_add_dict)
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
        X = self.augment(X_train.copy(), self.hues, self.expand)
        y = y_train.copy()
        self.model.fit(X, y)
        self.intercept_ = self.model.intercept_
        self.coef_ = pandas.Series(self.model.coef_, index=X.columns)
        self.X_train = X
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
        X = self.augment(X_test.copy(), self.hues, self.expand)
        return self.model.predict(X)
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
            this is the R^2 value
        """
        X = self.augment(X_test.copy(), self.hues, self.expand)
        y = y_test.copy()
        return self.model.score(X, y)
    def res_hist(self, X_test, y_test, n_bins):
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        X_test = self.augment(X_test.copy(), self.hues, self.expand)
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
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
        X = self.augment(X.copy(), self.hues, self.expand).reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            if self.alpha == 0:
                model = LinearRegression(fit_intercept = self.fit_intercept)
            else:
                model = Lasso(fit_intercept = self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results




class Categorical_Quadratic_Regression():
    """
    Description
    -----------
    this takes a dataframe whose categorical columns are all one-hot-encoded (with one column dropped).  then the columns in 
    quad_columns are expanded quadraticaly, as described above.  hues is a list of feature lists that we want to expand the expand 
    columns in the dataframe on.  A feature list is a list of the one-hot-encoded column names corresponding to the same feature.  
    The expand columns is a list column names, possibly including some or all of the hues columns, that we want to expand.  The algorithm 
    starts by taking the first feature list columns out of the expand set, if present, multiplying every remaining expand column by every 
    column in the first feature list, and then appending these columns to the original expand set. Then it takes the first and second 
    feature list columns out of the new augmented expand set, as present, and multiplies every remaining expand column in the new augmented 
    expand set by every column in the second feature list, and appends these columns to the augmented expand set. And this continues for 
    every feature list in hues.  Finally, the expand set is appended to the 'unexpanded' columns in the dataframe. This final augmented 
    dataframe then has all columns in the expand set split by every possible combination of hue values.  Thus when linearly, regressed, 
    we can get different slope and intercept coeffients for every 'hue' of all the values in the expand columns, whereas before, we would 
    only get different intercepts.  
    """
    def __init__(self, fit_intercept = True, quad_columns = [], hues = [], expand = "all", alpha = 0, max_iter = 1500):
        """
        Parameters
        ----------
        fit_intercept: Boolean
            True if want to fit intercept, False if want to force it to zero
        max_iter: int
            max iterations
        quad_columns: list
            list of numerical column names that we wanted expanded quadratically
        hues: list of lists
            list of list of same-feature column names which we want to expand the expand columns on
        expand: list
            list of column names that we wanted expanded/differentiated by hue
        alpha: float
            is Lasso regression parameter.
            
        Attributes
        ----------
        fit_intercept: Boolean
        max_iter: int
        quad_columns: list
        intercept_: float
            the regression intercept
        coef_: pandas Series
            series mapping column heading: linear regression slope coefficient
        model: sklearn linear/Lasso regression model
        X_train: pandas dataframe
            once fit method is employed, the augmented X_train is stored here. 
        hues: list of lists
            list of the one-hot-encoded column names we want to expand the expand columns on.  Each sublist corresponds to the same
            feature.  looks like hues = [["f1_b", "f1_c"], ["f2_b"]], etc.
        expand: list
            list of one-hot-encoded column names we want to be expanded by hue.
        alpha: float
            Lasso regression parameter
        res: pandas Series
            stores residues y_test - y_pred            
        """
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.quad_columns = quad_columns
        self.hues = hues
        self.expand = expand
        self.alpha = alpha
        self.model = LinearRegression(fit_intercept = self.fit_intercept) if alpha==0 else \
            Lasso(fit_intercept=self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
        self.intercept_ = None
        self.coef_ = None
        self.X_train = None
        self.res = None
    def augment(self, X, quad_columns, hues, expand):
        """
        Description
        -----------
        this is a helper function/method for the fit method.  It augments the quad columns quadratically.  And then augments the 
        expand columns of the dataframe by the hue columns

        Parameters
        ----------
        X: pandas dataframe
        quad_columns: list
        hues: list of list
        expand: list

        Returns
        -------
        pandas dataframe
            the augmented X
        """
        for i in range(len(quad_columns)):
            for j in range(i+1):
                X[quad_columns[i] + "*" + quad_columns[j]] = X[quad_columns[i]]*X[quad_columns[j]]
        X_added_columns = []                                        # now doing categorical augment. keeping a list of all added columns to later winnow 
        for i in range(len(hues)):
            features = list(chain.from_iterable(hues[0:i+1]))       # this flattens hues array
            X_columns_to_remove = []                                # when multiplying df by feature in hues, have to first remove all columns in df that hvae been multiplyied by current or previous feature
            X_columns_to_add_dict = {}                              # these are columns in reduced df * columns in feature that will be added to df
            for feature in features:
                    for X_column in X.columns:
                        if X_column[0:len(feature)] == feature:     # checking to see if X_column is a column that has already been multiplied by one of the features
                            X_columns_to_remove.append(X_column)    
            X_reduced = X.drop(X_columns_to_remove, axis=1)
            X_columns_to_multiply_X_reduced_by = hues[i]
            for X_column_to_multiply_X_reduced_by in X_columns_to_multiply_X_reduced_by:
                for X_reduced_column in X_reduced.columns:
                    X_column_to_add_name = "{:s}*{:s}".format(X_reduced_column, X_column_to_multiply_X_reduced_by)
                    X_columns_to_add_dict[X_column_to_add_name] = X[X_reduced_column]*X[X_column_to_multiply_X_reduced_by]
                    X_added_columns.append(X_column_to_add_name)    
            X_columns_to_add = pandas.DataFrame(X_columns_to_add_dict)
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
        X = self.augment(X_train.copy(), self.quad_columns, self.hues, self.expand)
        y = y_train.copy()
        self.model.fit(X, y)
        self.intercept_ = self.model.intercept_
        self.coef_ = pandas.Series(self.model.coef_, index = X.columns)
        self.X_train = X
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
        X = self.augment(X_test.copy(), self.quad_columns, self.hues, self.expand)
        return self.model.predict(X)
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
            this is the R^2 value
        """
        X = self.augment(X_test.copy(), self.quad_columns, self.hues, self.expand)
        y = y_test.copy()
        return self.model.score(X, y)
    def res_hist(self, X_test, y_test, n_bins):                     # bins can be number or list
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        X_test = self.augment(X_test.copy(), self.quad_columns, self.hues, self.expand)
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
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
        X = self.augment(X.copy(), self.quad_columns, self.hues, self.expand).reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            if self.alpha == 0:
                model = LinearRegression(fit_intercept = self.fit_intercept)
            else:
                model = Lasso(fit_intercept = self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results




class Categorical_Polynomial_Regression():
    """
    Description
    -----------
    this takes a dataframe whose categorical columns are all one-hot-encoded (with one column dropped).  then the numeric columns in 
    poly_columns are expanded polynomially, e.g., (a,b) --> (a**3, a**2*b, a**2*c, a*b**2, a*b*c, a*c**2, b**3, b**2*c, b*c**2, c**3) if 
    degree = 3.   hues is a list of feature lists that we want to expand the expand columns in the dataframe on.  A feature list is a list 
    of the one-hot-encoded column names corresponding to the same feature.  The expand columns is a list column names, possibly including 
    some or all of the hues columns, that we want to expand.  The algorithm starts by taking the first feature list columns out of the 
    expand set, if present, multiplying every remaining expand column by every column in the first feature list, and then appending these 
    columns to the original expand set. Then it takes the first and second feature list columns out of the new augmented expand set, as present, 
    and multiplies every remaining expand column in the new augmented expand set by every column in the second feature list, and appends these 
    columns to the augmented expand set. And this continues for every feature list in hues.  Finally, the expand set is appended to the 'unkept' 
    columns in the dataframe. This final augmented dataframe then has all columns in the expand set split by every possible combination of hue 
    values.  Thus when linearly, regressed, we can get different slope and intercept coeffients for every 'hue' of all the values in the 
    expand columns, whereas before, we would only get different intercepts.  
    """
    def __init__(self, fit_intercept = True, poly_columns = [], degree = 1, hues = [], expand = "all", alpha = 0, max_iter = 1500):
        """
        Parameters
        ----------
        fit_intercept: Boolean
            True if want to fit intercept, False if want to force it to zero
        max_iter: int
            max iterations
        poly_columns: list
            list of numerical column names that we wanted expanded polynomially
        degree: int
            degree of the desired polynomial
        hues: list of lists
            list of list of same-feature column names which we want to expand the expand columns on
        expand: list
            list of column names that we wanted expanded/differentiated by hue
        alpha: float
            is Lasso regression parameter.
            
        Attributes
        ----------
        fit_intercept: Boolean
        max_iter: int
        poly_columns: list
        degree: int
            the degree of the desired polynomial
        intercept_: float
            the regression intercept
        coef_: pandas Series
            series mapping column heading: linear regression slope coefficient
        model: sklearn linear/Lasso regression model
        X_train: pandas dataframe
            once fit method is employed, the augmented X_train is stored here. 
        hues: list of lists
            list of the one-hot-encoded column names we want to expand the expand columns on.  Each sublist corresponds to the same
            feature.  looks like hues = [["f1_b", "f1_c"], ["f2_b"]], etc.
        expand: list
            list of one-hot-encoded column names we want to be expanded by hue.
        alpha: float
            Lasso regression parameter
        res: pandas Series
            stores residues y_test - y_pred            
        """
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.poly_columns = poly_columns
        self.degree = degree
        self.hues = hues
        self.expand = expand
        self.alpha = alpha
        self.model = LinearRegression(fit_intercept = self.fit_intercept) if alpha==0 else \
            Lasso(fit_intercept=self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
        self.intercept_ = None
        self.coef_ = None
        self.X_train = None
        self.res = None
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
        powers_columns(X, poly_columns, degree)
        X_added_columns = []                                        # now doing categorical augment. keeping a list of all added columns to later winnow 
        for i in range(len(hues)):
            features = list(chain.from_iterable(hues[0:i+1]))       # this flattens hues array
            X_columns_to_remove = []                                # when multiplying df by feature in hues, have to first remove all columns in df that hvae been multiplyied by current or previous feature
            X_columns_to_add_dict = {}                              # these are columns in reduced df * columns in feature that will be added to df
            for feature in features:
                    for X_column in X.columns:
                        if X_column[0:len(feature)] == feature:     # checking to see if X_column is a column that has already been multiplied by one of the features
                            X_columns_to_remove.append(X_column)    
            X_reduced = X.drop(X_columns_to_remove, axis=1)
            X_columns_to_multiply_X_reduced_by = hues[i]
            for X_column_to_multiply_X_reduced_by in X_columns_to_multiply_X_reduced_by:
                for X_reduced_column in X_reduced.columns:
                    X_column_to_add_name = "{:s}*{:s}".format(X_reduced_column, X_column_to_multiply_X_reduced_by)
                    X_columns_to_add_dict[X_column_to_add_name] = X[X_reduced_column]*X[X_column_to_multiply_X_reduced_by]
                    X_added_columns.append(X_column_to_add_name)    
            X_columns_to_add = pandas.DataFrame(X_columns_to_add_dict)
            X = pandas.concat([X, X_columns_to_add], axis=1) 
        if expand == "all":                                          # now dropping all columns split by hues that aren't in expand
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
        X = self.augment(X_train.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        y = y_train.copy()
        self.model.fit(X, y)
        self.intercept_ = self.model.intercept_
        self.coef_ = pandas.Series(self.model.coef_, index = X.columns)
        self.X_train = X
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
        X = self.augment(X_test.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        return self.model.predict(X)
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
            this is the R^2 value
        """
        X = self.augment(X_test.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        y = y_test.copy()
        return self.model.score(X, y)
    def res_hist(self, X_test, y_test, n_bins): 
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        X_test = self.augment(X_test.copy(), self.poly_columns, self.degree, self.hues, self.expand)
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
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
            if self.alpha == 0:
                model = LinearRegression(fit_intercept = self.fit_intercept)
            else:
                model = Lasso(fit_intercept = self.fit_intercept, alpha = self.alpha, max_iter = self.max_iter)
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results


class Decision_Tree_Regression():
    """
    Description
    -----------
    This class enfolds some useful features within sklearn's decision tree regressor class.  
    Trying to make it have the same methods and things as the other classes above.
    """
    def __init__(self, min_samples_leaf=5, ccp_alpha=0):
        """
        Parameters
        ----------
        min_samples_leaf: int
        ccp_alpha: float
        
        Attributes
        ----------
        min_samples_leaf: int
        ccp_alpha: float
        feature_importances: pandas Series
            maps column nmaes to importances
        model: sklearn Decision Tree Regressor
        X_train: pandas dataframe
        res: pandas Series 
            series of residues y_test - y_pred
        """
        self.min_samples_leaf = min_samples_leaf 
        self.ccp_alpha = ccp_alpha 
        self.feature_importances = None 
        self.model = DecisionTreeRegressor(min_samples_leaf=min_samples_leaf, ccp_alpha=ccp_alpha) 
        self.X_train = None 
        self.res = None
    def fit(self, X_train, y_train):
        """
        Description
        -----------
        fits X_train to y_train and determines and works out feature importances
        
        Parameters
        ----------
        X_train: pandas dataframe
        y_train: pandas series
        
        Returns
        -------
        None
        """
        self.model.fit(X_train, y_train) 
        self.X_train = X_train
        self.feature_importances = pandas.Series(self.model.feature_importances_, index=self.X_train.columns)
    def predict(self, X_test):
        """
        Parameters
        ----------
        X_test: pandas dataframe

        Returns
        -------
        pandas series
        """
        return self.model.predict(X_test)
    def score(self, X_test, y_test):
        """
        Description
        -----------
        works out the fit score between X_test prediction and y_test.  
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series

        Returns
        -------
        float
            this is the R^2 value
        """
        return self.model.score(X_test, y_test)
    def res_hist(self, X_test, y_test, n_bins):
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
    def cross_val_scores(self, X, y, n, r):
        """
        Description
        ----------
        Splits, X, y, into n parts.  trains on n-1 of the parts, 
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
        X = X.copy().reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            model = self.model
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        self.X_train = X
        return cv_results



class Gradient_Boost_Regression():
    """
    Description
    -----------
    This class enfolds some useful features within sklearn's gradient boost regressor class.  
    Trying to make it have the same methods and things as the other classes above.
    """
    def __init__(self, min_samples_leaf=5, ccp_alpha=0):
        """
        Parameters
        ----------
        min_samples_leaf: int
        ccp_alpha: float
        
        Attributes
        ----------
        min_samples_leaf: int
        ccp_alpha: float
        feature_importances: pandas Series
            maps column nmaes to importances
        model: sklearn Gradient Boost Regressor
        X_train: pandas dataframe
        res: pandas Series 
            series of residues y_test - y_pred
        """
        self.min_samples_leaf = min_samples_leaf 
        self.ccp_alpha = ccp_alpha 
        self.feature_importances = None 
        self.model = GradientBoostingRegressor(min_samples_leaf=min_samples_leaf, ccp_alpha=ccp_alpha) 
        self.X_train = None 
        self.res = None
    def fit(self, X_train, y_train):
        """
        Description
        -----------
        fits X_train to y_train and determines and works out feature importances
        
        Parameters
        ----------
        X_train: pandas dataframe
        y_train: pandas series
        
        Returns
        -------
        None
        """
        self.model.fit(X_train, y_train) 
        self.X_train = X_train
        self.feature_importances = pandas.Series(self.model.feature_importances_, index=self.X_train.columns)
    def predict(self, X_test):
        """
        Parameters
        ----------
        X_test: pandas dataframe

        Returns
        -------
        pandas series
        """
        return self.model.predict(X_test)
    def score(self, X_test, y_test):
        """
        Description
        -----------
        works out the fit score between X_test prediction and y_test.  
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series

        Returns
        -------
        float
            this is the R^2 value
        """
        return self.model.score(X_test, y_test)
    def res_hist(self, X_test, y_test, n_bins):
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
    def cross_val_scores(self, X, y, n, r):
        """
        Description
        ----------
        Splits, X, y, into n parts.  trains on n-1 of the parts, 
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
        X = X.copy().reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            model = self.model
            model.fit(X.loc[train_indices], y.loc[train_indices])
            cv_results["fold " + str(j)] = model.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        self.X_train = X
        return cv_results


class Neural_Net_Regression():
    """
    Description
    -----------
    This class enfolds some useful features within keras' sequential neural net class.  
    Trying to make it have the same methods and things as the other classes above.
    """
    def __init__(self, layers = [], activation = "relu", epochs=500, batch_size = 50,\
                 optimizer="Adam", alpha=0.01, loss_function="mean_squared_error", metric="mean_squared_error"):        
        """     
        Description
        -----------
        Instatiates a Keras.Sequential() model, and then constructs the network architecture through specification of the 
        layers and activation function.  Then compiles the model with information provided about the optimizer, alpha, 
        loss function, and metric.  The opochs, and batch size are used later in the fit method.  
        
        Parameters
        ----------
        layers: list
            has the form layers = [input_layer, hidden_layer_1, hidden_layer_2, ..., hidden_layer_n].  
            input_layer must have the same dimensionality as X.  hidden_layer_n must have same dimensionality as y.
            These go into the model.add(keras.layers.Dense()) method.  
        activation: string
            this specifies the activation function used in the Keras compile method.  There is an activation function(s) 
            after every hidden layer. This goes into the keras.layers.Dense() method.
        epochs: int
            number of iterations over entire X data set.
        batch_size: int
            number of data points used per each iteration of the solver routine
        optimizer: string
            Basically doing either Adam or SGD as optimizer in Keras compile method.
        alpha: float
            the learning rate going into the specified optimizer, which goes into the Keras compile method.
        loss_function: string
            specifies the loss function used in Keras compile method.
        metric: string
            specifies the metric used in Keras compile method.

        Attributes
        ----------
        layers: list
        activation: string
        optimizer: string
        alpha: float
        loss_function: string
        metric: string
        model: Keas Sequential NN model
        epochs: int
        batch_size: int
        X_train: pandas dataframe
        res: pandas series
            will store the residues y_test - y_pred.  
        """
        self.layers = layers
        self.activation = activation
        if optimizer == "Adam":
            self.optimizer = tf.keras.optimizers.Adam(learning_rate=alpha)
        if optimizer == "SGD":
            self.optimizer = tf.keras.optimizers.SGD(learning_rate=alpha)
            print(alpha)
        self.alpha = alpha
        self.loss_function = loss_function
        self.metric = metric
        self.model = Sequential()
        for n in range(1,len(layers)):
            self.model.add(keras.layers.Dense(input_shape=(layers[n-1],), units=layers[n], activation=activation))
            self.model.add(keras.layers.Dropout(0.0))
        self.model.compile(optimizer=optimizer, loss=loss_function, metrics=metric)
        self.epochs = epochs
        self.batch_size = batch_size
        self.X_train = None        
        self.res = None
    def fit(self, X_train, y_train):
        """
        Description
        -----------
        fits X_train to y_train
        
        Parameters
        ----------
        X_train: pandas dataframe
        y_train: pandas series
        
        Returns
        -------
        None
        """
        self.X_train = X_train
        self.model.fit(X_train.values, y_train.values, epochs=self.epochs, batch_size=self.batch_size)
    def predict(self, X_test):
        """
        Parameters
        ----------
        X_test: pandas dataframe

        Returns
        -------
        pandas series
        """
        return self.model.predict(X_test)
    def score(self, X_test, y_test):
        """
        Description
        -----------
        works out the fit score between X_test prediction and y_test.  
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series

        Returns
        -------
        float
            this is the R^2 value
        """
        y_pred = self.model.predict(X_test)
        return r2_score(y_test, y_pred)
    def res_hist(self, X_test, y_test, n_bins):  
        """
        Description
        -----------
        This creates a histogram of the residues = y_test - y_pred.  We can of course use X_train, y_train here instead.
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        n_bins: int, list
            this can be either number of bins for the histogram, or a list of partition points
        
        Returns
        -------
        histogram
        """
        from matplotlib import pyplot
        self.res = y_test - self.model.predict(X_test)
        pyplot.hist(self.res, bins = n_bins)
        pyplot.ylabel("count")
        pyplot.xlabel("residue")
        pyplot.title("Residue Histogram")
        pyplot.show()
    def cross_val_scores(self, X, y, n, r, epochs=100, batch_size=50): 
        """
        Description
        ----------
        Splits, X, y, into n parts.  trains on n-1 of the parts, tests on the nth part, and calculates the score.  
        Then repeats n-1 more times for each of the different folds, and creates dictionary of scores, as determined from the 
        score method.  And using self.model.fit() instead of self.fit() so as to start from whatever training weights we ended up 
        with in the self.fit() method.  
        
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
        epochs: int
            number of epochs for the fit method
        batch_size: int
            batch size for the fit method
            
        Returns
        -------
        dictionary
            looks like {"fold 0": score 1, "fold 1": score 2, ..., "fold n": score n, "average": average of scores}
        """
        X = X.copy().reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n, shuffle=True, random_state = r)
        folds = kf.split(X)
        cv_results = {}
        j = 0
        for train_indices, test_indices in folds:
            self.model.fit(X.loc[train_indices], y.loc[train_indices], epochs=epochs, batch_size=batch_size)
            cv_results["fold " + str(j)] = self.score(X.loc[test_indices], y.loc[test_indices])
            j+=1
        cv_results["average"] = numpy.mean(list(cv_results.values()))
        return cv_results


