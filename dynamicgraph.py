import matplotlib.pyplot as plt
import numpy as np
from array import *

x = array('i',[])
y=array('i',[])
n=int(input("Enter the number of points\n"))
print("Enter the values of x\n")
for i in range(n):
    x.append(int(input("x coordinate : ")))
print("Enter the values of y\n")
for i in range(n):
                 y.append(int(input("y coordinate: ")))
plt.figure(figsize=(len(x),len(y))) 
plt.plot(x,y) 
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.title("Line Graph")
plt.grid()
plt.show()



    
            
        
    
         

         
     
    
        

        
    
    


    

