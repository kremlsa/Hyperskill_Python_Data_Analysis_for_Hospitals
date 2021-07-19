import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv
import seaborn as seaborn

data = {}
data.update({"general": pd.read_csv('test/general.csv')})
data.update({"prenatal": pd.read_csv('test/prenatal.csv')})
data.update({"sports": pd.read_csv('test/sports.csv')})
# Preparing data
data["prenatal"].rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
data["sports"].rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
hospitals = pd.concat([data["general"], data["prenatal"], data["sports"]], ignore_index=True)
hospitals.drop(columns='Unnamed: 0', inplace=True)
# replace Nan with zeros
hospitals = hospitals.fillna(0)
# delete empty line
for index, row in hospitals.iterrows():
    if row['hospital'] == 0:
        hospitals.drop(index=index, inplace=True)
hospitals['gender'] = hospitals['gender'].replace([0, 'female', 'woman'],'f')
hospitals['gender'] = hospitals['gender'].replace(['male', 'man'],'m')
# graphs
print("The answer to the 1st question is {}".format(hospitals['hospital'].value_counts(ascending=False).idxmax()))
hospitals['hospital'].value_counts().plot(kind="hist")
plt.show()
print("The answer to the 2nd question is {}".format(hospitals['diagnosis'].value_counts(ascending=False).idxmax()))
hospitals['diagnosis'].value_counts(ascending=False).plot(kind='pie')
plt.show()
print("The answer to the 3rd question is It's because...")
seaborn.violinplot(x="hospital", y="height", data=hospitals)
plt.show()
