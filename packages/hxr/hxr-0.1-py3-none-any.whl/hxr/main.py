def slp():
    code = """
import numpy as np

class SLP(object):
    def __init__(self, input_size, learning_rate=1, epochs=1000):
        self.Weights = np.zeros(input_size + 1)
        print("Creating weight vector, 1D Array with Zeros", self.Weights)
        self.epochs = epochs
        self.learning_rate = learning_rate

    def activation_function(self, input_value):
        return 1 if input_value >= 0 else 0

    def predict(self, input_value):
        z = self.Weights.T.dot(input_value)
        a = self.activation_function(z)
        return a

    def perceptronLearning(self, given_input, desired_output):
        for j in range(self.epochs):
            for i in range(desired_output.shape[0]):
                x = np.insert(given_input[i], 0, 1)
                y = self.predict(x)
                e = desired_output[i] - y

                print("Error: ", e)
                print("Predicted Output: ", y)
                self.Weights = self.Weights + self.learning_rate * e * x

# OR Gate
given_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
desired_output = np.array([0, 1, 1, 1])

slp = SLP(input_size=2, epochs=5)
slp.perceptronLearning(given_input, desired_output)

print("Input Weight with bias: ", slp.Weights)
print("Learning Rate: ", slp.learning_rate)
print("Total Epochs: ", slp.epochs)
"""
    print(code)


def mlp():
    code = """
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
y = np.array([0, 1, 1, 0])  # XOR gate
# y= np.array([1, 0, 0, 1])  # XNOR gate

no_x = 2
no_y = 1
no_h = 2
tot = x.shape[1]
lr = 0.1
np.random.seed(2)

w1 = np.random.rand(no_h, no_x)
w2 = np.random.rand(no_y, no_h)

losses = []

def back_prop(tot, w1, w2, z1, a1, z2, a2, y):
    dz2 = a2 - y
    dw2 = np.dot(dz2, a1.T) / tot
    dz1 = np.dot(w2.T, dz2) * a1 * (1 - a1)
    dw1 = np.dot(dz1, x.T) / tot
    dw1 = np.reshape(dw1, w1.shape)
    dw2 = np.reshape(dw2, w2.shape)
    return dz2, dw2, dz1, dw1

epochs = 20000

def sigmoid(z):
    z = 1 / (1 + np.exp(-z))
    return z

def frwd_prop(w1, w2, x):
    z1 = np.dot(w1, x)
    a1 = sigmoid(z1)
    z2 = np.dot(w2, a1)
    a2 = sigmoid(z2)
    return z1, a1, z2, a2

for i in range(epochs):
    z1, a1, z2, a2 = frwd_prop(w1, w2, x)
    loss = -(1 / tot) * np.sum(y * np.log(a2) + (1 - y) * np.log(1 - a2))
    losses.append(loss)
    da2, dw2, dz1, dw1 = back_prop(tot, w1, w2, z1, a1, z2, a2, y)
    w2 = w2 - lr * dw2
    w1 = w1 - lr * dw1

plt.plot(losses)
plt.xlabel("Epochs")
plt.ylabel("Loss Value")

def predict(w1, w2, input):
    z1, a1, z2, a2 = frwd_prop(w1, w2, mlp_test)
    a2 = np.squeeze(a2)
    if a2 >= 0.5:
        print("For Input", [i[0] for i in input], "Output is 1")
    else:
        print("For Input", [i[0] for i in input], "Output is 0")

mlp_test = np.array([[1], [0]])
predict(w1, w2, mlp_test)
mlp_test = np.array([[0], [0]])
predict(w1, w2, mlp_test)
mlp_test = np.array([[0], [1]])
predict(w1, w2, mlp_test)
mlp_test = np.array([[1], [1]])
predict(w1, w2, mlp_test)
"""
    print(code)


def dt():
    code = """
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("./salaries.csv")

inputs = df.drop("salary_more_then_100k", axis="columns")
target = df["salary_more_then_100k"]

le_company = LabelEncoder()

inputs["company_n"] = le_company.fit_transform(inputs["company"])

inputs_n = inputs.drop(["company", "job", "degree"], axis="columns")

model = tree.DecisionTreeClassifier()

model.fit(inputs_n, target)
model.score(inputs_n, target)
"""
    print(code)


def km():
    code = """
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("income.csv")

scaler = MinMaxScaler()

scaler.fit(df[["Income($)"]])
df["Income($)"] = scaler.transform(df[["Income($)"]])
scaler.fit(df[["Age"]])
df["Age"] = scaler.transform(df[["Age"]])

plt.scatter(df.Age, df["Income($)"])

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[["Age", "Income($)"]])
y_predicted

df["cluster"] = y_predicted

km.cluster_centers_

df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

plt.scatter(df1.Age, df1["Income($)"], color="green")
plt.scatter(df2.Age, df2["Income($)"], color="red")
plt.scatter(df3.Age, df3["Income($)"], color="black")
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color="purple", marker="*", label="centroid")
plt.legend()

sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Age', 'Income($)']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng, sse)
"""
    print(code)


def ga():
    code = """
import random 
best = -100000
populations = ([[random.randint(0,1) for x in range(6)] for i in range(4)])
print(type(populations))
parents = []
new_populations = []
print(populations)

def fitness_score():
    global populations , best
    fit_value = []
    fit_score = []
    for i in range(4):
        chromosome_value = 0
        
        for j in range(5,0,-1):
            chromosome_value += populations[i][j]*(2**(5-j))
        chromosome_value = -1*chromosome_value if populations[i][0] == 1 else chromosome_value
        print(chromosome_value)
        fit_value.append(-(chromosome_value**2)+5)
    print('fit value : ',fit_value)
    fit_value,populations = zip(*sorted((zip(fit_value,populations)),reverse= True))
    best = fit_value[0]
    
fitness_score()

def selectparent():
    global parents
    parents = populations[0:2]
    print(type(parents))
    print(parents)
selectparent()

def crossover():
    global parents
    
    cross_point = random.randint(0,5)
    parents = parents + tuple([(parents[0][0:cross_point + 1] + parents[1][cross_point + 1:6])])
    parents = parents + tuple([(parents[1][0:cross_point + 1] + parents[0][cross_point + 1:6])])
    
    print(parents)

def mutation():
    global populations, parents
    mute = random.randint(0,49)
    if mute == 20:
        x = random.randint(0,3)
        y = random.randint(0,5)
        parents[x][y] = 1 - parents[x][y]
    populations = parents
    print(populations)

for i in range(1000):
    fitness_score()
    selectparent()
    crossover()
    mutation()
print("best score: ")
print(best)
print("sequence.........")
print(populations[0])
"""
    print(code)


ga()
