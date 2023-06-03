import matplotlib.pyplot as plt
import numpy as np



#----------------------------------------- EXAMPLE ---------------------------------------------
# x=[1,2,3,4,5,6];
# y=[8,5,6,9,2,2];
# plt.xlabel("time");
# plt.ylabel("profit");
# plt.plot(x,y);
# plt.show();

#--------------------------------- RANGE FUNCTION --------------------------------------------
#range(startingValue,endingValue,interval)
number_list=list(range(1,10));
print(number_list);

#--------------------------------- TASK------------------------------------------------------
#Create a List from year 1950 to 2101
year_list=list(range(1950,2101));
print(year_list,len(year_list));

#Add interval of 10
year_list_interval= list(range(1950,2101,10));
print(year_list_interval);

#------------------------------------- TASK -------------------------------------------------
#Create list from -1 to -100
neg_list=list(range(-1,-100,-1));
print(neg_list);


#------------------------------------- TASK ------------------------------------------------
#Use the list for 1950 to 2021 and print last item from both the year and the pop list to see what is the predection in the year 2100

pop=[2.53,2.57,2.62,2.67,2.71,2.76,2.81,2.86,2.92,2.97,3.03,3.08,3.14,3.2,3.26,3.33,3.4,3.47,3.54,3.62,3.69,3.77,3.84,3.92,4.,4.07,4.15,4.22,4.3,4.37,4.45,4.53,4.61,4.69,4.78,4.86,4.95,5.05,5.14,5.23,5.32,5.41,5.49,5.58,5.66,5.74,5.82,5.9,5.98,6.05,6.13,6.2,6.28,6.36,6.44,6.51,6.59,6.67,6.75,6.83,6.92,7.,7.08,7.16,7.24,7.32,7.4,7.48,7.56,7.64,7.72,7.79,7.87,7.94,8.01,8.08,8.15,8.22,8.29,8.36,8.42,8.49,8.56,8.62,8.68,8.74,8.8,8.86,8.92,8.98,9.04,9.09,9.15,9.2,9.26,9.31,9.36,9.41,9.46,9.5,9.55,9.6,9.64,9.68,9.73,9.77,9.81,9.85,9.88,9.92,9.96,9.99,10.03,10.06,10.09,10.13,10.16,10.19,10.22,10.25,10.28,10.31,10.33,10.36,10.38,10.41,10.43,10.46,10.48,10.5,10.52,10.55,10.57,10.59,10.61,10.63,10.65,10.66,10.68,10.7,10.72,10.73,10.75,10.77,10.78,10.79,10.81,10.82,10.83,10.84,10.85];
print('Population of world in ',year_list[len(year_list)-1],' will be ',pop[len(pop)-1], ' Billion');


#---------------------------------- TASK ----------------------------------------------------   
#Make a plot with year on x axis and population on y axis

# plt.plot(year_list,pop);
plt.xlabel('Year');
plt.ylabel('Population');
plt.title('Population/Year');
# plt.show();

#use scatter plot
# plt.scatter(year_list,pop);
# plt.show();

#---------------------------------- TASK ----------------------------------------------------------------

month=['Jen','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nev','Dec'];
saving=[209.00,250.00,209.00,297.00,356.00,388.00,305.00,397.00,362.00,237.00,282.00,238.00];
plt.title("Monthly/Savings");
plt.xlabel("Month");
plt.ylabel("Savings($)");
# plt.plot(month,saving);
# plt.show();


#----------------------------------- TASK -----------------------------------------------------------
import pandas as pd;
import numpy as np;

data=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/gapminder.csv');
data_np=np.array(data);
gdp_exp=data_np[:,6];
life_exp=data_np[:,5];
#Calcualte values on the last index of both columns
print('The life exptency for ',gdp_exp[-1],' GDP Per Capita is',life_exp[-1]);

#Plot a graph between gdp_cap and life_exp
plt.title("GDP vs Life Exptency");
plt.xlabel("GDP");
plt.ylabel("Life Exptency");
# plt.scatter(gdp_exp,life_exp);
# plt.show();


