from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
iris=load_iris()
ind_f = iris.data[:,:-1]
de_f = iris.target
x_test,x_train,y_test,y_train = train_test_split(ind_f, de_f, test_size = 0.33)
treemodel = DecisionTreeClassifier(max_depth=2)
treemodel.fit(x_train,y_train)
y_predict=treemodel.predict(x_test)
score = accuracy_score(y_predict,y_test)
print(score)
print(classification_report(y_predict,y_test))
plt.figure(figsize=(15,10))
tree.plot_tree(treemodel,filled=True)
plt.show()