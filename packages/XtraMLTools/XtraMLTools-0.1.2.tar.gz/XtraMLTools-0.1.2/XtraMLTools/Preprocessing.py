# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:55:15 2024

@author: atdou
"""

import numpy, pandas, seaborn
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
from matplotlib import pyplot


class Regression_Outlier_Removal():
    """
    Description
    -----------
    class will fit a list of regression models to data.  For each model, runs a regression through the data, 
    identifies outliers, temporarily removes them, fit another regression, puts the temporary outliers back in 
    and reclassifiers outliers.  It repeats this process until the outlier classifications match within the 
    specified percent_match. It creates a pandas DataFrame of each model's predictions, residuals and outlier 
    classifications.  Then it averages the results of all the models as the final output.  Another option is to define
    a model (outside this class) which aggregates the predictions of the models in the list, and returns a single 
    prediction.  Then could pass that single aggregate model in this class.  That way we'd see the difference between
    taking the average of the classifications vs. classifying the average aggregate prediction.
    """
    def __init__(self, models, metric, factor, n_max, percent, window, threshold):
        """
        Parameters
        ----------
        models: a dictionary of regressor classes
        metric: string
            can be "std", or "IQR"
        factor: float
            the factor by which the metric is multiplied.  So if metric = "std", and factor = 3, then points outside 
            mean +/- 3*std will be classified as outliers.  If metric = "IQR", and factor = 2, then points less than 
            Q[1] - 2*IQR, or greater than Q[3] + 2*IQR will so classified. 
        n_max: int
            maximum number of iterations for solver to run through before quitting, if hasn't yet converged.
        percent: float
            the acceptable percentage match of outlier classifications between successive iterations of fit_per_model function.
            Must be between 0 and 1.
        window: int
            the number of successive iterations of the fit_per_model function that must output an acceptable percentage
            match before quitting.
        threshold: float
            smallest fraction of classifiers that must agree on outlier classification for classification
            to be accepted.

        Attributes
        ----------
        models: dictionary of regression classes
        length: int
        metric: string
        factor: float
        n_max: int
        percent_necessary: float
        window: int
        threshold: float
        train_n: dictionary of ints
            the number of iterations the solver took to exit, for each model in models.
        train_percent: dictionary of floats
            the final percent match between successive solver runs, for each model
        train_bounds: dictionary of tuples
            stores the min/max residuals values, beyond which points are ultimately classified as outliers, for each model.  
            Has form (Res_low_bound, Res_high_bound)
        train_data: dictionary of lists of pandas dataframes
            once fit method employed, each model in self.models gets a list of pandas dataframes for each iteration of the 
            solver in the fit method. The dataframe features are: [y_pred, Residuals, Outlying_Classification] for that 
            iteration.
        train_data_ave: pandas dataframe
            equals the average of all the final iteration dataframes in train_data.  
        X_train: pandas dataframe
            once fit is performed, this is the cleaned X_train (outliers removed)
        y_train: pandas series
            once fit is performed, this is the cleaned y_train (outliers removed)
        test_data: dictionary of pandas dataframes
            when transform method employed, each model is applied to the (X,y) data and a dataframe is generated.  Features of 
            df are [y_pred, Residuals, Outlying_Classification].
        test_data_ave: pandas dataframe
            equals the average of all the dataframes in test_data.  
        X_test: pandas dataframe
            once transform is performed, this is the cleaned X_test
        y_test: pandas series
            once transform is performed, this is the cleaned y_test
        """
        self.models = models     
        self.length = len(self.models)
        self.metric = metric
        self.factor = factor
        self.n_max = n_max       
        self.percent_necessary = percent
        self.window = window  
        self.threshold = threshold
        
        self.train_n = {list(models.keys())[j]: 0 for j in range(self.length)}
        self.train_percent = {list(models.keys())[j]: 0 for j in range(self.length)}
        self.train_bounds = {list(models.keys())[j]: () for j in range(self.length)}
        self.train_data = {list(models.keys())[j]: [] for j in range(self.length)}
        self.train_data_ave = pandas.DataFrame()
        self.X_train = None
        self.y_train = None
        self.test_data = {list(models.keys())[j]: [] for j in range(self.length)}
        self.test_data_ave = pandas.DataFrame()
        self.X_test = None
        self.y_test = None  
        self.cv_train_scores = None
        self.cv_test_scores = None
        
    def fit(self, X_train, y_train):
        """ 
        Description
        -----------
        fits X_train to y_train via previously specified regression models, iteratively works out outliers up to n_max times,
        until converges, storing results in self.train_n, self.train_percent, self.train_bounds, self.train_data.  Then averages 
        results for all models into self.train_ave.  In self.train_ave, makes final classification of outlier status according 
        to whether average Boolean value is greater than self.threshold or not.  Then drops outliers from X_train, y_train.  
        
        Parameters
        ----------
        X_train: pandas dataframe
        y_train: pandas series
        """
        def fit_per_model(X_train, y_train, model):
            """
            Description
            -----------
            for given regression model, converges on a regression fit, and outputs number of iterations, percent match of outlier 
            classifications between the last set of iterations before it exited the program, the residual bounds on the last iteration
            (beyond which points are classified as outliers), and a list of dataframes of the results of each iteration.  The df 
            features are ["y_pred", "Residuals", "Outlying_Classficiation"]. n is the iteration.  After every iteration, if percent < 
            percent_necessary, tag is set to n, and counter reset to 0. If percent > percent_necessary, then tag stays at that n for 
            as long as this continues to happen, while counter successively increments.  When/if counter > self.window, then programs 
            exits (by switching different_outliers to False). Also exits if max iterations exceeded of course.  
            """
            n = -1
            tag = 0
            counter = 0
            percent = 0
            bounds = ()
            data = []
            model.fit(X_train, y_train)
            different_outliers = True 
            while (different_outliers == True and n < self.n_max): 
                n += 1
                y_pred = model.predict(X_train) 
                Residuals = (y_train.values - y_pred.ravel()).ravel() 
                data_n = numpy.stack((y_pred, Residuals), axis=1)
                data_n = pandas.DataFrame(data_n, index = X_train.index.to_list(), columns = ["y_pred", "Residuals"]) 
                Q = numpy.quantile(Residuals,[0,0.25,0.50,0.75,1]) 
                IQR = Q[3]-Q[1] 
                mean = Residuals.mean() 
                std = Residuals.std() 
                if self.metric == "IQR":
                    Res_low_bound, Res_high_bound = Q[1] - self.factor*IQR, Q[3] + self.factor*IQR 
                elif self.metric == "std":
                    Res_low_bound, Res_high_bound = mean-self.factor*std, mean+self.factor*std
                else:
                    raise Exception("metric must be either 'IQR' or 'std'")
                bounds = Res_low_bound, Res_high_bound
                row_outlier_set = []
                for i in range(len(Residuals)):
                    if (Residuals[i] < Res_low_bound) or (Residuals[i] > Res_high_bound): 
                        row_outlier_set.append(True)
                    else:
                        row_outlier_set.append(False)
                data_n["Outlying_Prediction"] = row_outlier_set
                data.append(data_n)
                X_cleaned = X_train[~data_n["Outlying_Prediction"]]
                y_cleaned = y_train[~data_n["Outlying_Prediction"]]   
                model.fit(X_cleaned, y_cleaned)
                if n > 0:
                    comparison = (data[n]["Outlying_Prediction"] == data[tag]["Outlying_Prediction"])
                    percent = comparison.sum()/len(comparison)
                    if percent >= self.percent_necessary:
                        counter += 1
                        if counter >= self.window:
                            different_outliers = False
                        else:
                            pass
                    else:
                        counter = 0
                        tag = n
                else:
                    pass
            return  n, percent, bounds, data 
        
        for key in self.models:
            self.train_n[key],self.train_percent[key],self.train_bounds[key],self.train_data[key]=fit_per_model(X_train,y_train,self.models[key])
        self.train_data_ave = 0 
        for key in self.models:
            self.train_data_ave += self.train_data[key][-1]
        self.train_data_ave/=self.length
        self.train_data_ave["Outlying_Prediction"]=self.train_data_ave["Outlying_Prediction"].apply(lambda x:True if x>=self.threshold else False)       
        self.X_train = X_train[~self.train_data_ave["Outlying_Prediction"]]
        self.y_train = y_train[~self.train_data_ave["Outlying_Prediction"]]       
        
    def transform(self, X_test, y_test):
        """ 
        Description
        -----------
        makes predictions on X_test and compares to y_test via previously specified regression models to get the residuals.  
        Then uses previously calculated self.train_bounds to classify, per model, the outlier status of the row.  Stores 
        these results in self.test_data.  Then averages results for all models into self.test_data_ave.  In self.test_data_ave, 
        makes final classification of outlier status according to whether average Boolean value is greater than self.threshold or not.  
        Then drops outliers from X_test, y_test.  
        
        Parameters
        ----------
        X_test: pandas dataframe
        y_test: pandas series
        """
        def transform_per_model(X_test, y_test, model, bounds):
            """
            calculates test residuals, per model, by taking the models previously fit in the self.fit() method, 
            and making predictions on X_test and comparing to y_test. Then uses self.train_bounds from the self.fit() 
            method to classify the points as outliers or not.
            """
            data = []
            y_pred = model.predict(X_test)
            Residuals = (y_test.values - y_pred.ravel()).ravel()  
            data_0 = numpy.stack((y_pred, Residuals), axis=1)
            data_0 = pandas.DataFrame(data_0, index = X_test.index.to_list(), columns = ["y_pred", "Residuals"])
            row_outlier_set = []
            Res_low_bound, Res_high_bound = bounds      
            for i in range(len(Residuals)):
                if (Residuals[i] < Res_low_bound) or (Residuals[i] > Res_high_bound): 
                    row_outlier_set.append(True)
                else:
                    row_outlier_set.append(False)
            data_0["Outlying_Prediction"] = row_outlier_set
            data.append(data_0) 
            return data
            
        for key in self.models:
            self.test_data[key] = transform_per_model(X_test, y_test, self.models[key], self.train_bounds[key])
        self.test_data_ave = 0
        for key in self.models:
            self.test_data_ave += self.test_data[key][0]
        self.test_data_ave/=self.length
        self.test_data_ave["Outlying_Prediction"]=self.test_data_ave["Outlying_Prediction"].apply(lambda x:True if x>=self.threshold else False)
        self.X_test = X_test[~self.test_data_ave["Outlying_Prediction"]]
        self.y_test = y_test[~self.test_data_ave["Outlying_Prediction"]] 
        
    def cross_val_hist(self, X, y, n_folds=5, r=42, n_bins=25):
        """
        Description
        ----------
        splits data, X, into n parts.  trains on n-1 of the parts, tests on the nth part, and calculates the 
        histograms for the both using the last trained models in self.train_data / self.test_data, and also self.
        train_data_ave / self.test_data_ave.  Since this method employs self.train( ) and self.test ( ) it 
        will change what's stored in self.X_train, self.y_train, self.X_test, and self.y_test.  
        
        Parameters
        ----------
        X: pandas dataframe
            this is probably the original entire dataset independent variables
        y: pandas series
            this is also the original entire dataset dependent variables, probably
        n_folds: int
            the number of cross validation folds
        r: int
            a random state seed
        n_bins: int, list
            determines how the histogram is partitioned
        """
        X = X.reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n_folds, shuffle=True, random_state = r)
        folds = kf.split(X)
        n = 0
        for train_indices, test_indices in folds:
            n+=1
            self.fit(X.loc[train_indices], y.loc[train_indices])
            self.transform(X.loc[test_indices], y.loc[test_indices])
            train_data_dict = {key: self.train_data[key][-1] for key in self.train_data}
            train_data_dict["ave"] = self.train_data_ave
            test_data_dict = {key: self.test_data[key][-1] for key in self.test_data}
            test_data_dict["ave"] = self.test_data_ave
            for names in zip(train_data_dict, test_data_dict):
                train_name, test_name = names[0], names[1]
                pyplot.figure()
                train_data = train_data_dict[train_name]
                test_data = test_data_dict[test_name]
                train_residuals_normal = train_data["Residuals"][train_data["Outlying_Prediction"] == False]
                train_residuals_outliers = train_data["Residuals"][train_data["Outlying_Prediction"] == True]
                test_residuals_normal = test_data["Residuals"][test_data["Outlying_Prediction"] == False]
                test_residuals_outliers = test_data["Residuals"][test_data["Outlying_Prediction"] == True]
                nbins = n_bins
                if type(n_bins) == int:
                    res_min, res_max = train_data["Residuals"].min(), train_data["Residuals"].max()
                    nbins = numpy.linspace(res_min, res_max, n_bins)
                pyplot.subplot(121)
                pyplot.hist(train_residuals_normal, color = "blue", bins = nbins)
                pyplot.hist(train_residuals_outliers, color = "red", bins = nbins)
                pyplot.ylabel("counts")
                pyplot.xlabel("residuals")
                pyplot.title("Fold " + str(n) + " Res Hist train " + str(train_name))
                pyplot.grid()
                pyplot.subplot(122)
                pyplot.hist(test_residuals_normal, color = "blue", bins = nbins)
                pyplot.hist(test_residuals_outliers, color = "red", bins = nbins)
                pyplot.xlabel("residuals")
                pyplot.title("Fold " + str(n) + " Res Hist test " + str(test_name))
                pyplot.grid()
                pyplot.show()

    def cross_val_scores(self, X, y, n_folds=5, r=42):
        """
        Description
        ----------
        splits data, X, into n parts.  Trains on n-1 of the parts, applying the self.fit() method to it, and then applies
        self.transform() to the n_th part.  And calculates the fit_score (r2 value) for the n-1 parts, for every model in 
        self.models, using each of the last fit models in self.train_data, as well as the self.train_data_ave guy. And does
        likewise for the n_th part using the self.test_data, and self.test_data_ave.  Warning!  Since this method employs 
        self.train( ) and self.test( ) it will change what's stored in self.X_train, self.y_train, self.X_test, and self.y_test.
        It will store all these results in self.cv_train_scores, and self.cv_test_scores.
        
        The utility of this feature is questionable.  If use a model that can overfit, like a decision tree with min_samples_leaf
        = 1, then it will fit really close in the training part.  But then, since it is designed to throw away outliers, it will
        end up throwing away a lot of the points in the testing data set (the n_th part) that lie far from the probably really 
        bad fit it makes on that set.  So such models end up with overinflated scores.  
        
        Parameters
        ----------
        X: pandas dataframe
            this is probably the original entire dataset independent variables
        y: pandas series
            this is also the original entire dataset dependent variables, probably
        n_folds: int
            the number of cross validation folds
        r: int
            a random state seed
        """

        X = X.reset_index(drop=True)
        y = y.copy().reset_index(drop=True)
        kf = KFold(n_splits=n_folds, shuffle=True, random_state = r)
        folds = kf.split(X)
        n = 0
        train_scores = {}
        test_scores = {}
        for train_indices, test_indices in folds:
            n+=1
            self.fit(X.loc[train_indices], y.loc[train_indices])
            self.transform(X.loc[test_indices], y.loc[test_indices])
            train_data_dict = {key: self.train_data[key][-1] for key in self.train_data}
            train_data_dict["ave"] = self.train_data_ave
            test_data_dict = {key: self.test_data[key][-1] for key in self.test_data}
            test_data_dict["ave"] = self.test_data_ave
            train_scores["fold_" + str(n)] = []
            test_scores["fold_" + str(n)] = []
            for names in zip(train_data_dict, test_data_dict):
                train_name, test_name = names[0], names[1]
                train_data = train_data_dict[train_name]
                test_data = test_data_dict[test_name]
                train_data_non_outlier = train_data[train_data["Outlying_Prediction"]==False]
                test_data_non_outlier = test_data[test_data["Outlying_Prediction"]==False]
                y_train_pred = train_data_non_outlier["y_pred"]
                y_train = train_data_non_outlier["y_pred"] + train_data_non_outlier["Residuals"]
                y_test_pred = test_data_non_outlier["y_pred"]
                y_test = test_data_non_outlier["y_pred"] + test_data_non_outlier["Residuals"]               
                train_score = r2_score(y_train_pred, y_train)
                test_score = r2_score(y_test_pred, y_test)
                train_scores["fold_" + str(n)].append(train_score)
                test_scores["fold_" + str(n)].append(test_score)
        train_names = list(self.train_data.keys()) + ["ave"]
        test_names = list(self.test_data.keys()) + ["ave"]
        self.cv_train_scores = pandas.DataFrame(train_scores, index = train_names)
        self.cv_train_scores["net"] = self.cv_train_scores.mean(axis=1)
        self.cv_test_scores = pandas.DataFrame(test_scores, index = test_names)
        self.cv_test_scores["net"] = self.cv_test_scores.mean(axis=1)
        
    def res_hist(self, data_dict, n_bins):
        """ 
        Description
        -----------
        creates a histogram(s) of the residuals from any dictionary of dataframes with columns ["Residuals", "Outlying_Prediction"].
        Predicted outliers are colored red, otherwise, blue.  Hopefully outliers are non-Gaussian part of histogram.
        
        Parameters
        ----------
        data_dict: dictionary of pandas dataframes
            they should have columns ["Residuals", "Outlying_Prediction"].  As such those df's stored in self.train_data[m][iter],
            self.train_data_ave, self.test_data[m][iter], self.test_data_ave should all be amenable.
        n_bins: int, list
            number of bins to go in the histogram, or list of partition points
            
        Returns
        -------
        histograms
        """
        from matplotlib import pyplot
        for name in data_dict:
            pyplot.figure()
            data = data_dict[name]
            residuals_normal = data["Residuals"][data["Outlying_Prediction"] == False]
            residuals_outliers = data["Residuals"][data["Outlying_Prediction"] == True]
            nbins = n_bins
            if type(n_bins) == int:
                res_min, res_max = data["Residuals"].min(), data["Residuals"].max()
                nbins = numpy.linspace(res_min, res_max, n_bins)
            pyplot.hist(residuals_normal, color = "blue", bins = nbins)
            pyplot.hist(residuals_outliers, color = "red", bins = nbins)
            pyplot.ylabel("counts")
            pyplot.xlabel("residuals")
            pyplot.title("Residuals Histogram for " + str(name))
            pyplot.grid()
            pyplot.show()

    def outlier_overlap(self, data_dict):
        """
        Description
        -----------
        creates a heatmap of the residuals from any dictionary of dataframes with columns ["Residuals", "Outlying_Prediction"].
        element [i,j] is overlap between models i and j outlier predictions divided by their union.  Looks like 50% is typical number.
        
        Parameters
        ----------
        data_dict: dictionary of pandas dataframes
            they should have columns ["Residuals", "Outlying_Prediction"].  As such those df's stored in self.train_data[m][iter],
            self.train_data_ave, self.test_data[m][iter], self.test_data_ave should all be amenable.
        """
        L = len(data_dict)
        names = list(data_dict.keys())
        M = numpy.zeros((L, L))
        for i in range(L):
            for j in range(L):
                overlap = ((data_dict[names[i]]["Outlying_Prediction"]==True) & (data_dict[names[j]]["Outlying_Prediction"]==True)).sum()
                union = ((data_dict[names[i]]["Outlying_Prediction"]==True) | (data_dict[names[j]]["Outlying_Prediction"]==True)).sum()
                M[i][j] = overlap/union

        from matplotlib import pyplot
        pyplot.figure()
        df = pandas.DataFrame(M, columns = names, index = names)
        seaborn.heatmap(data=df, cmap="RdBu", vmin=0, vmax=1, center=0.5, square=True, annot = True, fmt=".2f")
        pyplot.title("overlap between models' outlier predictions", y=1.05)
        pyplot.show()



 