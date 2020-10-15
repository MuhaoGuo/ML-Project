import pandas

data_all = pandas.read_csv("data_train+test+validation.csv")
y_all = data_all.loc[:,'ConvertedComp']
x_all = data_all.drop(['MainBranch','ConvertedComp'],axis=1)

num = len(y_all)

class1 = 0 #less than 10000
class2 = 0 #10000-50000
class3 = 0 #50000-100000
class4 = 0 #100000-200000
class5 = 0 #more than 200000

for i in y_all:
    if i =="less than 10000":
        class1+=1
    elif i =="10000-50000":
        class2+=1
    elif i=="50000-100000":
        class3+=1
    elif i=="100000-200000":
        class4+=1
    elif i == "more than 200000":
        class5+=1

print("percentage of calss1 is "+ str (class1/num))
print("percentage of calss2 is "+ str (class2/num))
print("percentage of calss3 is "+ str (class3/num))
print("percentage of calss4 is "+ str (class4/num))
print("percentage of calss5 is "+ str (class5/num))

print("\n")
# one Vs rest (transform to binary class)is the data linear separable? use perceptron and F1 score to evaluate.
from sklearn.linear_model import Perceptron
from sklearn.metrics import f1_score

clf = Perceptron(tol=1e-3, random_state=0)
for classi in ["less than 10000","10000-50000","50000-100000","100000-200000","more than 200000"]:
    label=[]
    for i in y_all:
        if i == classi:
            label.append(1)
        else :
            label.append(0)

    clf.fit(x_all, label)
    y_predict = clf.predict(x_all)

    F1_score = f1_score(label, y_predict, average='weighted')

    print ("calss of "+classi+" with the rest class, F1 score is " + str (F1_score))

# multiclass : is the data linear separable? use perceptron and F1 score

clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(x_all, y_all)
y_predict = clf.predict(x_all)
F1_score = f1_score(y_all, y_predict, average='weighted')
print("\n")
print ("multiclass, total F1 score is " + str (F1_score))

