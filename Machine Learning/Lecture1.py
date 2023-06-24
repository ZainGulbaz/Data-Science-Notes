import pandas as pd;
import numpy as np;

data_frame=pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/USA_Housing.csv",header=0);

#describe gives statistics about numerical values
# print(data_frame.describe());

# #info describes the columns
# print(data_frame.info());


x= data_frame.drop(["Price","Address"],axis=1);
print(x);

data_frame2=pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv");
y=data_frame2.drop(["Description","Temperature"],axis=1);
print(y);

#print(data_frame2["Temperature"][0:10])