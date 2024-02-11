# Oskers_Datathon

## Problem Statement
The electrical distribution network comprising underground and overhead lines is a critical component of the power system infrastructure. However, it is susceptible to various faults due to equipment failure, environmental conditions, human errors, etc.

Traditional fault detection methods are very time-consuming, so come up with an ML model to determine the type of fault using current and voltage data.

## Solution:
I will use Linear models to solve this as the Problem consists of using voltage and current data primarily. I will thus focus on finding data which includes this. Then I will make our my edits to make the model more interactive and create a front-end framework from where it can be accessed. Our model will be able to take input and provide output in the form of the type of problem, it can also be connected to a live server as well as take input data. For now, we are focusing on taking input from the user.

## Datasets used
I have used a dataset from the model of a power system in MATLAB which simulates fault analysis. The power system consists of 4 generators of 11 × 10^3 V, each pair located at each end of the transmission line. Transformers are present in between to simulate and study the various faults at the midpoint of the transmission line.

The simulation of the circuit occurs under normal conditions as well as under various fault conditions. The measured Line Voltages and Line Currents at the output side of the power system are collected and saved. The dataset has nearly 12000 data points

[Electrical Fault Detection and Classification Dataset](https://www.kaggle.com/datasets/esathyaprakash/electrical-fault-detection-and-classification)
[Source](https://springerplus.springeropen.com/articles/10.1186/s40064-015-1080-x#:~:text=section%20is%20conclusion.-,Artificial%20neural%20network,form%20can%20be%20dealt%20with.)

Our second Dataset is used to predict if weather has any involvement in the electrical fault as such we use weather data and our previous voltage & current data to predict the type of fault using weather data

[Electrical Faults Analysis India Dataset](https://www.kaggle.com/datasets/hashbanger/electrical-faults-analysis-india)

## Data cleaning
In this step I dropped the columns not being used and removed outliers and missing values

## Feature Engineering
Herein I connected our input of voltage to both the datasets during predictions as such the voltage being used to predict the type of fault is the average of the voltage of all phases, in future versions I would prefer individual prediction as it would provide greater accuracy!

## Modelling
From the get-go my focus was to make an effective model as such I had the choice of 2 types of linear models! Regressor or Classifier. Regressor models are used for regression tasks, where the goal is to predict a continuous output or a numerical value. Classifier models are used for classification tasks, where the goal is to predict the class or category of a given input.

Regressor confusion matrix (Image_URL_3) Classifier confusion matrix (Image_URL_4)

### Conclusion
Classifier models are providing the best results as our data is in discrete form!

## Exploratory Data analysis
### Overall analysis
- Voltage graph (![Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/voltage.png))
- Current graph (![Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/current.png))
- Voltage and Current graph, where there is a large fluctuation in the graph, there faults have occurred

### No Fault
- Voltage graph (![No Fault Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/no%20fault%20voltage.png))
- Current graph (![No Fault Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/no%20fault%20current.png))
- In a normal (No_Fault) condition Voltage and Current graph is symmetrical and sinusoidal in nature with current and voltage 120 degrees in phase shift and maximum current is approximately +100 to -100 Amperes and voltage +0.5 pu to -0.5pu

### Faulty System with Line A to Ground Fault
- Voltage graph (![Line A to Ground Fault Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20to%20Ground%20Fault%20voltage.png))
- Current graph (![Line A to Ground Fault Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20to%20Ground%20Fault%20current.png))
- At a time of Line A to ground fault, the current in line A increases to 10 fold approximately 1000 Ampears from normal 100 Ampears and voltage reduced.

### Faulty System with Line A, Line B to Ground Fault
- Voltage graph (![Line A, Line B to Ground Fault Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20%2CLine%20B%20to%20Ground%20Fault%20voltage.png))
- Current graph (![Line A, Line B to Ground Fault Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20%2CLine%20B%20to%20Ground%20Fault%20current.png))

### Faulty System with Line B to Line C
- Voltage graph (![Line B to Line C Fault Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20B%20to%20Line%20C%20voltage.png))
- Current graph (![Line B to Line C Fault Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20B%20to%20Line%20C%20current.png))

### Faulty System with Line A - Line B - Line C 
- Voltage graph (![Line A - Line B - Line C - Ground Fault Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20to%20Ground%20Fault%20voltage.png))
- Current graph (![Line A - Line B - Line C - Ground Fault Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20to%20Ground%20Fault%20current.png))
  
### Faulty System with Line A - Line B - Line C - Ground
- Voltage graph (![Line A - Line B - Line C - Ground Fault Voltage graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20-%20Line%20B%20-%20Line%20C%20-%20Ground%20voltage.png))
- Current graph (![Line A - Line B - Line C - Ground Fault Current graph](https://github.com/Samyaktg/Oskers_Datathon/blob/main/res/Faulty%20System%20with%20Line%20A%20-%20Line%20B%20-%20Line%20C%20-%20Ground%20current.png))



## Model decision
I decided to use XGBoost Classifier since it requires minimal parameter tuning and gives accurate results quickly. However, to predict the type of fault, I had to predict a fault in each line. To achieve this, I had to create an ensemble, i.e., we are taking 6 inputs, and the model is predicting 4 outputs and calculating the type of fault based on it. So I utilized the Multiclass-multioutput classification (also known as multitask classification), which is a classification task that labels each sample with a set of non-binary properties. Both the number of properties and the number of classes per property are greater than 2. A single estimator thus handles several joint classification tasks. This is both a generalization of the multilabel classification task, which only considers binary attributes, as well as a generalization of the multiclass classification task, where only one property is considered.

As such, our model can now effectively make multiple predictions!

## For the frontend, I created a Streamlit server:
[Oskers Datathon Streamlit App](https://oskersdatathon.streamlit.app/)

## Learnings through this project:
During this period, I learned multiple new skills, from developing ML models to front end programming. The most amazing part was conducting Exploratory Data Analysis and finding effective features. Then struggling over which ML model was the best. A particular problem I faced was getting multiple predictions from the model as I struggled to find effective solutions before finding out about MultiOutputClassifier! Another daunting aspect was learning frontend from scratch as I learned Streamlit and its functions to host our very own Webapp. I particularly struggled with output errors since Streamlit was not accepting multiple outputs, as such I had to make If...else statements and arrays to ensure smooth operation.
