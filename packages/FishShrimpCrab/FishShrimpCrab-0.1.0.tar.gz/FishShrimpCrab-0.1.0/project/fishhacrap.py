
def play():
	print ("fish,ha,crap,cock,money,8")
	
	import random 
	
	cmove = ("fish","ha","crap","cock","money","8")
	player1 = input("press 1 to start: ")
	
	while player1 == "1":
		result1 = random.choice(cmove)
		result2 = random.choice(cmove)
		result3 = random.choice(cmove)
	
		print(result1)
		print(result2)
		print(result3)
	
		new_game = input("Press y to start a new match(y/n)")
		if new_game == "y":
			p1ayer1 = 1 
		else:
			player1 = 0
			print("Thanks For Playing")
