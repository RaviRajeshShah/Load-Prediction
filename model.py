
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df=pd.read_csv(r"D:\PythonForDs\DS64\ML\ML_dataset\classification\loan_default_2000rows.csv")

le=LabelEncoder()

df['EmploymentStatus']=le.fit_transform(df['EmploymentStatus'])
df['MaritalStatus']=le.fit_transform(df['MaritalStatus'])
df['Defaulted']=le.fit_transform(df['Defaulted'])

# col=df.columns
# for i in col:
#     print(df[i].isnull().sum())
#
# df.duplicated().sum()
# print(df.head())

x=df[['Age','Income','LoanAmount','LoanTerm','CreditScore','EmploymentStatus','MaritalStatus','PreviousDefaults']]
y=df['Defaulted']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()

model.fit(x_train,y_train)

y_predict=model.predict(x_test)

acc=accuracy_score(y_test,y_predict)

print("Accuracy of the model is ",acc*100,"%")

fh=open('model.pkl','wb')

pickle.dump(model,fh)
fh.close()


