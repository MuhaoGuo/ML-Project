import pickle
from sklearn.metrics import f1_score
import pandas as pd

validation = pd.read_csv("validation.csv")
y_validation = validation.loc[:,'ConvertedComp']
x_validation = validation.drop(['MainBranch','ConvertedComp'],axis=1)


best_SVC_model = pickle.load(open('best_SVC_model.sav', 'rb'))
best_LR_L1_model = pickle.load(open('best_LR_L1_model.sav', 'rb'))
best_LR_L2_model = pickle.load(open('best_LR_L2_model.sav', 'rb'))
best_RF_model = pickle.load(open('best_RF_model.sav', 'rb'))

model_list=[]
model_list.append(best_SVC_model)
model_list.append(best_LR_L1_model)
model_list.append(best_LR_L2_model)
model_list.append(best_RF_model)

F1_score_list = []
general_score_list = []
for model in model_list:
    validation_predict = model.predict(x_validation)
    F1_score = f1_score(y_validation, validation_predict, average='weighted')
    F1_score_list.append(F1_score)

    score=model.score(x_validation,y_validation)
    general_score_list.append(score)

print ("F1 score of the four model are:")
print (F1_score_list)
print ("general score of the four model are:")
print (general_score_list)
print ("\n")


index = F1_score_list.index (max(F1_score_list))
print (model_list[index])


filename = 'finalized_model.sav'
pickle.dump(model_list[index], open(filename, 'wb'))   # save the finalized model
