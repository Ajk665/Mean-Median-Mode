import pandas as pd
import statistics
import csv
df = pd.read_csv('height-weight.csv')
heightlist = df['Height(Inches)'].to_list()
weightlist = df['Weight(Pounds)'].to_list()

heightmean = statistics.mean(heightlist)
weightmean = statistics.mean(weightlist)

heightmode = statistics.mode(heightlist)
weightmode = statistics.mode(weightlist)

heightmedian = statistics.median(heightlist)
weightmedian = statistics.median(weightlist)

print('mean, median, mode of height is:{} , {} and {} respectively'.format(heightmean,heightmode,heightmedian))
print('mean, median, mode of weight is:{} , {} and {} respectively'.format(weightmean,weightmode,weightmedian))