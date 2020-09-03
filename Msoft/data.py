
import os
import csv


#data読み込み
with open('data/M 2019-10.csv') as f:
	reader = csv.reader(f)
	data_2019_10 = [x for x in reader]

with open('data/M 2019-11.csv') as f:
	reader = csv.reader(f)
	data_2019_11 = [x for x in reader]
	
with open('data/M 2019-12.csv') as f:
	reader = csv.reader(f)
	data_2019_12 = [x for x in reader]

with open('data/M 2020-1.csv') as f:
	reader = csv.reader(f)
	data_2020_1 = [x for x in reader]

with open('data/M 2020-2.csv') as f:
	reader = csv.reader(f)
	data_2020_2 = [x for x in reader]

with open('data/M 2020-3.csv') as f:
	reader = csv.reader(f)
	data_2020_3 = [x for x in reader]

with open('data/M 2020-6.csv') as f:
	reader = csv.reader(f)
	data_2020_6 = [x for x in reader]

data_list = [data_2019_10, data_2019_11, data_2019_12, data_2020_1, data_2020_2, data_2020_3, data_2020_6]
time = ["2019_10","2019_11","2019_12","2020_1","2020_2","2020_3","2020_6"]
