import os
import csv
import rate_system
import data



data_list = data.data_list

#初期rate生成
rate = {}
member = set([])

for i in data_list:
	member = rate_system.member_make(i,member)

rate = rate_system.make_rate(member,rate)

#レーティング
for i in data_list:
	rate = rate_system.rating(i,rate)

for name, point in rate.items():
	print(name + ":" + str(point))
