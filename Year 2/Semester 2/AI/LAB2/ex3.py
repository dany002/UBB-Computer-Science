#your code here
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet

df = pd.read_csv('score.csv')
#print(df)
X = np.array(df['Hours'])
Y = np.array(df['Scores'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

X = X.reshape(-1,1)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)

ridge = Ridge(alpha=0.7).fit(X_train, Y_train)

print("L2 regularization(Ridge)")
print(f"Ridge Regression-Training set score: {ridge.score(X_train, Y_train):.2f}")
print(f"Ridge Regression-Test set score: {ridge.score(X_test, Y_test):.2f}\n")

lasso = Lasso(alpha=1.0).fit(X_train, Y_train)
print("L1 regularization(Lasso)")
print(f"Lasso Regression-Training set score: {lasso.score(X_train, Y_train):.2f}")
print(f"Lasso Regression-Test set score: {lasso.score(X_test, Y_test):.2f}\n")

elastic_net = ElasticNet(alpha=0.01, l1_ratio=0.01).fit(X_train,Y_train)

print("Elastic Net")
print(f"Elastic Net-Training set score: {elastic_net.score(X_train, Y_train):.2f}")
print(f"Elastic Net-Test set score: {elastic_net.score(X_test, Y_test):.2f}
