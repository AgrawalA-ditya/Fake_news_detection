# Fake News Detection

## Dataset
In this project, a total of 5 datasets were used: Data_set_1, Data_set_2, politifact_3, Data_set_4, data.csv
For model Build need only text and Label,The final dataset will contain only 2 column ['Article','Label']

In the Label column,
1 represent true
0 represent fake

Shape of the combined dataset: (76480, 2)

## Data preprocessing
1. Remove all unwanted columns.
2. Remove All missing Values Records.
3. Removing all the extra information like brackets, any kind of punctuations - commas, apostrophes, quotes, question marks from Text.
4. Remove all the numeric text, urls from Text.

## ML model
Used Logistic Regression, Stochastic gradient descent,Random forest, GBC, xgboost, DecisionTree, Multinomial Naive Baye and Bernoulli Naive Baye classifiers.
The highest accuracy score is **87.18%** by LogisticGegression classifier, which was then saved on disk with name model.plk
model.plk is used to deploy the model using Flask.

## ML model Deployment
For Deployment, created a sample web interface which will get the text from the user and then send it to the flask server. In the flask server, we will use the saved model model.plk to predict the news is real or fake and then return the result to the user through web interface.
Prediction1:
<img width="1249" alt="prediction1" src="https://github.com/user-attachments/assets/6d45db30-7ce6-415b-86f3-69fbac6d90ce" />
Prediction2:
<img width="1263" alt="prediction2" src="https://github.com/user-attachments/assets/bb11ebe3-401f-473f-b864-27e79ad25d0b" />



