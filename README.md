# Fake News Detection

## Dataset
In this project, a total of 5 datasets were used: Data_set_1, Data_set_2, politifact_3, Data_set_4, data.csv
For model Build need only text and Label,The final dataset will contain only 2 column ['Article','Label']

In the Label column,
1 replaset true
0 replasent fake

Shape of the combined dataset: (76480, 2)

## Data preprocessing
1. Remove all unwanted columns.
2. Remove All Missing Values Records.
3. Removing all the extra information like brackets, any kind of puctuations - commas, apostrophes, quotes, question marks from Text.
4. Remove all the numeric text, urls from Text.

# ML model
Used Logistic Regression, Stochastic gradient descent,Random forest, GBC, xgboost, DecisionTree, Multinomial Naive Baye and Bernoulli Naive Baye classifiers.
The highest accuracy score is **87.18%** by LogisticGegression classifier, which was then saved on disk with name model.plk
model.plk is used to deploy the model usinf Flask.

