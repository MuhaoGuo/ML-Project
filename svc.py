from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import pandas as pd
import pickle

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
y_train = train.loc[:,'ConvertedComp']
x_train = train.drop(['MainBranch','ConvertedComp'],axis=1)

# y_test = test.loc[:,'ConvertedComp']
# x_test = test.drop(['MainBranch','ConvertedComp'],axis=1)

def SVC_Algorithm(Train_X,Train_Y):

    # validation to select the best parameters
    param_grid = {'gamma': [10000, 1000, 100, 10, 1, 0.1], 'C': [10000, 1000, 100, 10, 1, 0.1]}
    clf_SVC = SVC()
    clf = GridSearchCV(clf_SVC, cv=10, param_grid=param_grid)

    clf.fit(Train_X, Train_Y)

    best_params = clf.best_params_
    best_score = clf.best_score_
    best_estimator = clf.best_estimator_     # our selected model

    print ("the parameters for the best model are " + str(best_params))
    print ("the training score for the best model is " + str(best_score))

    filename = 'best_SVC_model.sav'
    pickle.dump(best_estimator, open(filename, 'wb'))

    # score_test = best_estimator.score(Train_X, Train_Y)
    # print("SVC Algorithm: the train score is " + str(SVC_Algorithm(x_train, y_train)))

    return best_score

SVC_Algorithm (x_train, y_train)
