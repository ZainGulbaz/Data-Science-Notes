#---------------------------- LOGIICAL OPERATORS -----------------------------------------------------------

#The most common logical operators used in python are less than <, greater than >,  euqals to = and less than or equals to <= and greater than or 

#For strings it does alphabetical comparison



#Numpy array comparison
import numpy as np;


#in numpy it does the element ot element comparison and returns a logical array
a=np.array([1,2,3]);
b=np.array([4,5,0]);
print(np.greater(a,b));


#--------------------------------------  TASK --------------------------------------------------------------

#Kitchen,living room ,bedroom and bathroom

my_house=np.array([18.0,20.0,10.75,9.50]);
your_house=np.array([14.0,24.0,14.25,9.0]);

print(" ");
#Which area in my house are equal to greater than 18.0
print("my_house area greater than equal to 18==>",my_house>=18);
#Which area in your house is equal to greater than 15.0
print("your_house area is greater than or equal to 15.0==>", your_house>=15);
#Which area my_house are smaller than the areas in your house
print("areas in my_house are smaller than the one in your house==>",my_house<your_house);



#-----------------------------------  BOOLEAN OPERATORS ------------------------------------------------------------

#The logical operators AND, OR and NOT are also logical operators that are also known as boolean operators.
#1- AND    2-OR    3-NOT

print(" ");
#AND True if both conditions are true
print("Examples of AND operator==>",2<5 and 5>3);

#OR True if only one condition is true
print("Example of OR operator==>", 2>5 or 1<2);

#NOT operaor it needs only one operand and reciprocates its value

print("Example of not operator==>",not(True),not(False));



#----------------------------------------- TASK --------------------------------------------------------------

my_kitchen=18.0;
your_kitchen=14.0;
print(" ");
print("My kitchen is greater than 10==>",my_kitchen>10);
print("Your kitchen is less than 18==>",your_kitchen<18);
print("My kitchen is smaller than 14 or bigger than 17==>",my_kitchen<14 or my_kitchen>17);

#--------------------------------------TASK------------------------------------------------------------
#check if double the area of my kitchen is smaller than triple the area of your kitchen

double_my_kitchen=2*my_kitchen;
triple_your_kitchen=3*your_kitchen;
print("");
print("Double of my kitchen is smaller than triple of your kitchen=>",double_my_kitchen<triple_your_kitchen);

#---------------------------------------- TASK --------------------------------------------------------
#Which areas in my_house are greater than 18.5 or less than 10 

print("");
print("reas in my_house are greater than 18.5 or less than 10 ==>",np.logical_or(my_house>=18.5, my_house<10));


#----------------------------------------------  TASK -----------------------------------------------
#Which areas are smaller than 11 in both my_house and your_house
print("");
print("areas are smaller than 11 in both my_house and your_house ==>",np.logical_and(my_house<11,your_house<11));


#------------------------------------------- IF CONDITION ------------------------------------------------
print("");

a=10;
if(a>15):
    print("This is a true statement");
else: 
   print("This is a false statement");


#------------------------------------------ TASK --------------------------------------------------------
print("");
room="kit";
area=14.0;


#check if room is kit it should print  "Looking around in the kitchen"

if(room=="kit"):
    print("Looking around in the kitchen");

#if area is greater than 15 print big place else small place
if(area>15):
    print("Big Place");
else:
    print("Small Place");


#------------------------------------------- elif -----------------------------------------------------

# if(room=="kit"):
#     print("Looking around in the kitchen");
# elif(room=="bed"):
#     print("Looking around in the bedroom");
# else:
#     print("Not looking anywhere");


#-----------------------------------------  TASK --------------------------------------------------------
area=14.0;

print("");
print("Checking the place size");
if(area>15):
    print("Big Place");
elif(area==14):
    print("Medium Place");
else: 
    print("Pretty Small");


#---------------------------------------------- LOOPS  ------------------------------------------------------

x=1;

#while loop
while(x<=10):
    print(x);
    x=x+1;


#------------------------------------------ TASK -----------------------------------------------------------
#Create a variabable offset with initial value 8 and run the loop as long as it is equals to 8 print("correcting...")
print(" ");

offset=8;
while(offset!=0):
    offset=offset-1;
    print("Correcting....");

#Now do it for offset equals to -6
print(" ");
offset=-6;
while(offset!=0):
    offset=offset+1;
    print("Correctiing....");

#----------------------------------------------  TASK   --------------------------------------------------------

error=40;

print(" ");

while(error>1):
    if error==10:
      error=error/2;
    else:
      error=error/4; 
    print(error); 


#--------------------------------------------  FOR LOOP -----------------------------------------------------------

fam=[1.73,1.68,1.71,1.89];

print(" ");
for x in fam:
    print(x);


#----------------------------------------------- TASK -----------------------------------------------------------
#iterate all of the values in the list
areas=[11.25,18.0,20.0,10.75,9.50];
print(" ");
print("Printing the areas list");
for area in areas:
    print(area);
   

#--------------------------------- LOOP over indexing ------------------------------------
print(" ");
print("Looping over indexing");
areas=[11.25,18.0,20.0,10.75,9.50];

for index,value in enumerate(areas):
    print(index,value);

#-------------------------------------------- TASK ------------------------------------------------------
#print the results of areas in the form of result x:y

print(" ");
print("TASK");
for index,value in enumerate(areas):
    print("Result ",index," : ",value);

#------------------------------------- LOOP OVER DICTIONARIES -----------------------------------------------
statesandcapitals={"Albama":"Montogemry","Alaska":"Juneau"}

print(" ");
print("traverse dictionary with for loop");
for key,value in statesandcapitals.items():
    print(key,value);


#------------------------------------------ TASK -----------------------------------------------------------
#Traverse through the list of europe array
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna'}

print(" ");
print("TASK");
for country,city in europe.items():
    print("The capital of ",country," is ",city);


#--------------------------------------- TRAVERSE THROUGH ARRAY ---------------------------------------------
arr= np.array([1,3,5,6,7,8]);
print(" ");
print("TRAVERSE THROUGH ARRAY");
for value in arr:
    print(value);

#----------------------------------------- LOOP OVER 2D ARRAY ---------------------------------------------


list=[[1,2],[3,4],[5,6],[7,8]]
array=np.array(list);

print(" ");
print("TRAVERSE IN 2D ARRAY")
for value in np.nditer(array):
    print(value);



#------------------------------------------ TASK -----------------------------------------------------
import pandas as pd;

response= pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/baseball_height_weight.csv");

dataArray= np.array(response);
print(" ");
print("TASK");

heights= dataArray[:,0];

# for height in heights:
#     print(height);

#now print every element of it

# for value in np.nditer(dataArray):
#     print(value);