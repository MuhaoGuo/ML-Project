from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import GridSearchCV
import pandas as pd
import pickle
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
y_train = train.loc[:,'ConvertedComp']
x_train = train.drop(['MainBranch','ConvertedComp'],axis=1)

# y_test = test.loc[:,'ConvertedComp']
# x_test = test.drop(['MainBranch','ConvertedComp'],axis=1)

def Logistic_Regression_Algorithm_l2penalty(Train_X,Train_Y):

    # validation

    # parameters = {'C': [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 1, 10, 100, 10**3, 10**4, 10**5]}
    # # val_list = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 1, 10, 100, 10**3, 10**4, 10**5]
    # clf_LR_l2= LogisticRegression(penalty="l2", multi_class="multinomial", max_iter=100000, solver="lbfgs")
    #
    # clf = GridSearchCV(clf_LR_l2, param_grid=parameters, cv=10)
    # clf.fit(x_train, y_train)
    c_list = [10 ** -5, 10 ** -4, 10 ** -3, 10 ** -2, 10 ** -1, 1, 10, 100, 10 ** 3, 10 ** 4, 10 ** 5]
    clf = LogisticRegressionCV (Cs=c_list, cv=10, penalty="l2", multi_class="multinomial", max_iter=10000, solver="lbfgs")   # CV =10
    clf.fit(Train_X, Train_Y)

    # best parameter
    best_params = clf.C_
    print("best parameters C for LR with l2 penalty: \n" + str(best_params))

    # selected model
    score_train = clf.score(Train_X, Train_Y)
    print("Logistic Regression Algorithm with l2 penalty: the training score is \n" + str(score_train))

    filename = 'best_LR_L2_model.sav'
    pickle.dump(clf, open(filename, 'wb'))

    return score_train

# print ("Logistic Regression Algorithm with l2 penalty: the predict score is "+str(Logistic_Regression_Algorithm_l2penalty(x_train, y_train, x_test, y_test)))

def Logistic_Regression_Algorithm_l1penalty(Train_X, Train_Y):

    # validation
    c_list = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 1, 10, 100, 10**3, 10**4, 10**5]
    # solver="liblinear" is used for l1 penalty

    clf = LogisticRegressionCV (Cs=c_list, cv=10, penalty="l1", multi_class="ovr", max_iter=10000, solver="liblinear")   #CV=10
    clf.fit(Train_X, Train_Y)

    # best parameter
    best_params = clf.C_
    print("best parameters C for LR with l1 penalty:\n" + str(best_params))

    score_train = clf.score(Train_X,Train_Y)
    print("Logistic Regression Algorithm with l1 penalty: the training score is \n" + str(score_train))

    filename = 'best_LR_L1_model.sav'
    pickle.dump(clf, open(filename, 'wb'))

    return score_train

# print ("Logistic Regression Algorithm with l1 penalty: the predict score is "+str(Logistic_Regression_Algorithm_l1penalty(x_train, y_train, x_test, y_test)))
# print ("\n\n")

Logistic_Regression_Algorithm_l1penalty(x_train, y_train)
Logistic_Regression_Algorithm_l2penalty(x_train, y_train)