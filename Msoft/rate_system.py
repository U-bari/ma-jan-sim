import matplotlib.pyplot as plt
import data

time = data.time

def rating(data,rate,K=16):
	for i in range(len(data)):
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
	for me, W in zip(player, prob_list):
		prob = []
		#me:enemy確率計算
		for enemy in player:
			if enemy != me:
				prob.append(1/(10**((int(rate[enemy]) - int(rate[me]))/400) + 1))
		expectation = prob[0]*(1-prob[1])*(1-prob[2]) + prob[1]*(1-prob[0])*(1-prob[2]) + prob[2]*(1-prob[1])*(1-prob[0]) + 2*(prob[0]*prob[1]*(1-prob[2])) + 2*(prob[2]*prob[1]*(1-prob[0])) + 2*(prob[0]*prob[2]*(1-prob[1])) + 3*prob[0]*prob[1]*prob[2]
		#絶対的な確立計算
		W.append(prob[0]*prob[1]*prob[2])
		W.append((prob[0]*prob[1]*(1-prob[2])) + (prob[2]*prob[1]*(1-prob[0])) + (prob[0]*prob[2]*(1-prob[1])))
		W.append(prob[0]*(1-prob[1])*(1-prob[2]) + prob[1]*(1-prob[0])*(1-prob[2]) + prob[2]*(1-prob[1])*(1-prob[0]))
		W.append((1 - prob[0])*(1-prob[1])*(1-prob[2]))
		print("")
		print(me)
		print("レート　　　  " +  str(rate[me]))
		print("平均順位　　　" + str(4 - expectation))
	#相対的な順位計算
	for me, i in zip(player,list(range(4))):
		print(A_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i]),
			B_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i]),
			C_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i]),
			D_prob[i]/(A_prob[i]+B_prob[i]+C_prob[i]+D_prob[i])
		)
		

def rate_all(data_list,rate,A,K=16):
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