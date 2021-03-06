## Day 1: April 25, 2018

**Theme**: Scikit Tutorial

**Today's Progress**:
* Set up ML repo
* Started with Scikit-Learn Tutorial
* Analysed general Scikit Datasets
* Practised Linear Regression and Classification Learning with Iris and Diabetic Datasets

**Thoughts**:
* What are different mechanisms to arrive at the correct alpha (or hyper parameters)?
* Need to build or find frameworks what learn using different algorithms and choose one with the best prediction

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/42d65a2a7a28b7a910af953fde10b3f9bb96fb9d)


## Day 2: April 26, 2018

**Theme**: Scikit Tutorial

**Today's Progress**:
* Completed exercise on classifying digits with KNN and Linear Models
* Completed exercise on classifying Iris dataset using SVM
* Practised scoring and cross-validation mechanisms
* Completed exercise on plotting cross validation scores of an SVC estimator for different C params

**Thoughts**:
* Mechanisms to find and verify the correct hyper parameters seem to be built-in, and all seem to be based on trial and error!
* Need to dive deeper in matplotlib - seems to have amazing graphing abilities

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/d0de7fd585b157432f5ee9339155921fe007ce6e)


## Day 3: April 27, 2018

**Theme**: Scikit Tutorial

**Today's Progress**:
* Practised GridSearch and Cross-validated estimators
* Completed exercise of finding optimal regularization parameter alpha
* Practised K-Means Clustering
* Understood Hierarchical Agglomerative clustering

**Thoughts**:
* `scipy.misc.imresize` seems to have been deprecated, and I couldn't find an alternative!
* Scipy tutorial makes a ton of assumptions on our current knowledge - Difficult to consume without background information=

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/fb6450c43c35e9371edf4b53a477f1aa04d3a90d)


## Day 4: April 28, 2018

**Theme**: Scikit Tutorial

**Today's Progress**:
* Practised Decompositions (PCA and ICA)
* Exercise: Pipelining (Decomposition followed by Prediction)
* Exercise: Face Recognition with eigenfaces

**Thoughts**:
* Somebody should outline who data can be transformed, the need for it and the various options available; Right now, it's just a bunch of commands in numpy!
* Cool methods in scikit like GridSearchCV, train_test_split and classification_report!

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/64b34ee40aba9ddddc50b022e5538824602a49d4)


## Day 5: April 29, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Data download/setup
* Data Cleanup
    * Substitute for missing values in Age, Cabin and Embarked

**Thoughts**:
* There are tons of tutorials on how to analyse Titanic dataset from Kaggle, but it's worth having a go at it by myself and referring to other implementations for ideas

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/077946d169cfe76055d18735a035909d2183b260)


## Day 6: April 30, 2018

**Theme**: Kaggle - 5 Day Data Cleaning Challenge

**Today's Progress**:
* Handling Missing Values and Imputation
* Scaling and Normalizing Data Values

**Thoughts**:
* Decided to dive deeper into data cleaning and transformation, to help with Titanic Analysis
* Need to understand more about scaling and normalizing data for practical applications

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/2b8ce4c1f9810ad2af6b42a31f1ad573ac1f2a4f)


## Day 7: May 1, 2018

**Theme**: Kaggle - 5 Day Data Cleaning Challenge

**Today's Progress**:
* Parse dates from strings in dataset
* Fix Character encoding issues in files
* Handle inconsistencies in data

**Thoughts**:
* Amazing to see such data transformation utilities built right into pandas and numpy; save time as long as you know they exist!

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/228e1e69390ceae4448aadcba052c7d09a98fe71)


## Day 8: May 2, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Learn about different Data Analysis techniques
* Implement a linear regression classifier to predict missing age values

**Thoughts**:
* It's pretty frustrating to go blind into the task and start from scratch with reading. But this is probably only the way to complete understanding. Looking up a tutorial and finishing this task is going to be a snap, but what will I ultimately derive?


## Day 9: May 3, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Come up with a more elegant technique to fill missing Age values (Yey, Interpolation!)
* Clean dataset and fix values where missing in all columns
* Create Box Plots on Fare and Age to detect outliers

**Thoughts**:
* `value_counts()` and `interpolate` blew my mind! They indeed have thought about everything in Pandas.

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/df1a70032b300d2160d62aba6c72e0b74e16afbb)


## Day 10: May 4, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Outlier Detection among Fare and Age columns (decided not to eliminate any outliers)
* Data preparation - convert string columns to numeric values
* Feature Selection - using Univariate Selection with sklearn's SelectKBest and `chi2` score function

**Thoughts**:
* Getting the hang of data analysis and preparation now; over time, a list of best practices should emerge
* The best output may be found probably with different data configurations (outliers, normalization etc.) along with different models

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/bd35a8d2b973c16939e1c4c51e32c8e8bf0cbd37)


## Day 11: May 5, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Feature Selection using Recursive, PCA and Feature Importance methods
* Logistic Regression with different feature sets
* Parameter optimisation with Cross Validation and GridSearchCV

**Thoughts**:
* Seems like getting to 80-81% of accuracy is fairly easy with the dataset, and just simple LogisticRegression was able to achieve this score.
* It's finally getting a little exciting to experiment with acutal models and see how different parameters affect the fit; at this stage, the more the number of mistakes, the better learning it is.

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/c587a8de6c601c0ab525c3a02e3a428213caff38)


## Day 12: May 6, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Support Vector Classification with different kernels 
* SVC Parameter optimisation with Cross Validation and GridSearchCV (Best score was 0.792 at C=1000 for Linear kernel)

**Thoughts**:
* Polynomial SVC took too long to complete. May have to run it overnight to see results.
* Though `rbf` is the default kernel, the best results were achieved with a Linear SVC suggesting that defaults may not always be the best options
* For C=1000, the linear kernel SVC took 39 minutes to complete. I should probably run on that on an Azure/AWS GPU and measure performance against my laptop.

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/6590dcc778ff33e2425e8b770cc97beba03afb80)


## Day 13: May 8, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Neural networks - MLPClassifier - with Cross validation
* Prepping to submit for Kaggle Competition

**Thoughts**:
* Neural Networks delivered the best scores, better than Logistic Regression and SVM, at around 85% accuracy.
* Not sure why, but I see varying results every time I try to predict survival on the test data set. Needs investigation.

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/9d71267876b99e88fa29da3a447094c9d2e481b9)


## Day 14: May 11, 2018

**Theme**: Kaggle - Titanic Survival Prediction

**Today's Progress**:
* Generated predictions on Test Data
* Submitted my first entry into a Kaggle competition (Score: 0.74641)!
* Started with Multiclass Classification problem of Poker Hand

**Thoughts**:
* So just like that, I have started putting out my models and algorithms out there into the world!
* While my initial submissions will be weak, I should periodically revisit and resubmit refactored models based on my learning

**Link to work**: [Commit](https://github.com/subhashb/100-days-of-ml/commit/ce5c873f693877106be6c4976757a0c24e894339)

