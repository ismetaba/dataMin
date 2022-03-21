import pandas as pd
import math
import matplotlib.pyplot as plt

csv_path="data.csv"
data = pd.read_csv(csv_path, sep=';')
healthData = data['health']
absencesData = data['absences']


# Q1
def calculateMean(sample):
    return sum(sample) / len(sample)

def calculateStandartDeviations(sample):
    mean = calculateMean(sample)
    size = len(sample)
    sum = 0
    for i in sample:
        sum += pow(i - mean, 2)
    return math.sqrt(sum / size)

def calculateZScore(value, data):
    return (value - calculateMean(data))/ calculateStandartDeviations(data)

def calculateNormalizedValue(value, data):
    return (value - data.min()) / (data.max() - data.min())

mean1 = calculateMean(healthData)
mean2 = calculateMean(absencesData)
print ('Means : ')
print (mean1)
print (mean2)
print ('---------')

print ('Standart Deviations : ')
std1 = calculateStandartDeviations(healthData)
std2 = calculateStandartDeviations(absencesData)
print (std1)
print (std2)
print ('---------')

print ('Z-Skores : ')
zScore1 = calculateZScore(1 ,healthData)
zScore2 = calculateZScore(1 ,absencesData)
print (zScore1)
print (zScore2)
print ('---------')

print ('Normalized Datas : ')
normalized_on_health_data = calculateNormalizedValue(2, healthData)
normalized_on_absences_data = calculateNormalizedValue(2, absencesData)
print (normalized_on_health_data)
print (normalized_on_absences_data)

# Q2
def calculateMedian(data):
    n = len(data)
    index = n // 2
    if n % 2:
        return sorted(data)[index]
    return sum(sorted(data)[index - 1:index + 1]) / 2

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def calculateFirstQuartiles(data):
    sortedData = sorted(data)
    return calculateMedian(sortedData[:int(len(sortedData) / 2)])

def calculateThirdQuartiles(data):
    sortedData = sorted(data)
    return calculateMedian(sortedData[int(len(sortedData) / 2):])

def calculateIQR(data):
    return calculateThirdQuartiles(sorted(data)) - calculateFirstQuartiles(sorted(data))

csv_path="data.csv"
data = pd.read_csv(csv_path, sep=';')
healthData = data['health']
absencesData = data['absences']

print ('Means : ')
median1 = calculateMedian(healthData)
median2 = calculateMedian(absencesData)
print (median1)
print (median2)
print ('---------')

print ('First Quartiles : ')
firstQuartile1 = calculateFirstQuartiles(healthData)
firstQuartile2 = calculateFirstQuartiles(absencesData)
print (firstQuartile1)
print (firstQuartile2)
print ('---------')

print ('Third Quartiles : ')
thirdQuartile1 = calculateThirdQuartiles(healthData)
thirdQuartile2 = calculateThirdQuartiles(absencesData)
print (thirdQuartile1)
print (thirdQuartile2)
print ('---------')

print ('IQR : ')
iqr1 = calculateIQR(healthData)
iqr2 = calculateIQR(absencesData)
print (iqr1)
print (iqr2)
print ('---------')

#Q3
csv_path="data.csv"
data = pd.read_csv(csv_path, sep=';')
healthData = data['health']
absencesData = data['absences']

plt.style.use('ggplot')
plt.hist(healthData, bins=10)
plt.show()


plt.style.use('ggplot')
plt.hist(absencesData, bins=10)
plt.show()

#Q4
csv_path="data.csv"
data = pd.read_csv(csv_path, sep=';')
healthData = data['health']
absencesData = data['absences']

fig = plt.figure(figsize=(10, 7))
plt.boxplot(healthData)
plt.show()

plt.boxplot(absencesData)
plt.show()