import math

TP = 2
TN = 16
FP = 1
FN = 1

#| TP  FP |
#| FN  TN |

accuracy = ((TP+TN)/(TP+TN+FP+FN))
accuracy = round(accuracy, 4)

precision = (TP/(TP+FP))
precision = round(precision, 4)



recall_sensitivity = (TP/(TP+FN))
recall_sensitivity = round(recall_sensitivity, 4)

specificity = (TN/(TN+FP))
specificity = round(specificity, 4)

f1score = ((2*TP)/((2*TP)+FP+FN))
f1score = round(f1score, 4)

# true positive rate
TPR = recall_sensitivity

# false positive rate
FPR = (FP/(FP+TN))
FPR = round(FPR, 4)


print("Accuracy : ")
x1 = f"({TP}+{TN})/({TP}+{TN}+{FP}+{FN}) = {accuracy}"
print(x1)
print("\n")
print("Precision : ")
x2 = f"{TP}/({TP}+{FP}) = {precision}"
print(x2)
print("\n")
print("Recall/Sen  : ")
x3 = f"{TP}/({TP}+{FN}) = {recall_sensitivity}"
print(x3)
print("\n")
print("Specificity  : ")
x4 = f"{TN}/({TN}+{FP}) = {specificity}"
print(x4)
print("\n")

print("F1 score : ")
x5 = f"(2*{TP})/((2*{TP})+{FP}+{FN}) = {f1score}"
print(x5)
print("\n")

print("true positive rate  : ")
x6 = f"{TP}/({TP}+{FN}) = {TPR}"
print(x6)
print("\n")

print("false positive rate : ")
x7 = f"{FP}/({FP}+{TN}) = {FPR}"
print(x7)
