#Will a person buy an insurance or not
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix

df=pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/insurance_data.csv");
print(df);
X = df.drop('bought_insurance', axis=1) #features
y = df['bought_insurance'] #target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
score=model.score(X_test,y_test);
print(score);
cm=confusion_matrix(y_test,y_predicted);
print(cm);


