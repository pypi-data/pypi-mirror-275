# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:55:14 2024

@author: atdou
"""

# XtraMLTools 
This package contains Regression and Classification modules to augment the options in sklearn.  Additionally, there is 
a preprocessing module to help with outlier detection.

### Regression
The **Regression** module includes Linear, Quadratic, and Polynomial Regression classes.  The *Quadratic* Regression 
class allows one to select numerical features in the dataset  to model quadratically.  It does this by adding to the 
dataframe additional columns equal to the products of the selected columns, and then applying sklearn's linear
Additionally regression algorithm.  The *Polynomial* Regression class is similar.  One selects the numerical features 
to model with a polynomial, inputs the desired degree, and then Polynomial Regression will add the requisite columns 
to the dataframe and perform a linear regression.  For instance, to model features n<sub>1</sub>, and n<sub>2</sub> 

<div style = "margin-left:15px">

| n<sub>1</sub> | n<sub>2</sub> | 
|:-------------:|:-------------:|
| 1             |  2            |  
| 3             |  4            |    
| 5             |  6            |  
| 7             |  8            | 
| 9             |  10           |
|11             |  12           |

</div>

with 3rd degree polynomial, it will add additional features: n<sub>1</sub><sup>3</sup>, 
n<sub>1</sub><sup>2</sup>n<sub>2</sub>, n<sub>1</sub>n<sub>2</sub><sup>2</sup>, n<sub>2</sub><sup>3</sup>,

<div style = "margin-left:15px">

| n<sub>1</sub> | n<sub>2</sub> | n<sub>1</sub><sup>3</sup> | n<sub>1</sub><sup>2</sup>n<sub>2</sub> | n<sub>1</sub>n<sub>2</sub><sup>2</sup> | n<sub>2</sub><sup>3</sup>|
|:-----------:|:-----------:|:---------:|:----------:|:-----------:|:----------:|
| 1           |  2          |  1        |   2        |   4         |   8        |
| 3           |  4          |  27       |   36       |   48        |   64       |  
| 5           |  6          |  125      |   150      |   180       |   216      |
| 7           |  8          |  343      |   392      |   448       |   512      |
| 9           |  10         |  729      |   810      |   900       |   1000     |
|11           |  12         |  1331     |   1452     |   1584      |   1728     |

</div>

Additionally, there are *Categorial Linear*, *Categorical Quadratic*, and *Categorical Polynomial* Regression Classes.  Say we have 
two numerical features as before, and additionally two categorical features, c<sub>1</sub>, with three possible values, and 
c<sub>2</sub>, with two.  After one-hot-encoding, and dropping the first columns, we might have something like this:

<div style = "margin-left:15px">

| n<sub>1</sub> | n<sub>2</sub> | c<sub>1b</sub> | c<sub>1c</sub>| c<sub>2b</sub>|
|:-------------:|:-------------:|:--------------:|:-------------:|:-------------:|
| 1             |  2            |  1             |  0            |  0            |
| 3             |  4            |  0             |  0            |  1            |
| 5             |  6            |  0             |  1            |  1            |
| 7             |  8            |  1             |  0            |  0            |
| 9             |  10           |  0             |  1            |  1            |
|11             |  12           |  0             |  0            |  0            |

</div>

When we run an ordinary linear regression on this data in sklearn, the regression coefficients/slopes of the 
n<sub>1</sub> and n<sub>2</sub> features will be independent of the values of the categorical features.  
This may not be desirable. For instance, if our target variable were y = distance, n<sub>1</sub> were time, 
and c<sub>2</sub> were gender, then we should generally expect the regression coefficient for n<sub>2</sub> 
to be larger when c<sub>2</sub> = male, than when c<sub>2</sub> = female.  If we wish to allow the numerical 
features' coefficients to vary with the categorical features' values, we can model the data with one of the 
Categorical Regression classes.  They do this by multiplying the selected numerical features by the selected 
categorical features, adding these columns to the dataframe, and performing a linear regression.  

### Classification
The classification module is similar to the regression module.  It allows one to add polynomial columns to the purely numeric 
features, and to also split these by whichever desired categorical features.  Then it fits a logistic regression curve through the 
augmented features.  This ought to be able to perfectly classify features that can be separated by any polynomial surface in the 
feature space of the numerical variables, with coefficients that possibly depend on the categorical features.  

### Preprocessing
There is as well a preprocessing module which contains a regression outlier removal class.  This can be used to help 
identify outliers.  One defines a dictionary of regressor models to feed into the object, fits the object to the data, 
and it will run a regression outlier removal program, progressively refinining the outlier estimations for each model 
until these converge.  One can then compare the outlier predictions for each of the models employed.  One can also look
at the predictions of an aggregate model that combines the predictions of all models and uses a user threshold 
majority vote for making a final prediction on whether a point is an outlier or not.  

# Installation
so, 

```
pip install XtraMLTools
```

# Usage examples
Later, gator.  



