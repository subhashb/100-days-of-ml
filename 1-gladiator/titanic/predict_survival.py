import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, chi2, RFE
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import KFold

train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

def clean_df(df):
    # Convert Cabins to Decks
    def convert_to_deck(cabin):
        if not pd.isna(cabin):
            cabin = cabin[0]
        return cabin

    df['Deck'] = df['Cabin'].apply(convert_to_deck)

    # Remove the odd value 'T' in Cabin/Deck
    df = df[df['Deck'] != 'T']

    # Random assignment of Decks for passengers with no Cabin info
    for i, row in df[df['Cabin'].isnull()].iterrows(): 
        if row['Pclass'] == 1:
            df.at[i, 'Deck'] = random.choice(['A', 'B'])
        elif row['Pclass'] == 2:
            df.at[i, 'Deck'] = random.choice(['D', 'E'])
        else:
            df.at[i, 'Deck'] = random.choice(['E', 'F', 'G'])

    # Drop cabin from the dataset
    df = df.drop('Cabin', axis=1)

    # Update null values in Embarked to S

    df['Embarked'].fillna('S', inplace=True)

    # Also replace Embarked with numeric values
    df.loc[df['Embarked'] == 'S', 'Embarked'] = 0
    df.loc[df['Embarked'] == 'C', 'Embarked'] = 1
    df.loc[df['Embarked'] == 'Q', 'Embarked'] = 2

    # Use Pandas Dataframe Interpolate to fill missing values!
    df = df.interpolate()

    # Change 'female' and 'male' values to 0 and 1 respectively.
    df['Sex'].replace({'female':0,'male':1},inplace=True)
    
    # Change A-G decks with numeric values
    df['Deck'].replace(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], [0, 1, 2, 3, 4, 5, 6, 7], inplace=True)
    
    # Drop **PassengerId**, **Ticket** and **Name** columns
    df = df.drop(['Name', 'PassengerId', 'Ticket'], axis=1)

    print(df.head())
    return df

df = clean_df(train_df)
# Separate data and target values
y = df['Survived']
df = df.drop('Survived', axis=1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=21)

# Scale Values
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Fit Model
mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30))
mlp.fit(X_train, y_train)

pred = mlp.predict(X_test)

print(classification_report(y_test, pred))

df = clean_df(test_df)
pred = mlp.predict(df)
for index, row in test_df.iterrows():
    print(row['PassengerId'], pred[index])