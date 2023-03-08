#your code here
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('score.csv')
#print(df)
X = np.array(df['Hours'])
Y = np.array(df['Scores'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

X = X.reshape(-1,1)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)

lr = LinearRegression().fit(X_train, Y_train)

print(f"Linear Regression-Training set score: {lr.score(X_train, Y_train):.2f}")
print(f"Linear Regression-Test set score: {lr.score(X_test, Y_test):.2f}")

lr.predict([[5], [10], [15]])


plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, lr.predict(X_train))
plt.title('Training set')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

plt.scatter(X_test, Y_test, color='green')
plt.plot(X_test, lr.predict(X_test))
plt.title('Test set')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

plt.scatter(X, Y, color='yellow')
plt.plot(X, lr.predict(X))
plt.title('Predictions')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()
