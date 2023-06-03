import matplotlib.pyplot as plt
import numpy as np;
import pandas as pd;


#------------------------------------------------ SCALES -----------------------------------------------------------------
#There are two types of scales:
#1-Log Scale
#2-Linear Scale


# x=[1,4,5,7,8,9];
# y=[1,10,100,1000,10000,100000]

# plt.plot(x,y);
# plt.xscale("log");
# plt.show();



#------------------------------------------------------- TASK -----------------------------------------------------------------------

# plt.scatter(gdp_cap,life_exp);
# plt.xscale('log');
# plt.show();


#-------------------------------------------- Corelation -------------------------------------------------------------

#Co-relation ==> Check the effect of change of one value to another.
#postive Corelation=> if one value increase, the other also does.
#zero Corelation=> the increase of one value does not effect others.
#negative Corelation=> if one value increases, the other value decreases.
# x=A, y=B Corelations=> AA AB BB BA

#Postive Corelation Example:

# a=[1,2,3,4,5,6];
# b=[2,4,6,8,9,10];
# plt.plot(a,b);
# plt.show();

#Negative Corelation

# a=[2,4,6,8,10];
# b=[10,8,6,4,2];
# plt.plot(a,b);
# plt.show();

#Zero Corelation

# a=[1,2,3,4,5];
# b=[3,3,3,3,3];
# plt.plot(a,b);
# plt.show();


#------------------------------------------ TASK  -----------------------------------------------------------

#pop=np_country_data[:,3];
# plt.plot(pop,life_exp);
# plt.xscale('log');
# plt.show();

 #Assignment==> what is the type of this corelation??


#-------------------------------------------- HISTOGRAM ---------------------------------------------------
#Takes only one axis and shows how many times a specific value occurs in the data set.

# x=[10,20,30,10,50,60,10,50,20,30,40,50,60,80,90,20,10,20,30,40];
# plt.hist(x);
# plt.show();


#----------------------------------------------- TASK  ----------------------------------------------------

# plt.hist(life_exp);
# plt.show();


#------------------------------------------------- LABELING THE PLOTS -------------------------------------

#plt.title("Graph");
#plt.xlabel("x-axis");
#plt.ylabel("y-axis");


#------------------------------------------ TICKS ----------------------------------------------------

#Use to change the values that can be shown on the scale.
#It changes the represtation of the values on specific x-axis

# x=[5,2,9,4,7];
# y=[10,5,8,4,2];
# color=['red','orange','yellow','pink','blue'];
# plt.scatter(x,y,size=100,c=color,opacity=0.2);
# plt.xticks([5,2,9,4,7],['five','tow','nine','four','seven']);
# plt.show();



#--------------------------------------  TASK ----------------------------------------------------

#Change the values on x-axis and y-axis into string

# x=[10,20,30,40,50,60,70,80,90];
# y=[5,10,15,20,25,30,35,40,45];

# plt.scatter(x,y);
# plt.title("Scatter plot");
# plt.xlabel("x-axis");
# plt.ylabel("y-axis");
# plt.xticks(x,["Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]);
# plt.yticks(y,["Five","Ten","Fifteen","Twenty","Twenty Five","Thirty","Thirty Five","Forty","Forty Five"]);
# plt.show();


#--------------------------------------------  TASK -----------------------------------------------------

# tick_val=[1000,10000,100000];
# tick_lab=['1k','10k','100k'];
# pop=np_country_data[:,3];
# plt.plot(pop,life_exp);
# plt.xticks(tick_val,tick_lab);
# plt.xscale('log');
# plt.show();


#------------------------------------------------ SIZE ------------------------------------------------------


# x=[1,2,3,4,5];
# y=[1,2,3,4,5];
# size=[100,200,300,400,500];
# plt.scatter(x,y,size);
# plt.show();


#----------------------------------------------------- TASK -----------------------------------------------
#Use the array from csv link to set the size of the data points.

# population=pd.read_csv("https:row.githubusercontent.com/Masadn/PythonCourse/master/dataset/popdata1.csv");
#np_population=np.array(population);
# np_pop=np_population[:,0];
# plt.plot(pop,life_exp);


#--------------------------------------  TEXT PLOT -----------------------------------------------------
#Grid is used to locate the positions of different samples


# x=[1,2,3,4,5];
# y=[1,2,3,4,5];
# size=[100,200,300,400,500];
# plt.scatter(x,y,size);
# plt.grid();
# plt.text(3,3,"Sample");
# plt.show();


#------------------------------------------ Dictionaries --------------------------------------------

#Dictionaries are a key-value pair in which we get the values in O(1) time
#{key:value}

# my_dist= {
#     "Lahore":1.9,
#     "Karachi":2.5,
#     "Multan":0.8
# }
# print(my_dist["Karachi"]);
# print(my_dist.keys());
# #Add Elements to the dictionary
# my_dist["islamabad"]=0.6;
# print(my_dist);
#del(my_dist["islamabad"]);



#--------------------------------------------- TASK -----------------------------------------------------
#use index function to find the capital of Germany
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

indexOfGermany=countries.index('germany');
germanyCapital=capitals[indexOfGermany];
print("The capital of the Germany is:",germanyCapital);

#------------------------------------------ TASK --------------------------------------------------------
#create a dictionary of country:capital of name europe

europe={
      
      "spain":"madrid",
      "france":"paris",
      "germany":"berlin",
      "norway":"oslow"

}

print(europe);
#print out all the available keys in Europe Dictionary
print(list(europe.keys()));
#print out all the available values in Europe Dictionary
print(europe.values());
#print out the value that belongs to the norway key in the dictionary
print(europe['norway']);
#Add Rome as the capital of the Europe
europe["italy"]="rome";
#Add poland, warsaw and iceland reykjavik
europe["poland"]="warsaw";
europe["iceland"]="reykjavik";

#Add Austria, Vienna and Germany bonn in the europe
#.update function can be use if we want to add multiple key:value at signle line of code
europe.update({"australia":"vienna","germany":"bonn"});
#update the germany capital back to berlin
europe["germany"]="berlin";
# europe.__delitem__("austria");

#-----------------------------------------------------------------------
#Assignment find out the dynamic way to merge two lists into dictionary
#-----------------------------------------------------------------------


#Viena is not the capital of Australia it is the capital of Austria. Kindly update the dictionary

del(europe["australia"]);
europe["austria"]="vienna";
print(europe);


#------------------------------------------------ NESTED DICTIONARY --------------------------------
#Dictionary with in a Dictionary
pep1={
    "name":"Johne",
     "age":"27",
     "Gender":"Male"
}

pep2={
    "name":"Maria",
     "age":"24",
     "Gender":"Female"
}
pep3={
    "name":"bob",
    "age":26,
    "Gender":"Male"
}

people={
    'person1':pep1,
    'person2':pep2,
    'person3':pep3
}

print(people);

#First get the outer dictionary and then the inner dictionary
print(people["person1"]["name"])

#------------------------------------TASK-------------------------------------------------
#Create dict of dic by using the dictionaries of individual countries

spain={ 'capital':'madrid', 'population':46.77 }
france= { 'capital':'paris', 'population':66.03 }
germany= { 'capital':'berlin', 'population':80.62 }
norway ={ 'capital':'oslo', 'population':5.084 }
europe ={
    "spain":spain,
    "france":france,
    "europe":europe,
    "norway":norway
}
spain_population=europe["spain"]["population"]
france_capital=europe["france"]["capital"]


#Add new dict of capital rome, population 59.83 for italy in europe
italy={"capital":"rome","population":"59.83"};
europe.update({"italy":italy});
print(europe);