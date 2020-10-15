import pandas as pd

test = pd.read_csv("test.csv")
y_test = test.loc[:,'ConvertedComp']
x_test = test.drop(['MainBranch','ConvertedComp'],axis=1)

import pickle
from sklearn.metrics import f1_score

def main():

    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))    # load the trained model

    test_predict = loaded_model.predict(x_test)

    score_test = loaded_model.score(x_test, y_test)
    F1_score_test = f1_score(y_test, test_predict, average='weighted')

    print("Random forest algorithm: the predit F1 score is\n" + str(F1_score_test))
    print("Random forest algorithm: the predit general score is\n" + str(score_test))

main()





