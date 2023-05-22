#-----------------Functions---------------------
# Two Types of Functions:
# 1- Pre defined 
# 2- User defined

# On the basis of data:
# 1- Row Level Functions (String/varchar data)
# 2- Aggregative Functions (Numeric data)
#In summary, aggregative functions operate on collections of values and provide summary statistics or aggregated results, while row lelvel functions operate on individual numeric values and perform mathematical operations on them.

#--------------------Types of Columns-----------------
#1- Base Column (The column that is imported from any database)
#2- Derived Column (The column that is derived after implementing some functions on the base column)

#------------------------Table -------------------------
#Combination of the rows and columns
# rows are the data while columns are their attributes


#-------------------------len() function-------------
#it is used to find the length of the list/string

# print(len("Hello"));
# a=[1,2,3,4,5];
# print(len(a));

#-------------------------------TASK-----------------------
#Find length of the List

# var1=[1,2,3,4]
# print(len(var1));


#------------------------------TASK-----------------------
#Convert the below variable into int from boolean

# var2=True;
# var3=int(var2);
# print(var3, type(var3));

#------------------------HELP FUNCTION-----------------
#Gives you the details of the function

#--------------------------STRING METHODS--------------------
#1- upper() to capitalize the string
#2- lower() to lower case the string
#3- count() to count a particular character in the string

# var4="today is monday, our 3 python class";
# print(var4.upper());
# print(var4.lower());
# print(var4.count('o'));

#---------------------TUPLE--------------------------------

#A technique in which we store data at same memeory location
# we separate the data with commas

#---------------------TASK---------------------------------

# place="poolhouse";
# place_up=place.upper();
# print(place,place_up);

#---------------------TASK----------------------------------

#place="poolhouse";
#print(place.count("0"));

#---------------------LIST METHODS--------------------------

# a=["apple","oranges","banana","mangos","apple","apple"];
# print(a.index("banana"));
# print(a.count("apple"));

#-----------------------TASK-------------------------------

# areas=[11.25,18.0,20.0,10.75,9.50];
# print(areas.index(20.0));

#---------------------------TASK-----------------------------

#How many times 9.50 appears in the list
# areas=[11.25,18.0,20.0,10.75,9.50];
# print(areas.count(9.50));


#------------------------MORE LIST METHODS-------------------

# list=[1,2];
# list.append(3);
# print(list);
# list.remove(2);
# print(list);
# list.reverse();
# print(list);

#---------------------------TASK ---------------------------
#Add 24.5 and 15.45 to the list
# areas=[11.25,18.0,20.0,10.75,9.50];
# areas.append(24.5);
# areas.append(15.45);
# print(areas);


#-----------------------------TASK----------------------------

#Reverse the order of the elements in areas and print out areas

# areas=[11.25,18.0,20.0,10.75,9.50];
# areas.reverse();
# print(areas);




#-----------------------IMPORT LIBRARIES-------------------

# import math;
# from math import pi;
# print(pi);

#-------------------------TASK----------------------------

#Calculate the area of the circle with radius=0.43

# from math import pi;
# area=(pi)*(0.43*0.43);
# print(round(area,4));










