import pandas as pd
import xgboost as xgb
import joblib

df = pd.read_csv('../data/creditcard_with_location.csv')
X = df.drop(columns=['Class'])
y = df['Class']

model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X, y)

joblib.dump(model, 'model.pkl')
