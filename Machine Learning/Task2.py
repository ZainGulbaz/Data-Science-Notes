import pandas as pd;
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data_frame=pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv");


x=data_frame.drop(["Temperature","Description"],axis=1);
y=data_frame["Temperature"];

model = LinearRegression()


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=0)

model.fit(X_train[["Humidity"]],y_train);
score=model.score(X_test[['Humidity']], y_test)
print(score);

model.fit(X_train[["Wind_Bearing_degrees"]],y_train);
score=model.score(X_test[['Wind_Bearing_degrees']], y_test)
print(score);

model.fit(X_train[["Pressure_millibars"]],y_train);
score=model.score(X_test[['Pressure_millibars']], y_test)
print(score);

model.fit(X_train[["Visibility_km"]],y_train);
score=model.score(X_test[['Visibility_km']], y_test)
print(score);

model.fit(X_train[["Rain"]],y_train);
score=model.score(X_test[['Rain']], y_test)
print(score);

model.fit(X_train[["Wind_Speed_kmh"]],y_train);
score=model.score(X_test[['Wind_Speed_kmh']], y_test)
print(score);

print(data_frame);

