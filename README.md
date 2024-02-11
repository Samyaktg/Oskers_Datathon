# Oskers_Datathon

## Problem Statement
The electrical distribution network, comprising underground and overhead lines, is a critical component of the power system infrastructure. However, it is susceptible to various faults due to equipment failure, environmental conditions, human errors, etc. Traditional fault detection methods are time-consuming. This project aims to develop an ML model to determine the type of fault using current and voltage data.

## Solution
I employed Linear models for fault detection, focusing on voltage and current data. The solution includes a front-end framework for user interaction. The model takes input and provides output in the form of the fault type. It can be connected to a live server and accepts input data.

## Datasets
1. [Electrical Fault Detection and Classification Dataset](https://www.kaggle.com/datasets/esathyaprakash/electrical-fault-detection-and-classification)
2. [Electrical Faults Analysis India Dataset](https://www.kaggle.com/datasets/hashbanger/electrical-faults-analysis-india)

## Data Processing
- Dropped unused columns and handled outliers and missing values.
- Connected voltage input to both datasets for predictions.

## Feature Engineering
Average voltage of all phases used for fault prediction.

## Modelling
Chose XGBoost Classifier for accurate results with minimal tuning. Utilized MultiOutputClassifier for predicting faults in each line, achieving multiple predictions.

## Exploratory Data Analysis
Explored generator images, voltage graphs, current graphs, and identified fault patterns.

## Model Decision
XGBoost Classifier with MultiOutputClassifier for predicting fault types effectively.

## Frontend
Developed a Streamlit server for user interaction. Visit [here](https://oskersdatathon.streamlit.app/).

## Learnings
Learned ML model development, frontend programming, and effective feature identification during Exploratory Data Analysis. Overcame challenges in obtaining multiple predictions and frontend development using Streamlit.

## Conclusion
The developed model effectively predicts electrical faults based on current and voltage data. The Streamlit front-end provides a user-friendly interface for accessing and interacting with the model.

---

*Note: Replace image links with actual image links in the final readme.*
