import pandas as pd;
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data_frame=pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv");


x=data_frame.drop(["Humidity","Description"],axis=1);
y=data_frame["Humidity"];


#To instantiate a linear regression model, refer to the code here:

model = LinearRegression()
#Fit the model to the  Avg.  Area Income  column in the training data using this code:
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=0)
model.fit(X_train[["Wind_Speed_kmh"]],y_train);
score=model.score(X_test[['Wind_Speed_kmh']], y_test)
print(score);



