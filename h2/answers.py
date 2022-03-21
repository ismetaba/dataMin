import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn.neighbors import DistanceMetric

csv_path="data.csv"
data = pd.read_csv(csv_path, sep=';')
feduData = data['Fedu']
meduData = data['Medu']

print ("Standart Dev of health data: ")
print (statistics.stdev(feduData))
print ("--------")

print ("Coorelation of Fedu and Medu: ")
print (np.corrcoef(feduData, meduData))
plt.matshow(data.corr())
plt.show()
print ("--------")
s1 = DistanceMetric.get_metric('manhattan').pairwise(data[['Fedu']])

print ("scatter plot of Fedu and Medu: ")
plt.scatter(feduData, meduData)
plt.show()
print ("--------")
s1 = s1/max(np.ptp(feduData),1)

def calculate_gower_distance(X):
    individual_variable_distances = []
    for i in range(X.shape[1]):
        feature = X.iloc[:, [i]]
        if feature.dtypes.values == np.object:
            feature_dist = DistanceMetric.get_metric('dice').pairwise(pd.get_dummies(feature))
        else:
            feature_dist = DistanceMetric.get_metric('manhattan').pairwise(feature) / max(np.ptp(feature.values), 1)
        individual_variable_distances.append(feature_dist)
    return np.array(individual_variable_distances).mean(0)

print ("box plot of Fedu and Medu: ")
plt.boxplot(feduData)
plt.show()
plt.boxplot(meduData)
plt.show()
print ("--------")

print ("box plot of Fedu and Medu: ")
print (calculate_gower_distance(data))
