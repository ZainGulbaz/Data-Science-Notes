



#---------------------------------PANDAS------------------------------------------------------------------
#PANDAS is used to fetch the data from remote servers.
#Its name is derived from "Panel Data"

#--------------------------------------DATA FRAME----------------------------------------------------------
#Default result from pandas read_csv is a data frame.
#It consists of data,rows and columns.
#Summarize tables don't have JOINS.
import pandas as pd;

Name=["Bob","Alex","Maria","Nick","Chandler"];
Age=[25,26,None,12,20];
Gender=["Male","Male","Female","Male","Male"];
Course=["Math","Physics","Chemistry","English","Computer"];

Data={
    "Name":Name,
    "Age":Age,
    "Gender":Gender,
    "Course":Course
}

Students=pd.DataFrame(Data);
#print(Students);

#---------------------------------------TASK---------------------------------------------------------
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, None]

Data={
    "country":names,
    "drives_right":dr,
    "cars_per_cap":cpc
}
#Label the data frame
row_labels=['US','AUS','JPN','IN','RU','MOR','EG'];

#Convert the data into data frame
Countries=pd.DataFrame(Data);
Countries.index=row_labels
# print(Countries);


#------------------------------------- READ CSV ------------------------------------------------
#80% of the time, we will deal with CSV


Cars=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/cars.csv",index_col =0); 

# print(Cars);


#call the column in data frame
# print(Cars.country)
# print(Cars[["country","cars_per_cap"]]); 
# print(Cars[["cars_per_cap","drives_right"]]);

#Specify the number of rows
# print(Cars[0:3]);


#Select first two rows from Cars
#print(Cars[0:2]);

#Select the sixth row only
# print(Cars[5:6]);


#-----------------------------iloc vs loc------------------------------------------------------------
#For loc we need to specify column name
#print(Students);
#print(Students.loc[Students['Gender']=='Male'])
#print(Students.loc[0:2],["Zero","Two"]);

#iloc reads only integers

#-------------------------------------- TASK---------------------------------------------------------
#Show the row with label "JAP"

#print(Countries);
# print(Countries.loc["JPN"]);


#-------------------------------------- TASK--------------------------------------------------------
#Print the country and drive_right for Morocco and Russia
#print(Countries.loc[["MOR","RU"],["country","drives_right"]]);

#-------------------------------------- TASK--------------------------------------------------------
#Print all rows and specified column drives_right

#loc
# print(Countries.loc[:,["drives_right"]]);

#iloc
# print(Countries.iloc[:,[1]]);

#--------------------------------------- TASk ----------------------------------------------------------------
#print cars_per_cap and drives_right column as Data Frame

#using loc
# print(Countries.loc[:,["cars_per_cap","drives_right"]]);

#using iloc

# print(Countries.iloc[:,[2,1]]);

# print(Countries.loc(Countries[["carrs_per_cap"]]=80))




