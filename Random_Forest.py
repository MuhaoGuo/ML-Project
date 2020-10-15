from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from sklearn.model_selection import GridSearchCV

train = pd.read_csv("train.csv")
y_train = train.loc[:,'ConvertedComp']
x_train = train.drop(['MainBranch','ConvertedComp'],axis=1)


def Randomforest_Algorithm(Train_X,Train_Y):
    clf_RF = RandomForestClassifier()
    parameters = {'n_estimators': [i for i in range(600, 1200, 50)],
                  'max_features': [i for i in range(6, 10)],
                  'max_depth': [None, 10, 20]}

    clf = GridSearchCV(clf_RF, param_grid=parameters, cv=5)
    clf.fit(Train_X, Train_Y)

    best_estimator = clf.best_estimator_

    best_parameter = clf.best_params_
    print ("the parameters for the best model are "+ str(best_parameter))

    best_score = best_estimator.score(Train_X, Train_Y)
    print("the training score for the best model is " + str(best_score))

    filename = 'best_RF_model.sav'
    pickle.dump(best_estimator, open(filename, 'wb'))

if __name__ == '__main__':
    Randomforest_Algorithm(x_train, y_train)