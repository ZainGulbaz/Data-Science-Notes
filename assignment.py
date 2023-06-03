import numpy as np;


def convert1Dto2D(arr1,arr2):
     if(len(arr1)!=len(arr2)):
          print("The length of the arrays must be same");
          return False;
     if(arr1.ndim!=1 or arr2.ndim!=1):
          print("The dimension of both arrays should be one");
          return False; 
     if(type(np.array([2]))!=type(arr1) or type(np.array([2]))!=type(arr2)):
           print("The type is not array");
           return False;
     return(np.vstack((arr1, arr2)).T);


arr1=np.array([1,2,3,4,5,6]);
arr2=np.array([7,8,9,10,11,12]);
newArr=convert1Dto2D(arr1,arr2);
print(newArr);
