import numpy as np


model = np.array([[150, 1.5, 2], [100, 1, 1.5], [50, 0.5,1.8]])
sample = np.array([[2104,5,460],[1416,3,232],[1534,4,315]])

result_list = []
n = 3
sz_list = []

for i in range(len(model)):
  #print("when i is ", i)
  w0 = model[i][0]
  w1 = model[i][1]
  w2 = model[i][2]
  for j in range(len(sample)):
    print("i = ", i, " j = ", j, ",")
    sx = sample[j][0]
    sy = sample[j][1]
    sz = sample[j][2]
    
    sz_list.append(sz)
    the_eq = "y' = (" + str(w0) + ")(1) + (" + str(w1) + ")(" + str(sx) + ") + (" + str(w2) + ")(" + str(sy) +")" 
    print(the_eq)
    #print("w0 : ", w0)
    #print("w1 : ", w1)
    #print("sx : ", sx)
    #print("sy : ", sy)
    
    result = w0*1 + w1*sx + w2*sy
    result_list.append(result)
    print("= ", result)
    
    print("\n")
  #print(result_list)
  #result_list = []
  mse = ((((sz_list[0]-result_list[0])**2) + ((sz_list[1]-result_list[1])**2) + ((sz_list[2]-result_list[2])**2))/n)
  round(mse, 2)
  print("mse for model ", i+1, " is : ", mse, "\n")  
  result_list = []
  sz_list = []
  
  
  
  

