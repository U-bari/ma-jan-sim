import matplotlib.pyplot as plt
import data

time = data.time

#dataごとにレーティング
def rating(data,rate,K=16):
	#iはdataのi列目を表す -> i番目の試合結果のデータ
	for i in range(len(data)):
		#i番目のデータの順位をrankとする
		for rank in range(4):
			prob = []
			for k in range(4):
				if k != rank:
					prob.append(1/(10**((int(rate[data[i][k]]) - int(rate[data[i][rank]]))/400) + 1))
			expectation = prob[0]*(1-prob[1])*(1-prob[2]) + prob[1]*(1-prob[0])*(1-prob[2]) + prob[2]*(1-prob[1])*(1-prob[0]) + 2*(prob[0]*prob[1]*(1-prob[2])) + 2*(prob[2]*prob[1]*(1-prob[0])) + 2*(prob[0]*prob[2]*(1-prob[1])) + 3*prob[0]*prob[1]*prob[2]
			rate[data[i][rank]] += K*((3 - rank) - expectation)
	return rate

def member_make(data,team):
	new_team = set([])
	for i in range(len(data)):
		for j in range(4):
			new_team.add(data[i][j])
	team = team | new_team
	return team

def make_rate(team,rate):
	for name in team:
		if name not in rate:
			rate[name] = 1500
	return rate

def expect(A,B,C,D,rate):
	player = [A,B,C,D]
	A_prob = []
	B_prob = []
	C_prob = []
	D_prob = []
	prob_list = [A_prob, B_prob, C_prob, D_prob]
	compare_prob_list = []
	#以下のfor文では　me vs enemy　の確率計算をしてW where is prob_listに追加してる
	for i, W in zip(list(range(4)), prob_list):
		prob = []
		me = player[i]
				
		#----------------------------------------
		#ここは正しい計算方法だが、同一選手が入力されたとき適切に判断できない

		"""
		for enemy in player:
			if enemy != me:
				prob.append(1/(10**((int(rate[enemy]) - int(rate[me]))/400) + 1))
		"""
		#----------------------------------------
		
		#同一選手の入力に対応したもの
		for j in range(4):
			if i != j:
				enemy = player[j]
				prob.append(1/(10**((int(rate[enemy]) - int(rate[me]))/400) + 1))

		expectation = prob[0]*(1-prob[1])*(1-prob[2]) + prob[1]*(1-prob[0])*(1-prob[2]) + prob[2]*(1-prob[1])*(1-prob[0]) + 2*(prob[0]*prob[1]*(1-prob[2])) + 2*(prob[2]*prob[1]*(1-prob[0])) + 2*(prob[0]*prob[2]*(1-prob[1])) + 3*prob[0]*prob[1]*prob[2]
		
		#絶対的な確立計算
		W.append(prob[0]*prob[1]*prob[2])
		W.append((prob[0]*prob[1]*(1-prob[2])) + (prob[2]*prob[1]*(1-prob[0])) + (prob[0]*prob[2]*(1-prob[1])))
		W.append(prob[0]*(1-prob[1])*(1-prob[2]) + prob[1]*(1-prob[0])*(1-prob[2]) + prob[2]*(1-prob[1])*(1-prob[0]))
		W.append((1 - prob[0])*(1-prob[1])*(1-prob[2]))

	#相対的な順位計算
	for i in list(range(4)):
		compare_prob_list.append([A_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i]),
			B_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i]),
			C_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i]),
			D_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i])]
			)
	return compare_prob_list

def expect_ave(A,B,C,D,rate):
	player = [A,B,C,D]
	expe = []
	for i in range(4):
		me = player[i]
		prob = []
				
		#----------------------------------------
		#ここは正しい計算方法だが、同一選手が入力されたとき適切に判断できない

		"""
		for enemy in player:
			if enemy != me:
				prob.append(1/(10**((int(rate[enemy]) - int(rate[me]))/400) + 1))
		"""
		#----------------------------------------
		
		#同一選手の入力に対応したもの
		for j in range(4):
			if i != j:
				enemy = player[j]
				prob.append(1/(10**((int(rate[enemy]) - int(rate[me]))/400) + 1))

			
		expectation = prob[0]*(1-prob[1])*(1-prob[2]) + prob[1]*(1-prob[0])*(1-prob[2]) + prob[2]*(1-prob[1])*(1-prob[0]) + 2*(prob[0]*prob[1]*(1-prob[2])) + 2*(prob[2]*prob[1]*(1-prob[0])) + 2*(prob[0]*prob[2]*(1-prob[1])) + 3*prob[0]*prob[1]*prob[2]
		expe.append(4 - expectation)
	return expe
		

def rate_all(data_list,rate,A="",K=16):
	the_rate = []
	j = 0
	for i in data_list:
		rate = rating(i,rate,K) 
		try:
			the_rate.append(rate[A])
		except KeyError:
			if A != "":
				if j == 0:
					print("選手名が正しく入力されていません")
			else:	
				pass
		j += 1

	if the_rate != []:
		plt.plot(the_rate)
		plt.ylim([1400,1650])
		plt.xticks(list(range(len(data_list))),time)
		plt.show()

	return rate

