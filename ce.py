import numpy as np
import math

n = 3
x0 = 1
e = math.e

model = np.array([[1, 0.01], [1.5, 0.02], [2, 0.05]])


sample = np.array([[5,1],[2,0],[4,1]])
result_list = []
sy_list = []

for i in range(len(model)):
  #print("when i is ", i)
  w0 = model[i][0]
  w1 = model[i][1]
  for j in range(len(sample)):
    print("i=", i, " j=", j, ",")
    sx = sample[j][0]
    sy = sample[j][1]
    sy_list.append(sy)
    
    result = w0*x0 + w1*sx
    result_list.append(result)
    
    the_eq = "S" + str(j+1) +  "=(" + str(w0) + ")(1)+(" + str(w1) + ")(" + str(sx) + ")"
    print(the_eq, "= ", result)

  yprime_list = []
  for count, i in enumerate(result_list):
    yprime = (1/(1 + (e ** (-i)))).round(4)
    yprime_str = f"1/(1 + e^-{i}) = {yprime}"
    print(yprime_str)
    yprime_list.append(yprime)
  
  logloss_list = []
  for count, i in enumerate(yprime_list):
    
    logloss = (- sy_list[count] * math.log(i,e) - (1 - sy_list[count]) * math.log((1 - i),e)).round(4)
    logloss_str = f"-({sy_list[count]})log({i})-(1-{sy_list[count]})log(1-{i}) = {logloss}"
    print(logloss_str)
    logloss_list.append(logloss)
    
  cost = ((logloss_list[0] + logloss_list[1] + logloss_list[2]) / 3).round(4)
  print("Cost is ", cost)
  result_list = []
  sy_list = []
  yprime_list = []
  logloss_list = []
  
  print("\n")
  
  
  
  

