# Data Science Curriculum 



# 2025 Weekly Schedule

## First Three Weeks
https://github.com/werowe/HypatiaAcademy?tab=readme-ov-file#statistics

* The Normal Curve
* Normalize Data with z-Score
* Poisson Distribution
* Normalize data, std, mean, z-score in Google Sheets
* Normal and Uniform Distribution in Google Sheets
* Binomial Distribution in Google Sheets
* Exponential Distribution



## Jan 7
* generate some random data using the =NORMINV(RAND(), average, std)
* calculate the z-score---use int() to make it an integer
* calculate the cumulative property of you observation using =NORM.DIST(observed,average,std,true)
* use chart to make a chart
6:59
 


## Jan 10
homework.  what does false versus true mean in this =NORM.DIST(C2,mean,std,false) function.  put into your previous homework and test it/prove it
homework:  so figure out how to adjust the chart in google sheets to show the edges, labels
in integers like -2, -1, 0, 1, 2


## January 14

homework https://docs.google.com/spreadsheets/d/1A-iJK4s-9hwPGzLW3jgpi4eKp1Uy4qv7JybnXWo1PjY/edit?usp=sharing
 
* optional homework figure out the  probability of flipping a coin 6 times and getting 2 heads
* solve this homework optional:
- why do you multiple each combination by	
- the probability of (each trial) ^ success 	
- and the probability of (1 - each trial)^(number of trials - successes)

which answer is correct this one https://docs.google.com/document/d/1q9lmsMowu2iVxyfCTvOSSttibkm669_lTNhgW3_6B78/edit?usp=sharing or this one https://docs.google.com/spreadsheets/d/1_05Bqp00qoUvtdOi77VEA6PLQsomabY8O7akXXYkeYo/edit?usp=sharing


```

Марія Афанасьєва
 
https://docs.google.com/document/d/1L3uAsnuPmbBLlJ0ni-NV9EANCQf93mkodAjMFtUM4p4/edit?usp=sharing
The formula explanation
```

```
Illia Zhupanov
 
https://docs.google.com/spreadsheets/d/17n2Prl6EDjZ4Rp54crbgaBNNasviuuYT2gCcUypt-3Q/edit?usp=sharing
diff between the two approaches
```

## Jan 21

homework is to understand this https://docs.google.com/spreadsheets/d/1p9vqIRI7LvKr-4OLL4VqhVjlXdbAfolBljSzPb-jWIQ/edit?usp=sharing


``` 
The formula explanation and why does the sum = 1
https://docs.google.com/spreadsheets/d/1V3DUL8GfVOLA-j-kxwPS3haeZ9V5Q_EzVvS09ZqXOzU/edit?usp=sharing
```

## Jan 21 Basic Numpy Introduction (slicing comes later).  Needed for Stats next few classes

homework https://colab.research.google.com/drive/1CNhYyLEMkIo16VmxUH9vUa9b2v5yJqeX?usp=sharing
 


## Jan 28  Goodness of Fit, Normal, and Weibull

https://github.com/werowe/HypatiaAcademy/blob/master/stats/goodness_of_fit.ipynb


## Jan 31  Goodness of Fit, Normal, and Weibull
https://github.com/werowe/HypatiaAcademy/blob/master/stats/weibull_ilya_numpy_plotting_homework_31_01_25.ipynb

## Feb 4
https://github.com/werowe/HypatiaAcademy/blob/master/class/2024_02_04_numpy_slicing_diagonal.ipynb


## Feb 7
(none, review Numpy quick start guide) 

## Feb 11
https://github.com/werowe/HypatiaAcademy/blob/master/stats/2024_02_11_charting.ipynb
https://github.com/werowe/HypatiaAcademy/blob/master/stats/2024_02_11_histogram.ipynb
https://github.com/werowe/HypatiaAcademy/blob/master/charts/2025_02_14_pie_chart.ipynb

## Feb 14
https://github.com/werowe/HypatiaAcademy/blob/master/stats/seaborn_bar.ipynb

# Pandas


## Feb 21
https://github.com/werowe/HypatiaAcademy/blob/master/pandas/ilya-pandas_homework_20_02_25.ipynb


## Feb 25 Fix Issues in this Pandas data from Ilias
https://github.com/werowe/HypatiaAcademy/blob/master/pandas/ilya-pandas_homework_20_02_25.ipynb


## Feb 27  Take Data from Previous Classes and Now put into Spark


## Example 1
https://github.com/werowe/HypatiaAcademy/blob/master/spark/youtube_german_channels.ipynb


## Example 2
https://github.com/werowe/HypatiaAcademy/blob/master/spark/2025_02_28_diana_pandas_to_spark.ipynb


## Imdb Spark
https://github.com/werowe/HypatiaAcademy/blob/master/spark/Imdb_spark_data.ipynb

## March 4 Steam Games
https://github.com/werowe/HypatiaAcademy/blob/master/spark/homework_spark_04_03_25.ipynb



## March 8 Data Cleaning part I

https://github.com/werowe/HypatiaAcademy/blob/master/pandas/pandas_missing_data.ipynb

**Homework**:  fix x=df.loc[abs(df['salary'] - mean) > 2 * std].apply(makeMean) in that notebook.  It updates all columns and the index too instead of one column.


##  March 11 Data Cleaning part II:  Drop Outliers

https://github.com/werowe/HypatiaAcademy/blob/master/pandas/pandas_drop_outliers.ipynb

## March 11: Start Some Days of Kaggle Data Cleaning Competition 

https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values

### Homework Bad data Examples

* **UCI Machine Learning Repository**
  - Wine Quality Dataset (contains outliers and formatting issues).    https://archive.ics.uci.edu/dataset/186/wine+quality
  - Solar Flare Dataset (missing values and categorical inconsistencies)  https://archive.ics.uci.edu/dataset/89/solar+flare

* **Kaggle**
  - https://www.kaggle.com/code/bozungu/ebay-used-car-sales-data  eBay Car Sales Dataset (contains missing values and inconsistencies).
  - https://www.kaggle.com/datasets/yasserh/housing-prices-dataset (Includes missing values for features like lot size and house condition, as well as price outliers)
  - https://www.kaggle.com/datasets/unsdsn/world-happiness


## March 14 Work on Kaggle Data Cleansing 

### Lecture Kaggle notebooks and google doc:
* https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values
* https://docs.google.com/document/d/15cqq284X55G352BGTLmg50_t9ZAXf_YWdoNQBVIVvmE/edit?usp=sharing
* https://www.kaggle.com/code/walkerroweiii/data-cleaning-challenge-scale-and-normalize-data

  
## April 1  Mutiple Linear Regression

Learn to move from simple linear regression to having mutiple features.  so the goal is to learn how reshape X

https://github.com/werowe/HypatiaAcademy/blob/master/ml/2025_04_01_scikit_learn_scipy_linear_regression.ipynb


## April 6 Multiple Linear Regression  

Fish:  https://github.com/werowe/HypatiaAcademy/blob/master/ml/multiple_linear_regression_scikit_learn_fish_market.ipynb

Nazar:  https://github.com/werowe/HypatiaAcademy/blob/master/ml/2025-04-05-nazar-wine-quality.ipynb


**Maria** 
https://github.com/werowe/HypatiaAcademy/blob/master/ml/Homework_2025_04_04%2C_Maria%2C_linear_regression.ipynb

**Nazar**
https://colab.research.google.com/drive/1nDSW7hnqFWpX9ARqy3LNE4hYj9rclMz4?usp=sharing


## April 11 Calulate LSE manually

**explanation**:   https://github.com/werowe/HypatiaAcademy/blob/master/class/calculate_linear_regression_manually.ipynb

## April 22 Calulate LSE manually


**solution**: https://github.com/werowe/HypatiaAcademy/blob/master/class/calculate_linear_regression_manually.ipynb


## April 25 logistic regression

https://github.com/werowe/HypatiaAcademy/blob/master/ml/logistic_regression_intro.ipynb


gambling odds and statistical odds


# May 2 Begin Neural Networks MNIST

https://github.com/werowe/HypatiaAcademy/blob/master/ml/2025_05_02_handwriting_recognition.ipynb

**Homework: Dissecting a Neural Network for MNIST Classification**
Objective: Deconstruct a trained MNIST model to understand data flow, layer operations, and prediction mechanics.
Part 1: Data Anatomy (30%)

Dataset Inspection
* Load MNIST using any library (24)

Report:
* Training/test sample counts
* Image dimensions
* Pixel value range

Plot first 10 training images with labels
1. Input Normalization
2. Convert pixel values from255 to1
Explain why normalization matters for training


 Part 2: Network Surgery (50%)
Layer Visualization

Using your trained model:

Print layer types/sizes (e.g. model.summary() in Keras)
Calculate total trainable parameters
Manual Prediction

For one test image:

Flatten to 784-dim vector3

Perform matrix multiplication for first dense layer

```
hidden_input = np.dot(image_flat, W1) + b1
```
