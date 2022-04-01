import numpy as np
import math


# change here
weight= np.array([-3,1,3])
sample_X = np.array([[1,1,1]])
sample_y = np.array([1])


learning_rate = 1
x0 = 1
total = 0
result_list = []
sy_list = []

net = sum(sample_X * weight)

for i in net:
  total = total + i
print("First total is ", total)
nn_str = f"net = w0x0 + w1x1 + w2x2 = {total}"
nn_str2 = f"yprime f(net) = ({weight[0]})({sample_X[0][0]}) + ({weight[1]})({sample_X[0][1]}) + ({weight[2]})({sample_X[0][2]}) = {total} "
print(nn_str)
print(nn_str2)
print("\n")
# y is sample_y[0]
# y' is total
if total != int(sample_y[0]):
  print("Misclassified, learning occurs.")
  w = weight + (learning_rate * (sample_y[0] - total) * sample_X[0])
  w_str = f"w(x) = w(x-1) + n * (y-y') * sx = {w}"
  print(w_str)
  w_str2 = f"{weight}+1*({sample_y[0]}-{total})*{sample_X[0]} = {w}"
  print(w_str2)
  
  total = 0
  for i in w:
    total = total + i
  
  print("New total is : ",total)
  
  if total >= 0 :
    print("label is 1")
  else:
    print("label is 0")
else:
  print("corectly classified, label is ", sample_y[0])
  
  
print("\n")


  

