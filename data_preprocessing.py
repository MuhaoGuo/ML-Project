import pandas
import pandas as pd

# path = '/Users/muhaoguo/Documents/study/EE660/project/survey_results_public.csv'
########################################################################################
data_original = pandas.read_csv("/Users/muhaoguo/Documents/study/EE660/project/survey_results_public.csv")#
data_original = data_original.iloc[:]                                              #
data_original.to_csv('/Users/muhaoguo/Documents/study/EE660/project/data.csv')          #
path = '/Users/muhaoguo/Documents/study/EE660/project/data.csv'                         #
########################################################################################
print (data_original)


# ********  select the useful features
data_original = pandas.read_csv(path, usecols=[2,3,4,5,6,7,9,10,12,13,
                                               14,15,16,17,18,19,20,21,22,23,
                                               32,33,34,36,37,38,39,40,43,55,      ###### 34 NO
                                               56,57,59,60,63,78,79,83])
# Index=['MainBranch', 'Hobbyist', 'OpenSourcer', 'OpenSource', 'Employment',
#        'Country', 'Student', 'EdLevel', 'UndergradMajor', 'EduOther',
#        'OrgSize', 'DevType', 'YearsCode', 'Age1stCode', 'YearsCodePro',
#        'CareerSat', 'JobSat', 'MgrIdiot', 'MgrMoney', 'MgrWant', 'JobSeek',
#        'LastHireDate', 'ConvertedComp', 'WorkWeekHrs', 'WorkPlan',
#        'WorkRemote', 'WorkLoc', 'ImpSyn', 'CodeRev', 'CodeRevHrs',
#        'PurchaseWhat', 'LanguageWorkedWith', 'LanguageDesireNextYear',
#        'DatabaseWorkedWith', 'DatabaseDesireNextYear', 'PlatformWorkedWith',
#        'PlatformDesireNextYear', 'WebFrameWorkedWith',
#        'WebFrameDesireNextYear', 'MiscTechWorkedWith',
#        'MiscTechDesireNextYear', 'DevEnviron', 'OpSys', 'Containers',
#        'BlockchainOrg', 'BetterLife', 'ITperson', 'Extraversion', 'Age',
#        'Gender', 'Dependents']
# cols=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,32,33,34,36,37,38,39,40,43,44,45,46,47,48,49,50,51,52,53,54,55,
#                                         56,57,59,60,63,78,79,83]


index_and_feature=[['MainBranch', 2], ['Hobbyist', 3], ['OpenSourcer', 4], ['OpenSource', 5], ['Employment', 6],
                   ['Country', 7], ['EdLevel', 9], ['UndergradMajor', 10],
                   ['OrgSize', 12], ['DevType', 13], ['YearsCode', 14], ['Age1stCode', 15], ['YearsCodePro', 16],
                   ['CareerSat', 17], ['JobSat', 18], ['MgrIdiot', 19], ['MgrMoney', 20], ['MgrWant', 21], ['JobSeek', 22],
                   ['LastHireDate', 23], ['ConvertedComp', 32], ['WorkWeekHrs', 33], ['WorkPlan','no',34], ['WorkRemote', 36],
                   ['WorkLoc', 37],['ImpSyn', 38], ['CodeRev', 39], ['CodeRevHrs', 40], ['PurchaseWhat', 43],

                   ['LanguageWorkedWith', 44], ['LanguageDesireNextYear', 45], ['DatabaseWorkedWith', 46], ['DatabaseDesireNextYear', 47],
                   ['PlatformWorkedWith', 48], ['PlatformDesireNextYear', 49], ['WebFrameWorkedWith', 50], ['WebFrameDesireNextYear', 51],
                   ['MiscTechWorkedWith', 52], ['MiscTechDesireNextYear', 53],['DevEnviron', 54],


                   ['OpSys', 55], ['Containers', 56], ['BlockchainOrg', 57], ['BetterLife', 59], ['ITperson', 60],
 ['Extraversion', 63], ['Age', 78], ['Gender', 79], ['Dependents', 83]]

####  ********** drop the NaN data
data_original.dropna(axis=0, how='any', inplace=True)

    # ***** drop the sample belong to students/hobby, select the professional programmer
data_original = data_original [True^data_original['MainBranch'].isin(['I am a student who is learning to code'])]
data_original = data_original [True^data_original['MainBranch'].isin(['I am not primarily a developer, but I write code sometimes as part of my work'])]
data_original = data_original [True^data_original['MainBranch'].isin(['I code primarily as a hobby'])]
data_original = data_original [True^data_original['MainBranch'].isin(['I used to be a developer by profession, but no longer am'])]

# data_original = data_original [True^data_original['Student'].isin(['Yes, full-time'])]
# data_original = data_original [True^data_original['Student'].isin(['Yes, part-time'])]

#  ['EdLevel', 9]:
valid_EdLevel = ['I never completed any formal education',
                 'Primary/elementary school',
                 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
                 'Some college/university study without earning a degree',
                 'Associate degree',
                 'Bachelor’s degree (BA, BS, B.Eng., etc.)',
                 'Master’s degree (MA, MS, M.Eng., MBA, etc.)',
                 'Professional degree (JD, MD, etc.)',
                 'Other doctoral degree (Ph.D, Ed.D., etc.)']
data_original = data_original [data_original['EdLevel'].isin(valid_EdLevel)]

#['UndergradMajor', 10]:
valid_UndergradMajor=['Computer science, computer engineering, or software engineering',
                      "Web development or web design",
                      'Information systems, information technology, or system administration',
                      'Mathematics or statistics',
                      'Another engineering discipline (ex. civil, electrical, mechanical)',
                      'A business discipline (ex. accounting, finance, marketing)',
                      'A health science (ex. nursing, pharmacy, radiology)',
                      'A humanities discipline (ex. literature, history, philosophy)',
                      'A natural science (ex. biology, chemistry, physics)',
                      'A social science (ex. anthropology, psychology, political science)',
                      'Fine arts or performing arts (ex. graphic design, music, studio art)',
                      'I never declared a major']
data_original = data_original [data_original['UndergradMajor'].isin(valid_UndergradMajor)]


# ['DevType', 13]:   add 24 features (different jobs)
# print (data_original['DevType'])

career=['Academic researcher','Data or business analyst','Data scientist or machine learning specialist',
            'Database administrator','Designer','Developer, backend','Developer, desktop or enterprise applications',
            'Developer, embedded applications or devices','Developer, frontend','Developer, fullstack','Developer, game or graphics',
            'Developer, mobile','Developer, QA or test','DevOps specialist','Educator','Engineer, data','Engineer, site reliability',
            'Engineering manager','Marketing or sales professional','Product manager','Scientist',
            'Senior Executive (CSuite, VP, etc.)','Student','System administrator']

data_original.index = [i for i in range(data_original.shape[0])]

print ('----------------------------------------------------------------')

# one hot code:
for i in range (len(data_original)):
    careerlist = data_original.loc[i,'DevType'].split(";")
    for item in career:
        if item in careerlist:
            data_original.loc[i,item] = '1'
        else:
            data_original.loc[i,item] = '0'

data_original = data_original.drop(columns=['DevType'])     #delect the original col

print ('-------------------------------------------------------------------')

# ******   reset the index
data_original.index=[i for i in range(data_original.shape[0])]

print ('------------------------------？-----------------------------------------------------')

# ['YearsCode', 14]:   str to int.  special case : Less than 1 year  --->0 ;  More than 50 years--->50
for i in range(len(data_original)):
    if data_original.loc[i,'YearsCode'] == 'Less than 1 year':
        data_original.loc[i, 'YearsCode'] = '0'
    elif data_original.loc[i,'YearsCode'] == 'More than 50 years':
        data_original.loc[i, 'YearsCode'] = '50'
# data_original.loc[i,['YearsCode'] == 'Less than 1 year'] = '0'    #special option    #此方法不行
# data_original['YearsCode'].loc[data_original['YearsCode'] == 'Less than 1 year'] = '0'    #special option
data_original['YearsCode'] = data_original['YearsCode'].astype(int)
print ('-----------------------------？------------------------------------------------------')

#['Age1stCode', 15]:   str to int. special case : Younger than 5 years ---> 5
for i in range(len(data_original)):
    if data_original.loc[i,'Age1stCode'] == 'Younger than 5 years':
        data_original.loc[i, 'Age1stCode'] = '5'

# data_original['Age1stCode'].loc[data_original['Age1stCode'] == 'Younger than 5 years'] = '5'
data_original['Age1stCode'] = data_original['Age1stCode'].astype(int)
print ('----------------------------?--------------------------------------------------------')

# ['YearsCodePro', 16]: str to int : special case: Less than 1 year ---> 0
data_original.loc[data_original['YearsCodePro'] == 'Less than 1 year'] = '0'
data_original['YearsCodePro'] = data_original['YearsCodePro'].astype(int)
print ('----------------------------?--------------------------------------------------------')

# ['ConvertedComp', 32]:   存在0？？############ y label----------------  drop unrealistic data salary==0
data_original['ConvertedComp'] = data_original['ConvertedComp'].astype(int)
data_original = data_original [True^data_original['ConvertedComp'].isin(['0'])]      # drop the unrealistic sample : 0 dollars/year
data_original.index=[i for i in range(data_original.shape[0])]
print ('----------------------------?--------------------------------------------------------')

## set the y_label
for i in range (len(data_original)):
    if data_original.loc[i,'ConvertedComp'] <= 10000:
        data_original.loc[i,'ConvertedComp'] = 'less than 10000'
    elif 10000 < data_original.loc[i,'ConvertedComp'] <= 50000:
        data_original.loc[i,'ConvertedComp'] = '10000-50000'
    elif 50000 < data_original.loc[i,'ConvertedComp'] <= 100000:
        data_original.loc[i,'ConvertedComp'] = '50000-100000'
    elif 100000 < data_original.loc[i,'ConvertedComp'] <= 200000:
        data_original.loc[i,'ConvertedComp'] = '100000-200000'
    else:
        data_original.loc[i,'ConvertedComp'] = 'more than 200000'
# for i in range (len(data_original['ConvertedComp'])):
#     if data_original['ConvertedComp'][i] <= 10000:
#         data_original['ConvertedComp'][i]='less than 10000'
#     elif 10000 < data_original['ConvertedComp'][i] <= 50000:
#         data_original['ConvertedComp'][i] = '10000-50000'
#     elif 50000 < data_original['ConvertedComp'][i] <= 100000:
#         data_original['ConvertedComp'][i] = '50000-100000'
#     elif 100000 < data_original['ConvertedComp'][i] <= 200000:
#         data_original['ConvertedComp'][i] = '100000-200000'
#     else:
#         data_original['ConvertedComp'][i] = 'more than 200000'

# data_original.loc[data_original['ConvertedComp'] <=10000] = 'less than 10000'
# data_original.loc[10000 < data_original['ConvertedComp'] <=50000] = '10000-50000'
# data_original.loc[50000 < data_original['ConvertedComp'] <=100000] = '50000-100000'
# data_original.loc[100000 < data_original['ConvertedComp'] <=200000] = '100000-200000'
# data_original.loc[data_original['ConvertedComp'] > 200000] = 'more than 200000'
print ('-----------------------------?-------------------------------------------------------')

# ['WorkWeekHrs', 33]：
data_original['WorkWeekHrs'] = data_original['WorkWeekHrs'].astype(int)
print ('------------------------------------------------------------------------------------')

# ['CodeRevHrs', 40]
data_original['CodeRevHrs'] = data_original['CodeRevHrs'].astype(int)
print ('------------------------------------------------------------------------------------')

# ['Age', 78] 有0 ???     drop the unrealistic data age==0
# ******   reset the index
data_original['Age'] = data_original['Age'].astype(int)
data_original = data_original [True^data_original['Age'].isin(['0'])]     #drop the unrealistic sample 0 years old
data_original.index=[i for i in range(data_original.shape[0])]
print ('------------------------------------------------------------------------------------')


# We should encode every str feature data to a numbertic type use LabelEncoder:
import sklearn.preprocessing
int_feature=['YearsCode',	'Age1stCode'	,'YearsCodePro','WorkWeekHrs'	,'CodeRevHrs','Age'	,
             'Academic researcher'	,'Data or business analyst'	,'Data scientist or machine learning specialist',
             'Database administrator'	,'Designer'	,'Developer, backend','Developer, desktop or enterprise applications'	,
             'Developer, embedded applications or devices','Developer, frontend',
             'Developer, fullstack','Developer, game or graphics','Developer, mobile','Developer, QA or test',
             'DevOps specialist','Educator','Engineer, data','Engineer, site reliability','Engineering manager',
             'Marketing or sales professional','Product manager','Scientist','Senior Executive (CSuite, VP, etc.)',
             'Student','System administrator']

str_feature=['Hobbyist'	,'OpenSourcer','OpenSource','Employment',	'Country',
             'EdLevel'	,'UndergradMajor'	,'OrgSize'	,'CareerSat'	,'JobSat',
             'MgrIdiot',	'MgrMoney',	'MgrWant'	,'JobSeek',	'LastHireDate',
             'WorkPlan'	, 'WorkRemote'	,'WorkLoc'	,'ImpSyn'	,'CodeRev',
             'PurchaseWhat'	,'OpSys','Containers'	, 'BlockchainOrg'	,'BetterLife' ,
             'ITperson'	,'Extraversion', 'Gender',	'Dependents']

label=['ConvertedComp']

# encode data : transfrom the str features to int features
le = sklearn.preprocessing.LabelEncoder()
for feature in str_feature:
    data_original.loc[:, feature] = le.fit_transform(data_original[feature])

from sklearn.model_selection import train_test_split
train, test = train_test_split(data_original, test_size=0.3)
train, validation = train_test_split(train, test_size=0.25)

train.index = [i for i in range(train.shape[0])]
test.index = [i for i in range(test.shape[0])]
validation.index = [i for i in range(validation.shape[0])]


data_original.to_csv('/Users/muhaoguo/Documents/study/EE660/project/data_train+test+validation.csv')
train.to_csv('/Users/muhaoguo/Documents/study/EE660/project/train.csv')
test.to_csv('/Users/muhaoguo/Documents/study/EE660/project/test.csv')
validation.to_csv('/Users/muhaoguo/Documents/study/EE660/project/validation.csv')


train_path = '/Users/muhaoguo/Documents/study/EE660/project/train.csv'
train = pd.read_csv(train_path, index_col=0)
test_path = '/Users/muhaoguo/Documents/study/EE660/project/test.csv'
test = pd.read_csv(test_path, index_col=0)
validation_path = '/Users/muhaoguo/Documents/study/EE660/project/validation.csv'
validation = pd.read_csv(validation_path, index_col=0)

print("train")
print(train)
print("test")
print(test)
print("validation")
print(validation)


#####  separate x and y：
y_train = train.loc[:,'ConvertedComp']
x_train = train.drop(['MainBranch','ConvertedComp'],axis=1)

y_test = test.loc[:,'ConvertedComp']
x_test = test.drop(['MainBranch','ConvertedComp'],axis=1)

y_validation = validation.loc[:,'ConvertedComp']
x_validation = validation.drop(['MainBranch','ConvertedComp'],axis=1)

print ('------------here is data preprocessing---------------------')