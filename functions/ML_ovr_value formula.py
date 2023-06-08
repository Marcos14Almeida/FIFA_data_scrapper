# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:05:07 2023

@author: marcos
"""
import numpy as np
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pickle

# create input and output data
# GOL 0, ZAG 1, VOL 2, MEI 3, ATA 4
data = [
    (35, 45, 4, 90),
    (24, 180, 4, 92),
    (31, 70, 4, 89),
    (37, 6, 1, 82),
    (24, 50, 0, 86),
    (28, 70, 1, 89),
    (24, 70, 1, 84),
    (27, 35, 1, 83),
    (30, 60, 0, 90),
    (25, 70, 1, 85),
    (30, 50, 1, 84),
    (33, 18, 3, 86),
    (37, 10, 3, 89),
    (22, 120, 4, 88),
    (22, 80, 4, 84),
    (35, 35, 4, 89),
    (20, 60, 2, 82),
    (23, 90, 2, 84),
    (31, 5, 1, 86),
    (27, 35, 1, 82),
    (26, 2, 1, 76),
    (36, 0.6, 0, 77),
    (28, 16, 0, 81),
    (27, 8, 1, 79),
    (35, 3, 1, 82),
    (29, 8, 3, 79),
    (21, 40, 4, 83),
    (30, 14, 3, 82),
    (27, 25, 1, 82),
    (28, 19, 3, 83),
    (27, 12, 4, 80),
    (33, 4.5, 3, 80),
    (35, 0.8, 1, 78),
    (22, 8, 1, 78),
    (25, 6, 1, 79),
    (25, 40, 2, 82, "Bennacer"),
    (23, 15, 4, 80, "Saelemaekers"),
    (29, 10, 4, 80, "Rebic"),
    (23, 15, 2, 76, "Pobega"),
    (27, 0.15, 2, 73, "Djavan BotafogoPB"),
    (76, 36, 2.5, 79, "Hulk"),
    (45, 1, 0, 77, "Buffon"),
    (28, 2, 1, 70, "Osorio Parma"),
    (36, 0.5, 1, 71, "Ansaldi"),
    (21, 6, 2, 69, "Bernabé"),
    (31, 1.3, 4, 70, "Inglese"),
    (22, 1.8, 4, 65, "Benedyczak"),
    (16, 20, 4, 73, "Endrick"),
    (27, 2, 2, 78, "Jailson"),
    (25, 3, 3, 76, "Atuesta"),
    (36, 0.4, 3, 76, "Lomba"),
    (34, 0.3, 4, 77, "Bruno Mezenga"),
    (25, 0.15, 2, 73, "Thiaguinho Agua Santa"),
    (28, 4.5, 4, 76, "Ademir Bahia"),
    (31, 4.5, 1, 78, "Vitor Hugo Bahia"),
    (28, 4.5, 1, 78, "Paulo Díaz"),
    (33, 3.5, 3, 79, "Nacho F."),
    (30, 5, 4, 77, "Borja"),
    (32, 2, 2, 76, "Aliendro"),
    (34, 1.2, 1, 78, "Casco"),
]

# create the X array
X = [[d[0], d[1], d[2]] for d in data]
y = [d[3] for d in data]

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.05, random_state=42
)

# create regression model and fit data
regressor = RandomForestRegressor()
regressor = GradientBoostingRegressor()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X)
mse = mean_squared_error(y, y_pred)

print("Mean Squared Error:", mse)

# predict values for new data
# Haaland, De Bruyne, Ederson, Dudu, Endrick
new_data = np.array([[22, 170, 4], [31, 80, 3], [29, 45, 0], [31, 12, 4], [16, 20, 4]])
predictions = regressor.predict(new_data)
print("Predictions:", [math.floor(x) for x in predictions])
print("Real:       ", [91, 89, 85, 81, 74])

new_data = np.array([[25, 0.15, 2]])
predictions = regressor.predict(new_data)
print("Predictions:", [math.floor(x) for x in predictions])

# save the model to a file
with open("model.pkl", "wb") as file:
    pickle.dump(regressor, file)
