# Import libraries
import pandas as pd

# read csv file
df = pd.read_csv('train.csv')
df = df['Age', 'Sex', 'Embarked', 'Survived'] # Only four features

# Data Preprocessing
categoricals = []
for col, col_type in df.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df[col].fillna(0, inplace=True)

df_pro = pd.get_dummies(df, columns=categoricals, dummy_na=True)

# Logistic Regression classifier
from sklearn.linear_model import LogisticRegression
dependent_variable = 'Survived'
x = df_pro[df_pro.columns.difference([dependent_variable])]
y = df_pro[dependent_variable]
lr = LogisticRegression()
lr.fit(x, y)

# Save your model
import joblib
joblib.dump(lr, 'model.pkl')
print("Model dumped!")

# Load the model that you just saved
lr = joblib.load('model.pkl')

# Saving the data columns from training
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
