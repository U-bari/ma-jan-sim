
import os
import csv


#data読み込み
with open('data/M 2018-10.csv') as f:
	reader = csv.reader(f)
	data_2018_10 = [x for x in reader]

with open('data/M 2018-11.csv') as f:
	reader = csv.reader(f)
	data_2018_11 = [x for x in reader]
	
with open('data/M 2018-12.csv') as f:
	reader = csv.reader(f)
	data_2018_12 = [x for x in reader]

with open('data/M 2019-1.csv') as f:
	reader = csv.reader(f)
	data_2019_1 = [x for x in reader]

with open('data/M 2019-2.csv') as f:
	reader = csv.reader(f)
	data_2019_2 = [x for x in reader]

with open('data/M 2019-3.csv') as f:
	reader = csv.reader(f)
	data_2019_3 = [x for x in reader]

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

data_list = [data_2018_10, data_2018_11, data_2018_12, data_2019_1, data_2019_2, data_2019_3, data_2019_10, data_2019_11, data_2019_12, data_2020_1, data_2020_2, data_2020_3, data_2020_6]
time = ["2018_10","2018_11","2018_12","2019_1","2019_2","2019_3", "2019_10","2019_11","2019_12","2020_1","2020_2","2020_3","2020_6"]
